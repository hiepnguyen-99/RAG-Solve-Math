import torch
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate
import google.generativeai as genai
from retrieval import *
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

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
model = genai.GenerativeModel("gemini-2.0-flash-lite")


def rewrite_query(query, k=5):
    query_rewrite_prompt = f"""
    Bạn là một trợ lý hữu ích, tạo ra {k} truy vấn tìm kiếm dựa trên một truy vấn đầu vào duy nhất theo nhiều góc độ ngữ nghĩa khác nhau.
    Yêu cầu:
    - Mỗi câu hỏi phải rõ ràng, dễ hiểu.
    - Không viết dài dòng; ngắn gọn, súc tích, không lan man.
    - Chỉ hiển thị danh sách các câu hỏi thay thế, mỗi câu trên một dòng mới.

    Câu hỏi gốc: {query}
    """
    response = model.generate_content(query_rewrite_prompt)
    return response.text.strip().split('\n')


def promt_text(context, question):
    return f"""
    "Dựa trên thông tin sau, hãy trả lời ngắn gọn, đúng trọng tâm câu hỏi, chỉ sử dụng tài liệu liên quan đến câu hỏi nhất để trả lời, tài liệu không liên quan vui lòng bỏ qua, chỉ trả lời 1 lần không cần tóm lại và không lặp lại câu hỏi:\n"
        Thông tin \n{context}\n
        Câu hỏi: \n{question}\n"
        Trả lời:
    """

def flatten_docs(docs):
    """Flatten nested lists và chỉ giữ lại valid document objects"""
    flattened = []
    if not docs:
        return flattened
    
    for item in docs:
        if hasattr(item, 'page_content'):
            # Đây là document object hợp lệ
            flattened.append(item)
        elif isinstance(item, list):
            # Đây là nested list, flatten recursively
            flattened.extend(flatten_docs(item))
    
    return flattened


# Hàm chính giải toán qua API
def solve_question_api_gemini(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True):
    try:
        # Tạo queries
        if rewrite:
            queries = rewrite_query(question, 3)
            queries.append(question)  # Thêm câu hỏi gốc vào cuối
        else:
            queries = [question]

        # Retrieve documents
        if rerank and RERANK_AVAILABLE:
            try:
                reranker = FlagReranker(RERANK_MODEL, use_fp16=True)
                docs = retrieve_docs_RAG_fuson(queries, k=k, rerank=True, vectorstore=db, reranker=reranker)
            except Exception as e:
                print(f"⚠️ Lỗi rerank: {e}, tiếp tục không rerank.")
                docs = retrieve_docs_RAG_fuson(queries, k=k, rerank=False, vectorstore=db)
        else:
            docs = retrieve_docs_RAG_fuson(queries, k=k, rerank=False, vectorstore=db)

        # Flatten documents để xử lý nested lists
        docs = flatten_docs(docs)

        # Tạo context từ documents
        context = "\n".join([doc.page_content for doc in docs]) if docs else "Không tìm thấy tài liệu liên quan."
        
        # Gọi API Gemini
        response = model.generate_content(promt_text(context, question))
        answer = response.text if hasattr(response, 'text') else str(response)

        # Xử lý câu trả lời
        if question in answer:
            answer = answer.split(question)[-1].strip(": \n")

        if not answer.strip():
            fallback_prompt = f"Câu hỏi: {question}\nTrả lời ngắn gọn:"
            fallback_response = model.generate_content(fallback_prompt)
            answer = fallback_response.text if hasattr(fallback_response, 'text') else str(fallback_response)

        # Tạo source documents
        source_docs = [{"page_content": doc.page_content, "metadata": doc.metadata} for doc in docs]
        return answer.strip(), source_docs
        
    except Exception as e:
        return f"Lỗi khi xử lý câu hỏi với Gemini: {str(e)}", []