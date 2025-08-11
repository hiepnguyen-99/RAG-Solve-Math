"""
RAG Utils - Các hàm tiện ích chung cho tất cả các RAG models
Chứa các hàm được dùng lại nhiều lần trong các file RAG khác nhau
"""

import os
import torch
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from retrieval import *
from conversation_manager import conversation_manager
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ===== Thiết bị và cấu hình chung =====
device = "cuda" if torch.cuda.is_available() else "cpu"
RERANK_MODEL = "BAAI/bge-reranker-base"

# ===== Kiểm tra FlagEmbedding =====
try:
    from FlagEmbedding import FlagReranker
    RERANK_AVAILABLE = True
except ImportError:
    print("⚠️ FlagEmbedding không có, bỏ qua reranking.")
    RERANK_AVAILABLE = False
    FlagReranker = None

# ===== Khởi tạo embedding model chung =====
def get_embedding_model():
    """Trả về embedding model chung cho tất cả RAG systems"""
    return HuggingFaceEmbeddings(
        model_name="Qwen/Qwen3-Embedding-0.6B",
        model_kwargs={"device": device},
        encode_kwargs={"normalize_embeddings": True}
    )

# ===== Khởi tạo Chroma database =====
def get_chroma_db():
    """Trả về Chroma database instance"""
    chroma_path = "./chroma_db"
    embedding_model = get_embedding_model()
    return Chroma(
        persist_directory=chroma_path,
        embedding_function=embedding_model,
        collection_name="math_vectors"
    )

# ===== Hàm xử lý conversation context =====
def build_conversation_context(conversation_history, question):
    """Xây dựng conversation context từ lịch sử"""
    if not conversation_history or not conversation_manager.should_use_context(question, conversation_history):
        return ""
    
    context = conversation_manager.build_conversation_context(conversation_history, question)
    print(f"🔄 Sử dụng conversation context: {len(context)} ký tự")
    return context

def enhance_question_with_context(question, conversation_history):
    """Cải thiện câu hỏi với context từ lịch sử trò chuyện"""
    if not conversation_history:
        return question
        
    topics = conversation_manager.extract_key_topics(conversation_history)
    if topics:
        return f"{question} (Liên quan: {', '.join(topics)})"
    return question

# ===== Hàm xử lý documents =====
def process_retrieved_docs(queries, db, k=3, rerank=False):
    """
    Xử lý việc retrieve và rerank documents từ multiple queries
    
    Args:
        queries: List các câu hỏi để tìm kiếm
        db: Chroma database instance
        k: Số lượng documents cần retrieve
        rerank: Có sử dụng reranking không
    
    Returns:
        List documents đã được xử lý
    """
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
        docs.append(doc)

    # Fusion tất cả documents
    all_docs = [doc for sublist in docs for doc in sublist]
    return reciprocal_rank_fusion([all_docs], num_docs=k)

def create_context_from_docs(docs):
    """Tạo context string từ list documents"""
    context = "\n".join([
        split_combined_content(doc.page_content) if doc.page_content else "" 
        for doc in docs
    ]).strip()
    return context

def create_source_documents(docs):
    """Tạo source documents cho response"""
    source_docs = []
    for doc in docs:
        source_docs.append({
            "page_content": split_combined_content(doc.page_content),
            "metadata": doc.metadata
        })
    return source_docs

# ===== Hàm xử lý rewrite queries =====
def extract_rewrite_queries(queries, include_original=False):
    """
    Trích xuất rewrite queries từ list queries
    
    Args:
        queries: List tất cả các queries
        include_original: Có bao gồm câu hỏi gốc không
    
    Returns:
        List rewrite queries (không bao gồm câu gốc nếu include_original=False)
    """
    if not queries or len(queries) <= 1:
        return []
    
    if include_original:
        return queries
    else:
        # Loại bỏ câu hỏi gốc (thường là câu cuối hoặc đầu)
        return queries[:-1] if queries[-1] == queries[0] else queries[1:]

# ===== Hàm xử lý fallback =====
def handle_empty_context(question, llm_caller):
    """
    Xử lý trường hợp không tìm thấy context phù hợp
    
    Args:
        question: Câu hỏi gốc
        llm_caller: Hàm gọi LLM (function pointer)
    
    Returns:
        Câu trả lời fallback
    """
    print("Không tìm thấy tài liệu liên quan. Chuyển sang trả lời bằng kiến thức mô hình.")
    fallback_prompt = f"Câu hỏi: {question}\nTrả lời ngắn gọn:"
    return llm_caller(fallback_prompt)

def clean_answer_response(answer, question):
    """
    Làm sạch câu trả lời để loại bỏ các phần không cần thiết
    
    Args:
        answer: Câu trả lời từ model
        question: Câu hỏi gốc
    
    Returns:
        Câu trả lời đã được làm sạch
    """
    if not answer:
        return ""
    
    # Xử lý lặp lại câu hỏi
    if question in answer:
        answer = answer.split(question)[-1].strip(": \n")
    
    return answer.strip()

# ===== Template cho prompt chung =====
def create_base_prompt_template(context, question, conversation_context="", style="default"):
    """
    Tạo prompt template cơ bản cho các model khác nhau
    
    Args:
        context: Nội dung tài liệu tham khảo
        question: Câu hỏi
        conversation_context: Ngữ cảnh trò chuyện
        style: Kiểu prompt ("default", "math", "concise")
    
    Returns:
        Prompt string
    """
    base_parts = []
    
    if style == "math":
        base_parts.append("Bạn là một trợ lý AI chuyên giải toán.")
    elif style == "concise":
        base_parts.append("Hãy trả lời ngắn gọn, đúng trọng tâm câu hỏi.")
    else:
        base_parts.append("Bạn là một trợ lý AI thông minh.")
    
    if conversation_context:
        base_parts.append(conversation_context)
    
    if context:
        if style == "math":
            base_parts.append("Dựa trên thông tin sau, hãy trả lời câu hỏi. Nếu có công thức toán học, hãy đặt trong khối LaTeX dùng $$.")
        else:
            base_parts.append("Hãy ưu tiên trả lời dựa vào thông tin sau nếu có:")
        base_parts.append(context)
    
    if style != "math":
        base_parts.append("Nếu không đủ thông tin, bạn có thể sử dụng kiến thức của mình để đưa ra câu trả lời chính xác nhất.")
    
    base_parts.extend([f"Câu hỏi: {question}", "Trả lời:"])
    
    return "\n\n".join(base_parts).strip()

# ===== Hàm kiểm tra và xử lý lỗi chung =====
def safe_execute(func, *args, **kwargs):
    """
    Thực thi function một cách an toàn với error handling
    
    Args:
        func: Function cần thực thi
        *args, **kwargs: Arguments cho function
    
    Returns:
        Tuple (success: bool, result: any, error: str)
    """
    try:
        result = func(*args, **kwargs)
        return True, result, None
    except Exception as e:
        error_msg = f"Lỗi trong {func.__name__}: {str(e)}"
        print(error_msg)
        return False, None, error_msg

# ===== Constants cho rewrite query prompts =====
REWRITE_QUERY_PROMPT_TEMPLATE = """
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

def clean_rewrite_queries(raw_output, original_query, max_queries=5):
    """
    Làm sạch output từ rewrite query function
    
    Args:
        raw_output: Raw output từ model
        original_query: Câu hỏi gốc
        max_queries: Số lượng queries tối đa
    
    Returns:
        List các queries đã được làm sạch
    """
    if not raw_output:
        return [original_query]
    
    # Tách thành các dòng
    if isinstance(raw_output, str):
        lines = raw_output.split('\n')
    elif isinstance(raw_output, list):
        lines = raw_output
    else:
        return [original_query]
    
    queries = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Loại bỏ các dòng không phải câu hỏi
        skip_words = ['okay', 'let\'s', 'first', 'user', 'think', 'wait', 'the', 'vui lòng']
        if any(word.lower() in line.lower() for word in skip_words):
            continue
        
        # Loại bỏ số thứ tự và ký hiệu đầu dòng
        import re
        line = re.sub(r'^\d+\.?\s*', '', line)  # "1. " hoặc "1 "
        line = re.sub(r'^[-•*]\s*', '', line)   # "- " hoặc "• "
        line = line.strip()
        
        # Kiểm tra độ dài và tính hợp lệ
        if line and len(line) > 10 and not line.lower().startswith(tuple(skip_words)):
            queries.append(line)
            
        if len(queries) >= max_queries:
            break
    
    # Đảm bảo luôn có ít nhất câu hỏi gốc
    if not queries:
        queries = [original_query]
    elif original_query not in queries:
        queries.append(original_query)
    
    return queries[:max_queries + 1]  # +1 để chứa câu gốc
