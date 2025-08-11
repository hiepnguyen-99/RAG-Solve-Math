import torch
import os
import requests
from dotenv import load_dotenv
from rag_utils import *

# Load ngrok URL from environment
load_dotenv()
NGROK_URL = os.getenv("NGROK_URL")

# Sử dụng các utility functions
embedding_model = get_embedding_model()
db = get_chroma_db()

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
    """Rewrite query sử dụng Qwen 4B"""
    prompt = f"Tạo {k} câu hỏi ngắn để tìm kiếm thông tin trả lời: \"{query}\"\n\nChỉ liệt kê {k} câu hỏi, mỗi câu một dòng:"
    
    if not NGROK_URL:
        print("Warning: NGROK_URL not configured, returning original query")
        return [query]
        
    response = call_qwen_4b(prompt, NGROK_URL)
    return clean_rewrite_queries(response, query, k)
def solve_question_4b(question: str, k: int = 3, ngrok_url: str = NGROK_URL, rerank: bool = False, rewrite: bool = True, conversation_history: list = None):
    """
    Giải câu hỏi với hỗ trợ conversation context sử dụng Qwen 4B
    """
    try:
        # Xây dựng conversation context sử dụng utility function
        conversation_context = build_conversation_context(conversation_history, question)
        
        # Tạo queries với rewrite
        if rewrite:
            enhanced_question = enhance_question_with_context(question, conversation_history)
            queries = rewrite_query_4b(enhanced_question, 3)
            queries.append(question)  # Thêm câu hỏi gốc
        else:
            queries = [question]

        # Xử lý documents sử dụng utility function
        docs = process_retrieved_docs(queries, db, k, rerank)
        
        # Tạo context
        context = create_context_from_docs(docs)

        if not context:
            answer = handle_empty_context(question, lambda p: call_qwen_4b(p, ngrok_url))
            return answer, [], []

        # Tạo prompt sử dụng utility function
        prompt = create_base_prompt_template(context, question, conversation_context, "concise")
        
        # Gửi prompt tới mô hình qua ngrok
        answer = call_qwen_4b(prompt, ngrok_url)

        # Làm sạch câu trả lời
        answer = clean_answer_response(answer, question)

        # Nếu không có câu trả lời rõ ràng, fallback
        if not answer.strip():
            answer = handle_empty_context(question, lambda p: call_qwen_4b(p, ngrok_url))

        # Tạo source documents và rewrite queries
        source_docs = create_source_documents(docs)
        rewrite_queries = extract_rewrite_queries(queries, include_original=False)

        return answer, source_docs, rewrite_queries

    except Exception as e:
        return f"Lỗi khi xử lý câu hỏi với Qwen 4B: {str(e)}", [], []
    if rewrite and len(queries) > 1:
        rewrite_queries = queries[:-1]  # Loại bỏ câu hỏi gốc

    return answer, source_docs, rewrite_queries

from langchain.prompts import PromptTemplate as MathPromptTemplate

def solve_math_question_4b(question: str, k: int = 3, ngrok_url: str = NGROK_URL, rerank: bool = False, rewrite: bool = True, conversation_history: list = None):
    """
    Giải toán bước-by-step, sử dụng biểu diễn LaTeX cho công thức.
    Trả về answer và source_docs.
    """
    # Xây dựng conversation context
    conversation_context = ""
    if conversation_history and conversation_manager.should_use_context(question, conversation_history):
        conversation_context = conversation_manager.build_conversation_context(conversation_history, question)
        print(f"🔄 Sử dụng conversation context: {len(conversation_context)} ký tự")
        
    # Tạo queries với rewrite
    if rewrite:
        if conversation_context:
            topics = conversation_manager.extract_key_topics(conversation_history)
            enhanced_question = question
            if topics:
                enhanced_question = f"{question} (Liên quan: {', '.join(topics)})"
            queries = rewrite_query_4b(enhanced_question, 3)
        else:
            queries = rewrite_query_4b(question, 3)
        queries.append(question)  # Thêm câu hỏi gốc vào cuối
    else:
        queries = [question]

    # Collect documents từ tất cả queries
    docs = []
    for query in queries:
        custom_retriever = db.as_retriever(search_kwargs={"k": k})
        doc = custom_retriever.invoke(query)
        
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
        input_variables=["context", "question", "conversation_context"],
        template="""
Bạn là trợ lý AI chuyên giải các bài toán.

{conversation_context}

Dựa vào thông tin sau:
{context}
Hãy giải bài toán sau đây từng bước một, không nhắc lại, không hiện suy nghĩ, hiển thị các công thức trong khối LaTeX (dùng $$):
Câu hỏi: {question}
Đầu ra:
1. Phân tích bài toán.
2. Giải các bước chi tiết kèm công thức.
3. Kết luận câu trả lời cuối cùng.
"""
    )
    prompt_text = math_template.format(
        context=context, 
        question=question, 
        conversation_context=conversation_context
    )
    
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
