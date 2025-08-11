import torch
import os
import google.generativeai as genai
from dotenv import load_dotenv
from rag_utils import *

# Load environment variables first
load_dotenv()

# Sử dụng các utility functions
embedding_model = get_embedding_model()
db = get_chroma_db()

# Gọi API mô hình
api_key = os.getenv("GEMINI_API_KEY")
print(f"DEBUG: GEMINI_API_KEY = {api_key[:20]}..." if api_key else "DEBUG: GEMINI_API_KEY not found")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
    print("✅ Gemini model đã được cấu hình thành công")
else:
    print("⚠️ GEMINI_API_KEY không được cấu hình")
    model = None


def rewrite_query(query, k=5):
    """Rewrite query sử dụng Gemini API"""
    if not model:
        print("⚠️ Gemini model không khả dụng, trả về query gốc")
        return [query]
        
    prompt = REWRITE_QUERY_PROMPT_TEMPLATE.format(query=query, k=k)
    try:
        response = model.generate_content(prompt,
                                          generation_config={
                                            "temperature": 0.9,        
                                            "top_p": 0.8,              
                                            "top_k": 40,   
                                            }
                                          )
        return clean_rewrite_queries(response.text.strip().split('\n'), query, k)
    except Exception as e:
        print(f"⚠️ Lỗi khi rewrite query: {e}")
        return [query]


def solve_question_api_gemini(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True, math: bool = False, conversation_history: list = None):
    """
    Hàm giải toán hoặc chat chung qua Gemini API.
    Nếu math=True thì sử dụng LaTeX step-by-step.
    """
    try:
        # Kiểm tra model khả dụng
        if not model:
            return "Lỗi: GEMINI_API_KEY không được cấu hình. Vui lòng thiết lập biến môi trường GEMINI_API_KEY.", [], []
        
        # Xây dựng conversation context sử dụng utility function
        conversation_context = build_conversation_context(conversation_history, question)
        
        # Tạo queries với rewrite
        if rewrite:
            enhanced_question = enhance_question_with_context(question, conversation_history)
            queries = rewrite_query(enhanced_question, 3)
            queries.append(question)  # Thêm câu hỏi gốc
        else:
            queries = [question]

        # Xử lý documents sử dụng utility function
        docs = process_retrieved_docs(queries, db, k, rerank)
        
        # Tạo context
        context = create_context_from_docs(docs)
        if not context:
            context = "Không tìm thấy tài liệu liên quan."
        
        # Gọi API Gemini với prompt phù hợp
        if math:
            prompt = create_base_prompt_template(context, question, conversation_context, "math")
            prompt += "\n1. Phân tích.\n2. Giải chi tiết.\n3. Kết luận."
        else:
            prompt = create_base_prompt_template(context, question, conversation_context, "default")
        
        try:
            response = model.generate_content(prompt, generation_config={
                "temperature": 0.9, "top_p": 0.8, "top_k": 40
            })
            answer = response.text.strip() if hasattr(response, 'text') else str(response)
        except Exception as e:
            return f"Lỗi khi gọi Gemini API: {str(e)}", [], []

        # Làm sạch câu trả lời
        answer = clean_answer_response(answer, question)

        if not answer.strip():
            fallback_prompt = f"Câu hỏi: {question}\nTrả lời ngắn gọn:"
            try:
                fallback_response = model.generate_content(fallback_prompt)
                answer = fallback_response.text if hasattr(fallback_response, 'text') else str(fallback_response)
            except Exception as e:
                answer = f"Không thể tạo câu trả lời: {str(e)}"

        # Tạo source documents và rewrite queries
        source_docs = create_source_documents(docs)
        rewrite_queries = extract_rewrite_queries(queries, include_original=False)

        return answer.strip(), source_docs, rewrite_queries
    
    except Exception as e:
        return f"Lỗi khi xử lý câu hỏi với Gemini: {str(e)}", [], []


# Alias cho math-gemini-api: chỉ gọi solve_question_api_gemini với math=True
def solve_math_question_api_gemini(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True, conversation_history: list = None):
    """
    Alias chế độ toán dành cho math-gemini-api
    """
    return solve_question_api_gemini(question, k=k, rerank=rerank, rewrite=rewrite, math=True, conversation_history=conversation_history)
