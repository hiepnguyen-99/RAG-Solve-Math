import os
import torch
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate as MathPromptTemplate
from groq import Groq

from retrieval import *
from conversation_manager import conversation_manager
from function import *

# ==== Thiết bị ====
device = "cuda" if torch.cuda.is_available() else "cpu"

# ==== DB & Embedding ====
embedding_model = get_embedding_model()
db = get_chroma_db()

# ==== Rerank ====
RERANK_MODEL = "BAAI/bge-reranker-base"
try:
    from FlagEmbedding import FlagReranker
    RERANK_AVAILABLE = True
except ImportError:
    print("⚠️ FlagEmbedding không có, bỏ qua reranking.")
    RERANK_AVAILABLE = False
    FlagReranker = None

# ==== Groq API ====
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    print("⚠️ GROQ_API_KEY không được cấu hình")
client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

# ==== Rewrite query ====
def rewrite_query_groq(query, k=5):
    """
    Viết lại câu query bằng Groq LLaMA 3 8B.
    """
    if not client:
        print("⚠️ Groq API không khả dụng, trả về query gốc")
        return [query]

    rewrite_prompt = f"""
    Từ truy vấn:
    "{query}"
    Hãy tạo {k} truy vấn khác nhau bằng tiếng Việt.
    """

    try:
        resp = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": rewrite_prompt}],
            temperature=0.4,
            max_tokens=256
        )
        text = resp.choices[0].message.content
        return [line.strip("-• ") for line in text.strip().split("\n") if line.strip()]
    except Exception as e:
        print(f"⚠️ Lỗi khi rewrite query: {e}")
        return [query]

# ==== Prompt thường ====
def promt_text(context, question, conversation_context=""):
    return f"""
Dựa trên thông tin sau, hãy trả lời câu hỏi.
Yêu cầu:
- Nếu có công thức toán học, đặt trong khối LaTeX `$$`.
- Không cần nói "Dựa trên thông tin được cung cấp".
- Mỗi ý xuống dòng riêng.

{conversation_context}

Thông tin:
{context}

Câu hỏi: {question}
Trả lời:
""".strip()

# ==== Template toán ====
math_template = MathPromptTemplate(
    input_variables=["context", "question", "conversation_context"],
    template="""
Bạn là trợ lý AI chuyên giải các bài toán. 

{conversation_context}

Dựa vào thông tin sau:
{context}
Hãy giải bài toán sau từng bước một, hiển thị công thức trong khối LaTeX `$$`.
Câu hỏi: {question}
1. Phân tích.
2. Giải chi tiết.
3. Kết luận.
"""
)

# ==== Hàm chính ====
def solve_question_api_groq(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True, math: bool = False, conversation_history: list = None):
    """
    Hàm giải câu hỏi qua Groq API LLaMA3.
    """
    try:
        if not client:
            return "Lỗi: GROQ_API_KEY không được cấu hình.", [], []

        # Context hội thoại
        conversation_context = ""
        if conversation_history and conversation_manager.should_use_context(question, conversation_history):
            conversation_context = conversation_manager.build_conversation_context(conversation_history, question)
            print(f"🔄 Sử dụng conversation context: {len(conversation_context)} ký tự")

        # Rewrite query
        if rewrite:
            if conversation_context:
                topics = conversation_manager.extract_key_topics(conversation_history)
                enhanced_question = f"{question} (Liên quan: {', '.join(topics)})" if topics else question
                queries = rewrite_query_groq(enhanced_question, 3)
            else:
                queries = rewrite_query_groq(question, 3)
            queries.append(question)
        else:
            queries = [question]

        # Retrieve docs
        docs = []
        for query in queries:
            retriever = db.as_retriever(search_kwargs={"k": k})
            doc = retriever.get_relevant_documents(query)
            if rerank and RERANK_AVAILABLE:
                try:
                    reranker = FlagReranker(RERANK_MODEL, use_fp16=True)
                    doc = rerank_docs_with_model(query, doc, reranker, num_doc=k)
                except Exception as e:
                    print(f"Lỗi khi rerank: {e}")
            docs.append(doc)

        docs = reciprocal_rank_fusion(docs, num_docs=k)
        context = "\n".join([split_combined_content(doc.page_content) for doc in docs]) if docs else "Không tìm thấy tài liệu liên quan."

        # Prompt
        if math:
            prompt = math_template.format(context=context, question=question, conversation_context=conversation_context)
        else:
            prompt = promt_text(context, question, conversation_context)

        # Gọi Groq API
        resp = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=512
        )

        answer = resp.choices[0].message.content

        # Tạo source docs
        source_docs = [{"page_content": split_combined_content(doc.page_content), "metadata": doc.metadata} for doc in docs]

        # Rewrite queries (bỏ câu gốc)
        rewrite_queries = queries[:-1] if rewrite else []

        return answer.strip(), source_docs, rewrite_queries

    except Exception as e:
        return f"Lỗi khi xử lý Groq API: {str(e)}", [], []

# ==== Alias cho toán ====
def solve_math_question_api_groq(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True, conversation_history: list = None):
    return solve_question_api_groq(question, k=k, rerank=rerank, rewrite=rewrite, math=True, conversation_history=conversation_history)
