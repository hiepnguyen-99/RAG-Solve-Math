import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline

# 1. Thiết bị
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Đang sử dụng thiết bị:", device)

# 2. Mô hình embedding
embedding_model = HuggingFaceEmbeddings(
    model_name="Qwen/Qwen3-Embedding-0.6B",
    model_kwargs={"device": device},
    encode_kwargs={"normalize_embeddings": True}
)

# 3. Load Chroma DB
chroma_path = "./chroma_db"
db = Chroma(persist_directory=chroma_path, embedding_function=embedding_model, collection_name="math_vectors"  # thêm dòng này!
)
retriever = db.as_retriever(search_kwargs={"k": 3})
print("Số lượng tài liệu trong Chroma:", db._collection.count())
print(f"Loading Chroma from: {chroma_path}")

# 4. Tải mô hình ngôn ngữ (LLM)
model_name = "Qwen/Qwen2-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, torch_dtype=torch.float16
).to(device)

# 5. Tạo pipeline sinh văn bản
generation_pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=300,
    temperature=0.7,
    top_p=0.9,
    do_sample=False,
    device=0 if device == "cuda" else -1,
    framework="pt"
)
llm = HuggingFacePipeline(pipeline=generation_pipe)

# 6. Prompt template cập nhật
prompt_template = PromptTemplate.from_template(
"""Bạn là trợ lý Toán học. Hãy trả lời ngắn gọn và chính xác nhất từ các thông tin sau."
Thông tin truy hồi:
---------------------
{context}
---------------------
Trả lời:"""
)

# 7. Tạo Retrieval-QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt_template},
    return_source_documents=True
)

# 8. Vòng lặp hỏi-đáp
print("=== Hệ thống truy vấn Toán học ===")
print("Nhập 'exit' để thoát.")
print("----------------------------------------")

while True:
    question = input("Câu hỏi của bạn: ").strip()
    if question.lower() == "exit":
        break

    result = qa_chain.invoke({"query": question})
    answer = result["result"].strip()

    # In các tài liệu đã truy hồi
    if result["source_documents"]:
        print("\n📚 Truy hồi các tài liệu:")
        for doc in result["source_documents"]:
            print(f"\n---\n{doc.page_content}\n---")
    else:
        print("\n⚠️ Không tìm thấy tài liệu liên quan trong Chroma.")

    # Nếu không có trả lời hoặc không có tài liệu → fallback
    if not result["source_documents"] or answer == "":
        fallback_prompt = f"Câu hỏi: {question}\nTrả lời ngắn gọn:"
        answer = llm.invoke(fallback_prompt).strip()

    print("\n➡️ Câu trả lời:", answer)
    print("----------------------------------------")
