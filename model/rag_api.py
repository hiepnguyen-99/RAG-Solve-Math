import os
import torch
import requests
from transformers import pipeline
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# Nếu có FlagEmbedding để rerank
try:
    from FlagEmbedding import FlagReranker
    RERANK_AVAILABLE = True
except ImportError:
    print("⚠️ FlagEmbedding không có, bỏ qua reranking.")
    RERANK_AVAILABLE = False
    FlagReranker = None

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

# Gọi API mô hình
def call_qwen_api(prompt: str):
    api_url = os.environ.get("API_URL", "https://api.together.xyz")
    api_key = os.environ.get("TOGETHER_API_KEY")

    if not api_key:
        return "❌ Không có TOGETHER_API_KEY trong biến môi trường"

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

    try:
        response = requests.post(f"{api_url}/v1/chat/completions", headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()["choices"][0]["text"].strip()
        return f"❌ Lỗi API: {response.text}"
    except Exception as e:
        return f"❌ Lỗi kết nối API: {e}"

# Prompt Template
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
Bạn là một trợ lý AI thông minh, chỉ trả lời câu hỏi dựa trên thông tin đã cho:
{context}
Dựa vào thông tin trên, hãy trả lời câu hỏi sau một cách chính xác:
Câu hỏi: {question}
Trả lời:
"""
)

# Rerank nếu có
def rerank_docs_with_model(query, docs, reranker, metadata_fields=["title", "section", "subsection"]):
    if not RERANK_AVAILABLE:
        return docs

    pairs = []
    for doc in docs:
        content_parts = [doc.metadata.get(field, "") for field in metadata_fields]
        content_for_rerank = " - ".join(part for part in content_parts if part)
        if not content_for_rerank:
            content_for_rerank = doc.page_content[:200]
        pairs.append((query, content_for_rerank))

    scores = reranker.compute_score(pairs)
    ranked_docs = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in ranked_docs]

# Hàm chính giải toán qua API
def solve_question_api(question: str, k: int = 3, rerank: bool = False):
    retriever = db.as_retriever(search_kwargs={"k": k})
    docs = retriever.get_relevant_documents(question)

    # Rerank nếu bật
    if rerank and docs and RERANK_AVAILABLE:
        try:
            reranker = FlagReranker(RERANK_MODEL, use_fp16=True)
            docs = rerank_docs_with_model(question, docs, reranker)
            print(f"✅ Đã rerank {len(docs)} tài liệu")
        except Exception as e:
            print(f"⚠️ Lỗi rerank: {e}, tiếp tục không rerank.")
    elif rerank and not RERANK_AVAILABLE:
        print("⚠️ Yêu cầu rerank nhưng không có FlagEmbedding")

    # Tạo prompt
    context = "\n".join([doc.page_content for doc in docs])
    prompt_text = prompt_template.format(context=context, question=question)

    # Gọi API
    answer = call_qwen_api(prompt_text)

    # Xử lý lại nếu có lặp lại câu hỏi trong câu trả lời
    if question in answer:
        answer = answer.split(question)[-1].strip(": \n")

    # Nếu vẫn rỗng, thử lại
    if not answer.strip():
        fallback_prompt = f"Câu hỏi: {question}\nTrả lời ngắn gọn:"
        answer = call_qwen_api(fallback_prompt)

    source_docs = [{"page_content": doc.page_content, "metadata": doc.metadata} for doc in docs]
    return answer, source_docs