import torch
from function import *
from retrieval import *
from dotenv import load_dotenv
from conversation_manager import conversation_manager
import requests
# Thiết bị
device = "cuda" if torch.cuda.is_available() else "cpu"

embedding_model = get_embedding_model()
db = get_chroma_db()
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

load_dotenv()
# Load .env

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
    output = call_qwen_api(query_rewrite_prompt)

    if not output:
        return [query]

    questions = [q.strip("-•* \n") for q in output.split("\n") if q.strip()]
    return [query] + questions[:k]

# Tạo prompt với conversation context
def prompt_text(context, question, conversation_context=""):
    base_prompt = f"""
Bạn là một trợ lý AI thông minh. 

{conversation_context}

Hãy ưu tiên trả lời dựa vào thông tin sau nếu có:
{context}

Nếu không đủ thông tin, bạn có thể sử dụng kiến thức của mình để đưa ra câu trả lời chính xác nhất.

Câu hỏi: {question}
Trả lời:
""".strip()
    return base_prompt

# Hàm chính giải toán
def solve_question_api(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True, conversation_history: list = None):
    """
    Giải câu hỏi với hỗ trợ conversation context
    
    Args:
        question: Câu hỏi hiện tại
        k: Số lượng tài liệu retrieve
        rerank: Có sử dụng reranking không
        rewrite: Có rewrite query không
        conversation_history: Lịch sử trò chuyện (danh sách messages)
    """
    try:
        # Xây dựng conversation context
        conversation_context = ""
        if conversation_history and conversation_manager.should_use_context(question, conversation_history):
            conversation_context = conversation_manager.build_conversation_context(conversation_history, question)
            print(f"🔄 Sử dụng conversation context: {len(conversation_context)} ký tự")
        
        # Tạo queries với rewrite
        if rewrite:
            # Cải thiện query bằng context nếu có
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

        all_docs = [doc for sublist in docs for doc in sublist]
        docs = reciprocal_rank_fusion([all_docs], num_docs=k)

        # Tạo context
        context = "\n".join([split_combined_content(doc.page_content) if doc.page_content else "" for doc in docs]).strip()

        if not context:
            print("Không tìm thấy tài liệu liên quan. Chuyển sang trả lời bằng kiến thức mô hình.")
            fallback_prompt = f"Câu hỏi: {question}\nTrả lời ngắn gọn:"
            answer = call_qwen_api(fallback_prompt)
            return answer, [], []

        # Gọi API
        answer = call_qwen_api(prompt_text(context, question, conversation_context))

        # Xử lý lặp lại
        if question in answer:
            answer = answer.split(question)[-1].strip(": \n")

        # Nếu rỗng, gọi lại
        if not answer.strip():
            fallback_prompt = f"Câu hỏi: {question}\nTrả lời ngắn gọn:"
            answer = call_qwen_api(fallback_prompt)

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

    except Exception as e:
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