import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_huggingface import HuggingFacePipeline
from function import *
from conversation_manager import conversation_manager


# Thiết bị
device = "cuda" if torch.cuda.is_available() else "cpu"

# Sử dụng các utility functions
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

# 6. Prompt rút gọn với conversation context
prompt_template = PromptTemplate(
    input_variables=["context", "question", "conversation_context"],
    template=(
        "{conversation_context}\n\n"
        "Dựa trên thông tin sau, hãy trả lời ngắn gọn, đúng trọng tâm câu hỏi, chỉ sử dụng tài liệu liên quan đến câu hỏi nhất để trả lời, tài liệu không liên quan vui lòng bỏ qua, chỉ trả lời 1 lần không cần tóm lại và không lặp lại câu hỏi:\n"
        "{context}\n"
        "Câu hỏi: {question}\n"
        "Trả lời:"
    )
)

def rewrite_query_15b(query, k=5):
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
    response = llm.invoke(query_rewrite_prompt).strip()
    return response.split('\n') if response else [query]

# 8. Hàm giải đáp với conversation context
def solve_question_15b(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True, conversation_history: list = None):
    """
    Giải câu hỏi với hỗ trợ conversation context
    
    Args:
        question: Câu hỏi hiện tại
        k: Số lượng tài liệu retrieve
        rerank: Có sử dụng reranking không
        rewrite: Có rewrite query không
        conversation_history: Lịch sử trò chuyện (danh sách messages)
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
            queries = rewrite_query_15b(enhanced_question, 3)
        else:
            queries = rewrite_query_15b(question, 3)
        queries.append(question)  # Thêm câu hỏi gốc vào cuối
    else:
        queries = [question]

    # Collect documents từ tất cả queries
    docs = []
    for query in queries:
        custom_retriever = db.as_retriever(search_kwargs={"k": k})
        doc = custom_retriever.get_relevant_documents(query)
        
        # Apply reranking if enabled
        if rerank and doc and RERANK_AVAILABLE:
            try:
                reranker = FlagReranker(RERANK_MODEL, use_fp16=True)
                doc = rerank_docs_with_model(query, doc, reranker)
                print(f"Reranking applied to {len(doc)} documents")
            except Exception as e:
                print(f"Reranking failed: {e}, continuing without reranking...")
        elif rerank and not RERANK_AVAILABLE:
            print("Reranking requested but FlagEmbedding not available")
        
        docs.extend([doc])

    # Sử dụng reciprocal rank fusion để kết hợp kết quả
    docs = reciprocal_rank_fusion(docs, num_docs=k)

    # Tạo prompt với conversation context
    context = "\n".join([split_combined_content(doc.page_content) for doc in docs])
    prompt_text = prompt_template.format(
        context=context, 
        question=question, 
        conversation_context=conversation_context
    )
    
    # Gọi model
    answer = llm.invoke(prompt_text).strip()

    # Xử lý lặp lại prompt trong câu trả lời
    if question in answer:
        answer = answer.split(question)[-1].strip(": \n")

    # fallback nếu không có kết quả
    if not answer:
        fallback_prompt = f"Câu hỏi: {question}\nTrả lời ngắn gọn:"
        raw_output = llm.invoke(fallback_prompt).strip()
        if question in raw_output:
            answer = raw_output.split(question)[-1].strip(": \n")
        else:
            answer = raw_output.strip()

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

# Thêm hàm giải toán chuyên biệt cho Qwen 1.5B với LaTeX
from langchain.prompts import PromptTemplate as MathPromptTemplate

def solve_math_question_15b(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True, conversation_history: list = None):
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
            queries = rewrite_query_15b(enhanced_question, 3)
        else:
            queries = rewrite_query_15b(question, 3)
        queries.append(question)  # Thêm câu hỏi gốc vào cuối
    else:
        queries = [question]

    # Collect documents từ tất cả queries
    docs = []
    for query in queries:
        custom_retriever = db.as_retriever(search_kwargs={"k": k})
        doc = custom_retriever.get_relevant_documents(query)
        
        if rerank and RERANK_AVAILABLE:
            try:
                reranker = FlagReranker(RERANK_MODEL, use_fp16=True)
                doc = rerank_docs_with_model(query, doc, reranker)
            except Exception:
                pass
        
        docs.extend([doc])

    # Sử dụng reciprocal rank fusion để kết hợp kết quả
    docs = reciprocal_rank_fusion(docs, num_docs=k)
    
    context = "\n".join([split_combined_content(doc.page_content) for doc in docs])
    math_template = MathPromptTemplate(
        input_variables=["context", "question", "conversation_context"],
        template=(
            "Bạn là trợ lý AI chuyên giải toán.\n\n"
            "{conversation_context}\n\n"
            "Dựa vào thông tin:\n{context}\n"
            "Giải từng bước rõ ràng, biểu diễn công thức trong LaTeX (đặt giữa $$).\n"
            "Câu hỏi: {question}\n"
            "Trả lời:\n1. Phân tích.\n2. Giải chi tiết.\n3. Kết luận."
        )
    )
    prompt_text = math_template.format(
        context=context, 
        question=question, 
        conversation_context=conversation_context
    )
    result = llm.invoke(prompt_text).strip()
    answer = result
    
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
