import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFacePipeline

# 1. Thiết bị
device = "cuda" if torch.cuda.is_available() else "cpu"

# 2. Mô hình embedding
embedding_model = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-base",
    model_kwargs={"device": device}
)

# 3. Load Chroma
chroma_path = "./chroma_db"
db = Chroma(
    persist_directory=chroma_path,
    embedding_function=embedding_model,
    collection_name="math_vectors"
)
retriever = db.as_retriever(search_kwargs={"k": 3})

# 4. Load LLM
model_name = "Qwen/Qwen2-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, torch_dtype=torch.float16
).to(device)

# 5. Pipeline tối ưu
generation_pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200,
    temperature=0.6,
    top_p=0.9,
    do_sample=False,
    return_full_text=False,
    device=0 if device == "cuda" else -1
)
llm = HuggingFacePipeline(pipeline=generation_pipe)

# 6. Prompt rút gọn
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template=(
        "Dựa trên thông tin sau, hãy trả lời ngắn gọn và không lặp lại câu hỏi:\n"
        "{context}\n"
        "Câu hỏi: {question}\n"
        "Trả lời:"
    )
)

# 7. Tạo QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt_template},
    return_source_documents=True
)

# 8. Hàm giải đáp
def solve_question(question: str):
    result = qa_chain.invoke({"query": question})
    answer = result["result"].strip()

    # Xử lý lặp lại prompt
    if question in answer:
        answer = answer.split(question)[-1].strip(": \n")

    docs = [doc.page_content for doc in result.get("source_documents", [])]

    # fallback nếu không có kết quả
    if not answer:
        fallback_prompt = f"Câu hỏi: {question}\nTrả lời ngắn gọn:"
        raw_output = llm.invoke(fallback_prompt).strip()
        if question in raw_output:
            answer = raw_output.split(question)[-1].strip(": \n")
        else:
            answer = raw_output.strip()

    return answer, docs
