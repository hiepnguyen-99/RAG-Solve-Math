import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFacePipeline
from retrieval import *

# Optional import for reranking
try:
    from FlagEmbedding import FlagReranker
    RERANK_AVAILABLE = True
except ImportError:
    print("Warning: FlagEmbedding not available. Reranking will be disabled.")
    RERANK_AVAILABLE = False
    FlagReranker = None

# 1. Thiết bị
device = "cuda" if torch.cuda.is_available() else "cpu"
# Load ngrok URL from environment
load_dotenv()
NGROK_URL = os.getenv("NGROK_URL")

# 2. Mô hình embedding
embedding_model = HuggingFaceEmbeddings(
    model_name="Qwen/Qwen3-Embedding-0.6B",
    model_kwargs={"device": device},
    encode_kwargs={"normalize_embeddings": True}
)

# 3. Load Chroma
chroma_path = "./chroma_db"
db = Chroma(
    persist_directory=chroma_path,
    embedding_function=embedding_model,
    collection_name="math_vectors"
)

# 4. Load LLM
import requests

# Configuration
RERANK_MODEL = "BAAI/bge-reranker-base"

def call_qwen_4b(prompt: str, ngrok_url: str):
    if not ngrok_url:
        return "Lỗi: NGROK_URL không được cấu hình"
    
    try:
        response = requests.post(f"{ngrok_url}/generate", json={"prompt": prompt})
        if response.status_code == 200:
            return response.json()["response"].strip()
        else:
            return f"Lỗi HTTP {response.status_code}: {response.text}"
    except requests.exceptions.ConnectionError:
        return f"Lỗi: Không thể kết nối đến server {ngrok_url}"
    except requests.exceptions.Timeout:
        return "Lỗi: Timeout khi kết nối đến server"
    except Exception as e:
        return f"Lỗi: {str(e)}"

def rewrite_query_4b(query, k=5):
    query_rewrite_prompt = f"""
    Với truy vấn sau:
    "{query}"
    Hãy phân tích và liệt kê **các thành phần kiến thức toán học cần thiết** để có thể trả lời truy vấn này một cách đầy đủ và chính xác. Bao gồm:
    - Các định nghĩa cần thiết
    - Các định lý hoặc mệnh đề liên quan
    - Ký hiệu hoặc biểu thức cần làm rõ
    - Quy trình hoặc phương pháp giải
    - Các ví dụ minh họa tiêu biểu
    - Các nhánh toán học liên quan (nếu có)
    Yêu cầu:
    - Chỉ in ra {k} câu truy vấn thay thế, mỗi câu liên quan đến một thành phần kiến thức khác nhau.
    - Mỗi câu phải rõ ràng, ngắn gọn, đi thẳng vào vấn đề không lan man để tránh gây nhiễu khi truy vấn.
    - Chỉ hiển thị danh sách các câu, mỗi câu trên một dòng mới.
    Câu hỏi gốc: {query}
    """
    
    if not NGROK_URL:
        print("Warning: NGROK_URL not configured, returning original query")
        return [query]
        
    response = call_qwen_4b(query_rewrite_prompt, NGROK_URL)
    
    if response and not response.startswith("Lỗi:"):
        queries = [q.strip() for q in response.split('\n') if q.strip()]
        return queries if queries else [query]
    else:
        print(f"Rewrite failed: {response}")
        return [query]


# PromptTemplate cần được khởi tạo với mẫu cụ thể
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
Bạn là một trợ lý AI thông minh, chỉ trả lời câu hỏi dựa trên thông tin đã cho:
{context}
Dựa vào thông tin trên, hãy trả lời câu hỏi sau một chính xác:
Câu hỏi: {question}
Trả lời:
"""
)

def solve_question_4b(question: str, k: int = 3, ngrok_url: str = NGROK_URL, rerank: bool = False, rewrite: bool = True):
    # Tạo queries với rewrite
    if rewrite:
        queries = rewrite_query_4b(question, 3)
        queries.append(question)  # Thêm câu hỏi gốc vào cuối
    else:
        queries = [question]

    # Collect documents từ tất cả queries
    docs = []
    for query in queries:
        custom_retriever = db.as_retriever(search_kwargs={"k": k})
        doc = custom_retriever.get_relevant_documents(query)
        
        # Apply reranking if enabled
        if rerank and doc and RERANK_AVAILABLE:
            try:
                reranker = FlagReranker(RERANK_MODEL, use_fp16=True)
                doc = rerank_docs_with_model(query, doc, reranker)
                print(f"Reranking applied to {len(doc)} documents")
            except Exception as e:
                print(f"Reranking failed: {e}, continuing without reranking...")
        elif rerank and not RERANK_AVAILABLE:
            print("Reranking requested but FlagEmbedding not available")
        
        docs.extend([doc])

    # Sử dụng reciprocal rank fusion để kết hợp kết quả
    docs = reciprocal_rank_fusion(docs, num_docs=k)
    
    # Lấy nội dung các tài liệu
    context = "\n".join([split_combined_content(doc.page_content) for doc in docs])

    # Áp dụng PromptTemplate để tạo prompt hoàn chỉnh
    prompt_text = prompt_template.format(context=context, question=question)

    # Gửi prompt tới mô hình qua ngrok
    answer = call_qwen_4b(prompt_text, ngrok_url)

    # Xử lý nếu mô hình lặp lại câu hỏi
    if question in answer:
        answer = answer.split(question)[-1].strip(": \n")

    # Nếu không có câu trả lời rõ ràng, fallback
    if not answer.strip():
        fallback_prompt = f"Câu hỏi: {question}\nTrả lời ngắn gọn:"
        answer = call_qwen_4b(fallback_prompt, ngrok_url)

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

    return answer, source_docs, rewrite_queries

from langchain.prompts import PromptTemplate as MathPromptTemplate

def solve_math_question_4b(question: str, k: int = 3, ngrok_url: str = NGROK_URL, rerank: bool = False, rewrite: bool = True):
    """
    Giải toán bước-by-step, sử dụng biểu diễn LaTeX cho công thức.
    Trả về answer và source_docs.
    """
    # Tạo queries với rewrite
    if rewrite:
        queries = rewrite_query_4b(question, 3)
        queries.append(question)  # Thêm câu hỏi gốc vào cuối
    else:
        queries = [question]

    # Collect documents từ tất cả queries
    docs = []
    for query in queries:
        custom_retriever = db.as_retriever(search_kwargs={"k": k})
        doc = custom_retriever.get_relevant_documents(query)
        
        # Rerank nếu cần
        if rerank and RERANK_AVAILABLE:
            try:
                reranker = FlagReranker(RERANK_MODEL, use_fp16=True)
                doc = rerank_docs_with_model(query, doc, reranker)
            except Exception:
                pass
        
        docs.extend([doc])

    # Sử dụng reciprocal rank fusion để kết hợp kết quả
    docs = reciprocal_rank_fusion(docs, num_docs=k)
    
    # Chuẩn bị context
    context = "\n".join([split_combined_content(doc.page_content) for doc in docs])
    
    # Math prompt template
    math_template = MathPromptTemplate(
        input_variables=["context", "question"],
        template="""
Bạn là trợ lý AI chuyên giải các bài toán. Dựa vào thông tin sau:
{context}
Hãy giải bài toán sau đây từng bước một, hiển thị các công thức trong khối LaTeX (dùng $$):
Câu hỏi: {question}
Đầu ra:
1. Phân tích bài toán.
2. Giải các bước chi tiết kèm công thức.
3. Kết luận câu trả lời cuối cùng.
"""
    )
    prompt_text = math_template.format(context=context, question=question)
    
    # Gọi API
    raw = call_qwen_4b(prompt_text, ngrok_url)
    
    # Xử lý
    answer = raw.strip()
    
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
    
    return answer, source_docs, rewrite_queries
