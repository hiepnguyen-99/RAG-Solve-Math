import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
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
model_name = "Qwen/Qwen2-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, torch_dtype=torch.float16
).to(device)

# Configuration
RERANK_MODEL = "BAAI/bge-reranker-base"


# 5. Pipeline tối ưu
generation_pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=300,
    temperature=0.6,
    top_p=0.9,
    do_sample=False,
    return_full_text=False,
    device=device
)
llm = HuggingFacePipeline(pipeline=generation_pipe)

# 6. Prompt rút gọn
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template=(
        "Dựa trên thông tin sau, hãy trả lời ngắn gọn, đúng trọng tâm câu hỏi, chỉ sử dụng tài liệu liên quan đến câu hỏi nhất để trả lời, tài liệu không liên quan vui lòng bỏ qua, chỉ trả lời 1 lần không cần tóm lại và không lặp lại câu hỏi:\n"
        "{context}\n"
        "Câu hỏi: {question}\n"
        "Trả lời:"
    )
)

# 8. Hàm giải đáp
def solve_question_15b(question: str, k: int = 3, rerank: bool = False):
    # Tạo retriever mới với k tài liệu gần nhất
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

    temp_qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=custom_retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt_template},
        return_source_documents=True
    )

    result = temp_qa_chain.invoke({"query": question})
    answer = result["result"].strip()

    # Xử lý lặp lại prompt trong câu trả lời
    if question in answer:
        answer = answer.split(question)[-1].strip(": \n")

    # Use reranked docs if available, otherwise use original
    source_docs = docs if rerank else result.get("source_documents", [])
    
    docs = [
    {
        "page_content": doc.metadata.get("original_content"),
        "metadata": doc.metadata
    }
    for doc in source_docs
]
    # fallback nếu không có kết quả
    if not answer:
        fallback_prompt = f"Câu hỏi: {question}\nTrả lời ngắn gọn:"
        raw_output = llm.invoke(fallback_prompt).strip()
        if question in raw_output:
            answer = raw_output.split(question)[-1].strip(": \n")
        else:
            answer = raw_output.strip()

    return answer, docs
