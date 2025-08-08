import torch
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate
from langchain.prompts import PromptTemplate as MathPromptTemplate
import google.generativeai as genai
from retrieval import *
from dotenv import load_dotenv


RERANK_MODEL = "BAAI/bge-reranker-base"
device = "cuda" if torch.cuda.is_available() else "cpu"

# Nếu có FlagEmbedding để rerank
try:
    from FlagEmbedding import FlagReranker
    RERANK_AVAILABLE = True
except ImportError:
    print("⚠️ FlagEmbedding không có, bỏ qua reranking.")
    RERANK_AVAILABLE = False
    FlagReranker = None


# Embedding
embedding_model = HuggingFaceEmbeddings(
    model_name="Qwen/Qwen3-Embedding-0.6B",
    model_kwargs={"device": device},
    encode_kwargs={"normalize_embeddings": True}
)

# Chroma
chroma_path = "./chroma_db"
db = Chroma(
    persist_directory=chroma_path,
    embedding_function=embedding_model,
    collection_name="math_vectors"
)


# Gọi API mô hình
api_key = os.getenv("GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash")


def rewrite_query(query, k=5):
    query_rewrite_prompt = f"""
    Từ truy vấn:
    "{query}"
    Hãy tạo {k} truy vấn chuyên biệt,
    Mỗi truy vấn tập trung vào một khía cạnh kiến thức toán học cần thiết để trả lời đầy đủ câu gốc, bao gồm : định nghĩa, định lý, ký hiệu, phương pháp, ví dụ, hoặc lĩnh vực liên quan.
    Yêu cầu:
    - Mỗi truy vấn ngắn gọn, rõ ràng, trực tiếp, không lan man, tránh gây nhiễu khi truy vấn.
    - Mỗi truy vấn thể hiện một mục tiêu tra cứu riêng biệt.
    - Chỉ in danh sách truy vấn, mỗi truy vấn một dòng.
    Câu hỏi gốc: {query}
    """
    response = model.generate_content(query_rewrite_prompt,
                                      generation_config={
                                        "temperature": 0.9,        
                                        "top_p": 0.8,              
                                        "top_k": 40,   
                                        }
                                      )
    return response.text.strip().split('\n')


def promt_text(context, question):
    return f"""
    "Dựa trên thông tin sau, hãy trả lời câu hỏi, 
    Khi trả lời, hãy tuân thủ nghiêm ngặt các quy định sau:
    - Nếu có sử dụng công thức toán học, hãy đặt công thức trong khối LaTeX dùng `$$` (hoặc trong code block Markdown nếu cần).
    - Không cần nói "Dựa trên thông tin được cung cấp"
    - Mỗi bước xuống dòng riêng.\n"
    Thông tin \n{context}\n
    Câu hỏi: \n{question}\n"
    Trả lời:
    """
# template cho giải toán step-by-step với LaTeX
math_template = MathPromptTemplate(
    input_variables=["context", "question"],
    template="""
Bạn là trợ lý AI chuyên giải các bài toán. Dựa vào thông tin sau:
{context}
Hãy giải bài toán sau đây từng bước một, hiển thị các công thức trong khối LaTeX (đặt giữa $$):
Câu hỏi: {question}
1. Phân tích.
2. Giải chi tiết.
3. Kết luận.
"""
)


def solve_question_api_gemini(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True, math: bool = False):
    """
    Hàm giải toán hoặc chat chung qua Gemini API.
    Nếu math=True thì sử dụng LaTeX step-by-step.
    """
    try:
        # Tạo queries
        if rewrite:
            queries = rewrite_query(question, 3)
            queries.append(question)  # Thêm câu hỏi gốc vào cuối
        else:
            queries = [question]

        docs = []
        for query in queries:
            retriever = db.as_retriever(search_kwargs={"k": k})
            doc = retriever.get_relevant_documents(query)
            if rerank and RERANK_AVAILABLE:
                try:
                    reranker = FlagReranker(RERANK_MODEL, use_fp16=True)
                    doc = rerank_docs_with_model(query, doc, reranker, num_doc=k)
                except Exception as e:
                    print(f"Lỗi khi rerank với FlagReranker: {str(e)}")
            docs.extend([doc])

        docs = reciprocal_rank_fusion(docs, num_docs=k)
        context = "\n".join([split_combined_content(doc.page_content) for doc in docs]) if docs else "Không tìm thấy tài liệu liên quan."
        
        # Gọi API Gemini với chế độ chung hoặc toán
        if math:
            prompt = math_template.format(context=context, question=question)
            gen_config = {"temperature": 0.9, "top_p": 0.8, "top_k": 40}
        else:
            prompt = promt_text(context, question)
            gen_config = {"temperature": 0.9, "top_p": 0.8, "top_k": 40}
        response = model.generate_content(prompt, generation_config=gen_config)
        answer = response.text.strip() if hasattr(response, 'text') else str(response)

        # Xử lý câu trả lời
        if question in answer:
            answer = answer.split(question)[-1].strip(": \n")

        if not answer.strip():
            fallback_prompt = f"Câu hỏi: {question}\nTrả lời ngắn gọn:"
            fallback_response = model.generate_content(fallback_prompt)
            answer = fallback_response.text if hasattr(fallback_response, 'text') else str(fallback_response)

        # Tạo source documents
        source_docs = []
        for doc in docs:
            source_docs.append({
                "page_content": split_combined_content(doc.page_content),
                "metadata": doc.metadata
            })
        
        # Tạo thông tin về rewrite queries riêng biệt
        rewrite_queries = []
        if rewrite and len(queries) > 1:
            rewrite_queries = queries[:-1]  # Loại bỏ câu hỏi gốc

        return answer.strip(), source_docs, rewrite_queries
    
    except Exception as e:
        return f"Lỗi khi xử lý câu hỏi với Gemini: {str(e)}", [], []


# Alias cho math-gemini-api: chỉ gọi solve_question_api_gemini với math=True
def solve_math_question_api_gemini(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True):
    """
    Alias chế độ toán dành cho math-gemini-api
    """
    return solve_question_api_gemini(question, k=k, rerank=rerank, rewrite=rewrite, math=True)
