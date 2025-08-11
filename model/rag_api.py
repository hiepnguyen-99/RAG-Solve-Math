import os
import torch
import requests
from dotenv import load_dotenv
from transformers import pipeline
from rag_utils import *

# Load .env
load_dotenv()

# Sử dụng các utility functions
embedding_model = get_embedding_model()
db = get_chroma_db()

# Gọi API mô hình
def call_qwen_api(prompt: str):
    api_url = os.environ.get("API_URL", "https://api.together.xyz")
    api_key = os.environ.get("TOGETHER_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        "messages": [
            {"role": "system", "content": "Bạn là một trợ lý AI chuyên giải toán."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 512,
        "top_p": 0.9,
        "stop": ["<|im_end|>"]
    }

    response = requests.post(f"{api_url}/v1/chat/completions", headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    return None

def rewrite_query_api(query, k=5):
    """Rewrite query sử dụng template chung"""
    prompt = REWRITE_QUERY_PROMPT_TEMPLATE.format(query=query, k=k)
    output = call_qwen_api(prompt)
    return clean_rewrite_queries(output, query, k)

# Hàm chính giải toán
def solve_question_api(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True, conversation_history: list = None):
    """
    Giải câu hỏi với hỗ trợ conversation context
    """
    try:
        # Xây dựng conversation context sử dụng utility function
        conversation_context = build_conversation_context(conversation_history, question)
        
        # Tạo queries với rewrite
        if rewrite:
            enhanced_question = enhance_question_with_context(question, conversation_history)
            queries = rewrite_query_api(enhanced_question, 3)
            queries.append(question)  # Thêm câu hỏi gốc
        else:
            queries = [question]

        # Xử lý documents sử dụng utility function
        docs = process_retrieved_docs(queries, db, k, rerank)
        
        # Tạo context
        context = create_context_from_docs(docs)

        if not context:
            answer = handle_empty_context(question, call_qwen_api)
            return answer, [], []

        # Gọi API với prompt template chung
        prompt = create_base_prompt_template(context, question, conversation_context, "math")
        answer = call_qwen_api(prompt)

        # Làm sạch câu trả lời
        answer = clean_answer_response(answer, question)

        # Nếu rỗng, gọi lại
        if not answer.strip():
            answer = handle_empty_context(question, call_qwen_api)

        # Tạo source documents và rewrite queries
        source_docs = create_source_documents(docs)
        rewrite_queries = extract_rewrite_queries(queries, include_original=False)

        return answer, source_docs, rewrite_queries

    except Exception as e:
        print(f"Lỗi trong solve_question_api: {str(e)}")
        return f"Lỗi: {str(e)}", [], []
        return f"Lỗi trong quá trình xử lý: {str(e)}", [], []

# Hàm giải toán chuyên sâu sử dụng API của Qwen với LaTeX

def solve_math_question_api(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True, conversation_history: list = None):
    """
    Giải toán chi tiết từng bước, sử dụng LaTeX cho công thức.
    Trả về (answer, source_docs).
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
            queries = rewrite_query_api(enhanced_question, 3)
        else:
            queries = rewrite_query_api(question, 3)
        queries.append(question)  # Thêm câu hỏi gốc vào cuối
    else:
        queries = [question]

    # Collect documents từ tất cả queries
    docs = []
    for query in queries:
        retriever = db.as_retriever(search_kwargs={"k": k})
        doc = retriever.get_relevant_documents(query)
        
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
    context = "\n".join([split_combined_content(doc.page_content) for doc in docs]).strip()
    
    # Toán prompt với conversation context
    math_prompt = f"""
Bạn là trợ lý AI chuyên giải toán.

{conversation_context}

Dựa vào thông tin sau:
{context}
Hãy giải toán sau đây từng bước, biểu diễn công thức trong LaTeX (đặt giữa $$):
Câu hỏi: {question}
1. Phân tích.
2. Giải chi tiết.
3. Kết luận.
"""
    # Gọi API
    answer = call_qwen_api(math_prompt) or ""
    
    # Xử lý lặp lại
    if question in answer:
        answer = answer.split(question)[-1].strip()
    
    # Fallback
    if not answer.strip():
        answer = call_qwen_api(f"Câu hỏi: {question}\nGiải toán từng bước với LaTeX:") or ""
    
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