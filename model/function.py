import os
import torch
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from .retrieval import *
from .conversation_manager import conversation_manager


device = "cuda" if torch.cuda.is_available() else "cpu"
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
    chroma_path = os.getenv("CHROMA_DB_PATH", "./chroma_db")
    embedding_model = get_embedding_model()
    return Chroma(
        persist_directory=chroma_path,
        embedding_function=embedding_model,
        collection_name="math_vectors"
    )


def classify_question_type_generic(question: str, model_classify_func=None) -> str:
    """
    Phân loại loại câu hỏi bằng model AI hoặc pattern matching
    
    Args:
        question: Câu hỏi cần phân loại
        model_classify_func: Hàm phân loại của model cụ thể (optional)
    
    Returns:
        'math_solving': Cần giải toán trực tiếp  
        'knowledge_retrieval': Cần tìm kiếm tài liệu
    """
    
    # Nếu có hàm phân loại của model cụ thể, dùng nó
    if model_classify_func:
        try:
            result = model_classify_func(question)
            if result in ['math_solving', 'knowledge_retrieval']:
                return result
        except Exception as e:
            print(f"⚠️ Lỗi phân loại bằng model: {e}")
    
    # Fallback: Pattern matching thông minh
    return classify_by_pattern(question)


def classify_by_pattern(question: str) -> str:
    """
    Phương pháp fallback: Phân loại bằng pattern matching thông minh
    """
    import re
    
    question_lower = question.lower()
    
    # Pattern 1: Có biểu thức toán học cụ thể
    math_expressions = [
        r'f\(.*\)\s*=',  # f(x) = ...
        r'[a-z]\s*=\s*\d',  # x = 5
        r'\d+[a-z]\s*[+\-*/]',  # 2x + ...
        r'[+\-*/=]\s*\d',  # = 5, + 3
        r'\d+\s*[+\-*/]\s*\d',  # 2 + 3
        r'sin\(|cos\(|tan\(|log\(',  # sin(x)
        r'\[.*\d.*\]',  # [1 2; 3 4]
        r'ma\s*trận.*[=].*\d',  # ma trận A = [...]
    ]
    
    for pattern in math_expressions:
        if re.search(pattern, question):
            return 'math_solving'
    
    # Pattern 2: Từ khóa lý thuyết mạnh
    theory_patterns = [
        r'\b(là\s+gì|định\s+nghĩa|khái\s+niệm)\b',
        r'\b(cách\s+\w+|phương\s+pháp|làm\s+thế\s+nào)\b',
        r'\b(cho\s+ví\s+dụ|ví\s+dụ\s+về)\b',
        r'\b(giải\s+thích|trình\s+bày|mô\s+tả)\b',
        r'\b(có\s+những|các\s+loại|phân\s+loại)\b',
        r'\b(định\s+lý|tính\s+chất|đặc\s+điểm)\b'
    ]
    
    for pattern in theory_patterns:
        if re.search(pattern, question_lower):
            return 'knowledge_retrieval'
    
    # Pattern 3: Phân tích ngữ cảnh từ "tính"
    if 'tính' in question_lower:
        # Nếu có "cách tính", "phương pháp tính" → lý thuyết
        if re.search(r'\b(cách|phương\s+pháp|để)\s+tính\b', question_lower):
            return 'knowledge_retrieval'
        # Nếu có số cụ thể hoặc biến → giải toán
        elif re.search(r'\d+|[a-z]\(.*\)', question):
            return 'math_solving'
    
    # Mặc định: knowledge_retrieval (an toàn)
    return 'knowledge_retrieval'


# Compatibility function - giữ lại để không phá code cũ
def classify_question_type(question: str) -> str:
    """
    Hàm tương thích với code cũ - sử dụng pattern matching
    """
    return classify_by_pattern(question)