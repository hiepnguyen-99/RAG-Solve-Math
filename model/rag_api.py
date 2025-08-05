import os
import torch
import requests
from dotenv import load_dotenv
from transformers import pipeline
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from retrieval import *

# Load .env
load_dotenv()

# Thiết bị
device = "cuda" if torch.cuda.is_available() else "cpu"

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

# Rerank config
RERANK_MODEL = "BAAI/bge-reranker-base"

# Kiểm tra FlagEmbedding
try:
    from FlagEmbedding import FlagReranker
    RERANK_AVAILABLE = True
except ImportError:
    print("⚠️ FlagEmbedding không có, bỏ qua reranking.")
    RERANK_AVAILABLE = False
    FlagReranker = None

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

def rewrite_query(query, k=5):
    query_rewrite_prompt = f""" 
Bạn là một trợ lý tìm kiếm tài liệu hữu ích, tạo ra {k} truy vấn tìm kiếm dựa trên một truy vấn đầu vào duy nhất theo nhiều góc độ ngữ nghĩa khác nhau, sao cho:
- Giữ nguyên ý nghĩa chính
- Mỗi câu dùng cách diễn đạt khác hoặc nhấn mạnh khía cạnh khác
- Ngắn gọn, rõ ràng, mỗi câu trên một dòng

Câu hỏi gốc: "{query}" 
"""
    output = call_qwen_api(query_rewrite_prompt)

    if not output:
        return [query]

    questions = [q.strip("-•* \n") for q in output.split("\n") if q.strip()]
    return [query] + questions[:k]

# Tạo prompt
def prompt_text(context, question):
    return f"""
Bạn là một trợ lý AI thông minh. Hãy ưu tiên trả lời dựa vào thông tin sau nếu có:
{context}

Nếu không đủ thông tin, bạn có thể sử dụng kiến thức của mình để đưa ra câu trả lời chính xác nhất.

Câu hỏi: {question}
Trả lời:
""".strip()

# Hàm chính giải toán
def solve_question_api(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True):
    try:
        # Tạo queries
        if rewrite:
            queries = rewrite_query(question, 3)
            queries.append(question)
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
            return answer, []

        # Gọi API
        answer = call_qwen_api(prompt_text(context, question))

        # Xử lý lặp lại
        if question in answer:
            answer = answer.split(question)[-1].strip(": \n")

        # Nếu rỗng, gọi lại
        if not answer.strip():
            fallback_prompt = f"Câu hỏi: {question}\nTrả lời ngắn gọn:"
            answer = call_qwen_api(fallback_prompt)

        source_docs = [{"page_content": split_combined_content(doc.page_content), "metadata": doc.metadata} for doc in docs]
        return answer, source_docs

    except Exception as e:
        return f"Lỗi trong quá trình xử lý: {str(e)}", []