import torch
import re
from .function import *
from dotenv import load_dotenv
from .conversation_manager import conversation_manager
from groq import Groq
from langchain.prompts import PromptTemplate as MathPromptTemplate

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

# ==== Instructions & Styles ====
MATH_STRICT_INSTRUCTION = """
    Bạn là một trợ lý toán học, chuyên giải quyết các bài toán và câu hỏi của người dùng. 
    Khi trình bày bạn phải
      + mỗi công thức, Tiêu đề,... phải ở trên một dòng riêng.
      + Không dùng inline LaTeX.
      + Ngắn gọn, chỉ giữ bước quan trọng, không văn hoa.
"""

STYLES = {
    # Phong cách mặc định cho các bài toán (đúng yêu cầu người dùng)
    "bai_toan": MATH_STRICT_INSTRUCTION
}

# ==== Rewrite query ====
def rewrite_query_groq(query, k=5, conversation_history=None):
    """
    Rewrite query sử dụng context hội thoại (multi-turn) - sử dụng Gemma 7B
    """
    if not client:
        print("⚠️ Groq API không khả dụng, trả về query gốc")
        return [query]

    # Xây dựng context hội thoại nếu có
    history_text = ""
    if conversation_history:
        for turn in conversation_history:
            user = turn.get("user", "")
            model = turn.get("model", "")
            history_text += f"User: {user}\nModel: {model}\n"

    query_rewrite_prompt = (
        f"Dựa vào lịch sử hội thoại sau (nếu có):\n{history_text}\n"
        f"Từ câu hỏi: '{query}'\n"
        f"Tạo {k} câu hỏi TÌM KIẾM khác nhau, mỗi câu tập trung vào khía cạnh riêng:\n"
        f"- Câu 1: Tìm định nghĩa/khái niệm\n"
        f"- Câu 2: Tìm công thức/phương pháp\n"
        f"- Câu 3: Tìm ví dụ/bài tập\n"
        f"Chỉ viết {k} câu hỏi, mỗi câu một dòng, không đánh số:\n"
    )

    try:
        resp = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[{"role": "user", "content": query_rewrite_prompt}],
            temperature=0.7,  # Tăng từ 0.4 lên 0.7 để đa dạng hơn
            max_tokens=256
        )
        
        response = resp.choices[0].message.content

        if response and not response.startswith("Lỗi:"):
            # Tách các dòng và làm sạch
            lines = response.split('\n')
            queries = []
            seen_queries = set()  # Để tránh trùng lặp

            for line in lines:
                line = line.strip()
                if not line:
                    continue

                # Bỏ qua các dòng không phải câu hỏi (tiếng Anh, số thứ tự, etc.)
                if any(word.lower() in line.lower() for word in ['okay', 'let\'s', 'first', 'user', 'think', 'wait', 'the']):
                    continue

                # Loại bỏ số thứ tự ở đầu dòng (1., 2., -, •, etc.)
                line = re.sub(r'^\d+\.?\s*', '', line)  # Loại bỏ "1. " hoặc "1 "
                line = re.sub(r'^[-•*]\s*', '', line)   # Loại bỏ "- " hoặc "• "
                line = line.strip()

                # Kiểm tra trùng lặp và điều kiện khác
                if (line and len(line) > 10 and 
                    not line.lower().startswith(('vui lòng', 'okay', 'first')) and
                    line.lower() not in seen_queries and
                    line != query):  # Không trùng với câu gốc
                    
                    queries.append(line)
                    seen_queries.add(line.lower())

            # Giới hạn số lượng câu hỏi theo k
            queries = queries[:k] if len(queries) > k else queries
            
            print(f"🔍 Generated {len(queries)} unique rewrite queries")
            for i, q in enumerate(queries, 1):
                print(f"   {i}. {q}")
                
            return queries if queries else [query]
        else:
            print(f"Rewrite failed: {response}")
            return [query]
            
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
    template=f"""
{STYLES["bai_toan"]}

{{conversation_context}}

Dựa vào thông tin sau:
{{context}}
Hãy giải bài toán sau từng bước một, hiển thị công thức trong khối LaTeX `$$`.
Câu hỏi: {{question}}
1. Phân tích.
2. Giải chi tiết.
3. Kết luận.
"""
)

# ==== Hàm chính ====
def classify_question_groq(question: str) -> str:
    """
    Phân loại câu hỏi bằng Groq Mixtral 8x7B model
    """
    if not client:
        return None
        
    classification_prompt = f"""
Phân loại câu hỏi sau đây thuộc loại nào:

LOẠI 1 - "SOLVING": Câu hỏi yêu cầu GIẢI TOÁN CỤ THỂ, tính toán, tìm nghiệm, chứng minh với dữ liệu cụ thể
- Có số liệu, biểu thức, phương trình cụ thể cần giải
- Yêu cầu tính toán, tìm kết quả số
- Ví dụ: "Tính đạo hàm của f(x)=x²", "Giải phương trình x²-5x+6=0"

LOẠI 2 - "KNOWLEDGE": Câu hỏi yêu cầu GIẢI THÍCH LÝ THUYẾT, định nghĩa, phương pháp, khái niệm
- Hỏi về cách làm, phương pháp, định nghĩa, lý thuyết
- Yêu cầu ví dụ, giải thích khái niệm
- Ví dụ: "Định nghĩa đạo hàm là gì?", "Cách tính định thức của ma trận"

Câu hỏi: "{question}"

Trả lời CHÍNH XÁC một trong hai từ: SOLVING hoặc KNOWLEDGE
"""
    
    try:
        resp = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[{"role": "user", "content": classification_prompt}],
            temperature=0.1,
            max_tokens=10
        )
        
        result = resp.choices[0].message.content.strip().upper()
        
        if "SOLVING" in result:
            return 'math_solving'
        elif "KNOWLEDGE" in result:
            return 'knowledge_retrieval'
        else:
            return None
    except Exception as e:
        print(f"⚠️ Lỗi phân loại Groq: {e}")
        return None


def solve_question_api_groq(question: str, k: int = 3, rerank: bool = False, rewrite: bool = True, math: bool = False, conversation_history: list = None):
    """
    Hàm giải câu hỏi qua Groq API Mixtral 8x7B.
    Tự động phân loại câu hỏi để quyết định dùng RAG hay giải toán trực tiếp.
    """
    try:
        if not client:
            return "Lỗi: GROQ_API_KEY không được cấu hình.", [], []

        # Phân loại câu hỏi bằng chính Groq LLaMA3 model
        question_type = classify_question_type_generic(question, classify_question_groq)
        print(f"🔍 Loại câu hỏi được phân loại bởi LLaMA3: {question_type}")

        # Context hội thoại
        conversation_context = ""
        if conversation_history and conversation_manager.should_use_context(question, conversation_history):
            conversation_context = conversation_manager.build_conversation_context(conversation_history, question)
            print(f"🔄 Sử dụng conversation context: {len(conversation_context)} ký tự")

        if question_type == 'math_solving':
            # Giải toán trực tiếp - không cần retrieval
            print("⚡ Chế độ giải toán trực tiếp (không dùng RAG)")
            return solve_math_direct_groq(question, conversation_history)
        else:
            # Dùng RAG để tìm kiếm tài liệu
            print("📚 Chế độ tìm kiếm tài liệu (dùng RAG)")

            # Rewrite query
            if rewrite:
                if conversation_context:
                    topics = conversation_manager.extract_key_topics(conversation_history)
                    enhanced_question = f"{question} (Liên quan: {', '.join(topics)})" if topics else question
                    queries = rewrite_query_groq(enhanced_question, 3, conversation_history)  # Dùng k=3 như 4b
                else:
                    queries = rewrite_query_groq(question, 3, conversation_history)  # Dùng k=3 như 4b
                queries.append(question)  # Tổng cộng 4 câu (3 mới + 1 gốc)
            else:
                queries = [question]

            # Retrieve docs
            docs = []
            for query in queries:
                retriever = db.as_retriever(search_kwargs={"k": k})
                doc = retriever.invoke(query)
                if rerank and RERANK_AVAILABLE:
                    try:
                        reranker = FlagReranker(RERANK_MODEL, use_fp16=True)
                        doc = rerank_docs_with_model(query, doc, reranker, num_doc=k)
                    except Exception as e:
                        print(f"Lỗi khi rerank: {e}")
                docs.append(doc)

            docs = reciprocal_rank_fusion(docs, num_docs=k)
            context = "\n".join([split_combined_content(doc.page_content) for doc in docs]) if docs else "Không tìm thấy tài liệu liên quan."

            # Prompt và gọi API
            if math:
                # Sử dụng system message cho math
                user_content = f"""
{conversation_context}

Dựa vào thông tin sau:
{context}
Hãy giải bài toán sau từng bước một, hiển thị công thức trong khối LaTeX `$$`.
Câu hỏi: {question}
1. Phân tích.
2. Giải chi tiết.
3. Kết luận.
"""
                messages = [
                    {"role": "system", "content": STYLES["bai_toan"]},
                    {"role": "user", "content": user_content}
                ]
            else:
                prompt = promt_text(context, question, conversation_context)
                messages = [{"role": "user", "content": prompt}]

            # Gọi Groq API
            resp = client.chat.completions.create(
                model="gemma2-9b-it",
                messages=messages,
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


# Hàm giải toán không dùng retrieval - chỉ dùng model trực tiếp
def solve_math_direct_groq(question: str, conversation_history: list = None):
    """
    Giải toán trực tiếp bằng Groq API không cần retrieval documents
    
    Args:
        question: Câu hỏi toán học
        conversation_history: Lịch sử trò chuyện
    """
    try:
        if not client:
            return "Lỗi: GROQ_API_KEY không được cấu hình.", [], []

        # Context hội thoại
        conversation_context = ""
        if conversation_history and conversation_manager.should_use_context(question, conversation_history):
            conversation_context = conversation_manager.build_conversation_context(conversation_history, question)
            print(f"🔄 Sử dụng conversation context: {len(conversation_context)} ký tự")

        # Tạo messages với system instruction
        messages = [
            {"role": "system", "content": STYLES["bai_toan"]},
            {"role": "user", "content": f"""
{conversation_context}

Hãy giải bài toán sau đây từng bước một, hiển thị các công thức trong khối LaTeX (đặt giữa $$):

Câu hỏi: {question}

Hãy làm theo các bước:
1. Phân tích đề bài và xác định phương pháp giải
2. Giải chi tiết từng bước với các công thức toán học
3. Đưa ra kết luận cuối cùng
"""}
        ]

        # Gọi Groq API
        resp = client.chat.completions.create(
            model="gemma2-9b-it",
            messages=messages,
            temperature=0.3,
            max_tokens=1024
        )

        answer = resp.choices[0].message.content

        # Trả về với source_docs và rewrite_queries rỗng vì không dùng retrieval
        return answer.strip(), [], []

    except Exception as e:
        return f"Lỗi khi xử lý Groq API: {str(e)}", [], []
