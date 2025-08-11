import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_huggingface import HuggingFacePipeline
from rag_utils import *

# Thiết bị
device = "cuda" if torch.cuda.is_available() else "cpu"

# Sử dụng các utility functions
embedding_model = get_embedding_model()
db = get_chroma_db()

# Load LLM
model_name = "Qwen/Qwen2-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, torch_dtype=torch.float16
).to(device)

# Pipeline tối ưu
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

def rewrite_query_15b(query, k=5):
    """Rewrite query sử dụng Qwen 1.5B"""
    prompt = REWRITE_QUERY_PROMPT_TEMPLATE.format(query=query, k=k)
    response = llm.invoke(prompt).strip()
    return clean_rewrite_queries(response.split('\n') if response else [query], query, k)

def solve_question_15b(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True, conversation_history: list = None):
    """
    Giải câu hỏi với hỗ trợ conversation context sử dụng Qwen 1.5B
    """
    try:
        # Xây dựng conversation context sử dụng utility function
        conversation_context = build_conversation_context(conversation_history, question)
        
        # Tạo queries với rewrite
        if rewrite:
            enhanced_question = enhance_question_with_context(question, conversation_history)
            queries = rewrite_query_15b(enhanced_question, 3)
            queries.append(question)  # Thêm câu hỏi gốc
        else:
            queries = [question]

        # Xử lý documents sử dụng utility function
        docs = process_retrieved_docs(queries, db, k, rerank)
        
        # Tạo context
        context = create_context_from_docs(docs)

        if not context:
            answer = handle_empty_context(question, llm.invoke)
            return answer, [], []

        # Tạo prompt sử dụng utility function
        prompt = create_base_prompt_template(context, question, conversation_context, "concise")
        
        # Gọi model
        answer = llm.invoke(prompt)

        # Làm sạch câu trả lời
        answer = clean_answer_response(answer, question)

        # Nếu không có câu trả lời rõ ràng, fallback
        if not answer.strip():
            answer = handle_empty_context(question, llm.invoke)

        # Tạo source documents và rewrite queries
        source_docs = create_source_documents(docs)
        rewrite_queries = extract_rewrite_queries(queries, include_original=False)

        return answer, source_docs, rewrite_queries

    except Exception as e:
        return f"Lỗi khi xử lý câu hỏi với Qwen 1.5B: {str(e)}", [], []


def solve_math_question_15b(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True, conversation_history: list = None):
    """
    Giải toán chi tiết từng bước, sử dụng LaTeX cho công thức.
    """
    try:
        # Xây dựng conversation context
        conversation_context = build_conversation_context(conversation_history, question)
        
        # Tạo queries với rewrite
        if rewrite:
            enhanced_question = enhance_question_with_context(question, conversation_history)
            queries = rewrite_query_15b(enhanced_question, 3)
            queries.append(question)
        else:
            queries = [question]

        # Xử lý documents
        docs = process_retrieved_docs(queries, db, k, rerank)
        
        # Tạo context
        context = create_context_from_docs(docs)

        if not context:
            answer = handle_empty_context(question, llm.invoke)
            return answer, [], []

        # Tạo prompt cho math mode
        prompt = create_base_prompt_template(context, question, conversation_context, "math")
        prompt += "\n1. Phân tích.\n2. Giải chi tiết.\n3. Kết luận."
        
        # Gọi model
        answer = llm.invoke(prompt)

        # Làm sạch câu trả lời
        answer = clean_answer_response(answer, question)

        if not answer.strip():
            answer = handle_empty_context(question, llm.invoke)

        # Tạo source documents và rewrite queries
        source_docs = create_source_documents(docs)
        rewrite_queries = extract_rewrite_queries(queries, include_original=False)

        return answer, source_docs, rewrite_queries

    except Exception as e:
        return f"Lỗi khi xử lý câu hỏi toán với Qwen 1.5B: {str(e)}", [], []
