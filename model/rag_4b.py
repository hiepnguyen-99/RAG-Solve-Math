import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFacePipeline

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

def rerank_docs_with_model(query, docs, reranker, metadata_fields=["title", "section", "subsection"]):
    """
    Rerank documents using a reranker model
    """
    if not RERANK_AVAILABLE:
        print("Reranking not available, returning original order")
        return docs
        
    pairs = []
    for doc in docs:
        # Combine multiple metadata fields
        content_parts = [doc.metadata.get(field, "") for field in metadata_fields]
        content_for_rerank = " - ".join(part for part in content_parts if part)
        
        # If no metadata, use part of page content
        if not content_for_rerank:
            content_for_rerank = doc.page_content[:200]  # First 200 chars
            
        pairs.append((query, content_for_rerank))

    # Get scores from reranker
    scores = reranker.compute_score(pairs)

    # Sort documents by scores
    scored_docs = list(zip(docs, scores))
    ranked_docs = sorted(scored_docs, key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in ranked_docs]

def call_qwen_4b(prompt: str, ngrok_url: str):
    response = requests.post(f"{ngrok_url}/generate", json={"prompt": prompt})
    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return f"Lỗi: {response.text}"

from langchain.prompts import PromptTemplate

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

def solve_question_4b(question: str, k: int = 3, ngrok_url: str = "https://7df30a3ef6e2.ngrok-free.app", rerank: bool = False):
    # Tìm kiếm tài liệu liên quan
    custom_retriever = db.as_retriever(search_kwargs={"k": k})
    docs = custom_retriever.get_relevant_documents(question)

    # Apply reranking if enabled
    if rerank and docs and RERANK_AVAILABLE:
        try:
            reranker = FlagReranker(RERANK_MODEL, use_fp16=True)
            docs = rerank_docs_with_model(question, docs, reranker)
            print(f"Reranking applied to {len(docs)} documents")
        except Exception as e:
            print(f"Reranking failed: {e}, continuing without reranking...")
    elif rerank and not RERANK_AVAILABLE:
        print("Reranking requested but FlagEmbedding not available")

    # Lấy nội dung các tài liệu
    context = "\n".join([doc.page_content for doc in docs])

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

    # Trả kết quả kèm tài liệu nguồn
    source_docs = [{
        "page_content": doc.page_content,
        "metadata": doc.metadata
    } for doc in docs]

    return answer, source_docs
