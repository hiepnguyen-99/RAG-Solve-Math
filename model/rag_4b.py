import torch
from function import *
from dotenv import load_dotenv
import requests
from conversation_manager import conversation_manager
from langchain.prompts import PromptTemplate
import sys
sys.stdout.reconfigure(encoding="utf-8")

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

load_dotenv()
NGROK_URL = os.getenv("NGROK_URL")


def call_qwen_4b(prompt: str, ngrok_url: str):
    if not ngrok_url:
        return "Lỗi: NGROK_URL không được cấu hình"
    
    try:
        response = requests.post(f"{ngrok_url}/generate", json={"prompt": prompt})
        if response.status_code == 200:
            return response.json()["response"].strip()
        else:
            return f"Lỗi HTTP {response.status_code}: {response.text}"
    except requests.exceptions.ConnectionError:
        return f"Lỗi: Không thể kết nối đến server {ngrok_url}"
    except requests.exceptions.Timeout:
        return "Lỗi: Timeout khi kết nối đến server"
    except Exception as e:
        return f"Lỗi: {str(e)}"

def rewrite_query_4b(query, k=5, conversation_history=None):
    """
    Rewrite query sử dụng context hội thoại (multi-turn)
    """
    # Xây dựng context hội thoại nếu có
    history_text = ""
    if conversation_history:
        for turn in conversation_history:
            user = turn.get("user", "")
            model = turn.get("model", "")
            history_text += f"User: {user}\nModel: {model}\n"

    query_rewrite_prompt = (
        f"Dựa vào lịch sử hội thoại sau (nếu có):\n{history_text}\n"
        f"Tạo {k} câu hỏi ngắn, đa dạng để tìm kiếm thông tin trả lời cho câu hỏi cuối cùng: '{query}'\n"
        f"Chỉ liệt kê {k} câu hỏi, mỗi câu một dòng, không giải thích:\n"
    )

    if not NGROK_URL:
        print("Warning: NGROK_URL not configured, returning original query")
        return [query]

    response = call_qwen_4b(query_rewrite_prompt, NGROK_URL)

    if response and not response.startswith("Lỗi:"):
        # Tách các dòng và làm sạch
        lines = response.split('\n')
        queries = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Bỏ qua các dòng không phải câu hỏi (tiếng Anh, số thứ tự, etc.)
            if any(word.lower() in line.lower() for word in ['okay', 'let\'s', 'first', 'user', 'think', 'wait', 'the']):
                continue

            # Loại bỏ số thứ tự ở đầu dòng (1., 2., -, •, etc.)
            import re
            line = re.sub(r'^\d+\.?\s*', '', line)  # Loại bỏ "1. " hoặc "1 "
            line = re.sub(r'^[-•*]\s*', '', line)   # Loại bỏ "- " hoặc "• "
            line = line.strip()

            if line and len(line) > 10 and not line.lower().startswith(('vui lòng', 'okay', 'first')):
                queries.append(line)

        # Giới hạn số lượng câu hỏi theo k
        queries = queries[:k] if len(queries) > k else queries
        return queries if queries else [query]
    else:
        print(f"Rewrite failed: {response}")
        return [query]


# PromptTemplate cần được khởi tạo với mẫu cụ thể
prompt_template = PromptTemplate(
    input_variables=["context", "question", "conversation_context"],
    template="""
{conversation_context}

Chỉ dựa vào thông tin sau, hãy trả lời câu hỏi sau một cách ngắn gọn, không hiện suy nghĩ:
{context}
Câu hỏi: {question}
Trả lời:
"""
)

def classify_question_4b(question: str, ngrok_url: str = NGROK_URL) -> str:
    """
    Phân loại câu hỏi bằng chính Qwen 4B model qua ngrok
    """
    if not ngrok_url:
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
        response = call_qwen_4b(classification_prompt, ngrok_url).strip().upper()
        
        if "SOLVING" in response:
            return 'math_solving'
        elif "KNOWLEDGE" in response:
            return 'knowledge_retrieval'
        else:
            return None
    except Exception as e:
        print(f"⚠️ Lỗi phân loại Qwen 4B: {e}")
        return None


def solve_question_4b(question: str, k: int = 3, ngrok_url: str = NGROK_URL, rerank: bool = False, rewrite: bool = True, conversation_history: list = None):
    """
    Giải câu hỏi với hỗ trợ conversation context.
    Tự động phân loại câu hỏi để quyết định dùng RAG hay giải toán trực tiếp.
    
    Args:
        question: Câu hỏi hiện tại
        k: Số lượng tài liệu retrieve
        ngrok_url: URL của ngrok server
        rerank: Có sử dụng reranking không
        rewrite: Có rewrite query không
        conversation_history: Lịch sử trò chuyện (danh sách messages)
    """
    # Phân loại câu hỏi bằng chính Qwen 4B model
    def model_classify_func(q):
        return classify_question_4b(q, ngrok_url)
    
    question_type = classify_question_type_generic(question, model_classify_func)
    print(f"🔍 Loại câu hỏi được phân loại bởi Qwen 4B: {question_type}")
    
    # Xây dựng conversation context
    conversation_context = ""
    if conversation_history and conversation_manager.should_use_context(question, conversation_history):
        conversation_context = conversation_manager.build_conversation_context(conversation_history, question)
        print(f"🔄 Sử dụng conversation context: {len(conversation_context)} ký tự")
    
    if question_type == 'math_solving':
        # Giải toán trực tiếp - không cần retrieval
        print("⚡ Chế độ giải toán trực tiếp (không dùng RAG)")
        return solve_math_direct_4b(question, ngrok_url, conversation_history)
    else:
        # Dùng RAG để tìm kiếm tài liệu
        print("📚 Chế độ tìm kiếm tài liệu (dùng RAG)")
        
        # Tạo queries với rewrite
        if rewrite:
            # Nếu có context, có thể cải thiện query
            if conversation_context:
                topics = conversation_manager.extract_key_topics(conversation_history)
                enhanced_question = question
                if topics:
                    enhanced_question = f"{question} (Liên quan: {', '.join(topics)})"
                queries = rewrite_query_4b(enhanced_question, 3)
            else:
                queries = rewrite_query_4b(question, 3)
            queries.append(question)  # Thêm câu hỏi gốc vào cuối
        else:
            queries = [question]

        # Collect documents từ tất cả queries
        docs = []
        for query in queries:
            custom_retriever = db.as_retriever(search_kwargs={"k": k})
            doc = custom_retriever.invoke(query)
            
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
        
        # Lấy nội dung các tài liệu
        context = "\n".join([split_combined_content(doc.page_content) for doc in docs])

        # Áp dụng PromptTemplate để tạo prompt hoàn chỉnh
        prompt_text = prompt_template.format(
            context=context, 
            question=question, 
            conversation_context=conversation_context
        )

        # Gửi prompt tới mô hình qua ngrok
        answer = call_qwen_4b(prompt_text, ngrok_url)

        # Xử lý nếu mô hình lặp lại câu hỏi
        if question in answer:
            answer = answer.split(question)[-1].strip(": \n")

        # Nếu không có câu trả lời rõ ràng, fallback
        if not answer.strip():
            fallback_prompt = f"Câu hỏi: {question}\nTrả lời ngắn gọn:"
            answer = call_qwen_4b(fallback_prompt, ngrok_url)

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

from langchain.prompts import PromptTemplate as MathPromptTemplate

def solve_math_question_4b(question: str, k: int = 3, ngrok_url: str = NGROK_URL, rerank: bool = False, rewrite: bool = True, conversation_history: list = None):
    """
    Giải toán bước-by-step, sử dụng biểu diễn LaTeX cho công thức.
    Trả về answer và source_docs.
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
            queries = rewrite_query_4b(enhanced_question, 3)
        else:
            queries = rewrite_query_4b(question, 3)
        queries.append(question)  # Thêm câu hỏi gốc vào cuối
    else:
        queries = [question]

    # Collect documents từ tất cả queries
    docs = []
    for query in queries:
        custom_retriever = db.as_retriever(search_kwargs={"k": k})
        doc = custom_retriever.invoke(query)
        
        # Rerank nếu cần
        if rerank and RERANK_AVAILABLE:
            try:
                reranker = FlagReranker(RERANK_MODEL, use_fp16=True)
                doc = rerank_docs_with_model(query, doc, reranker)
            except Exception:
                pass
        
        docs.extend([doc])

    # Sử dụng reciprocal rank fusion để kết hợp kết quả
    docs = reciprocal_rank_fusion(docs, num_docs=k)
    
    # Chuẩn bị context
    context = "\n".join([split_combined_content(doc.page_content) for doc in docs])
    
    # Math prompt template
    math_template = MathPromptTemplate(
        input_variables=["context", "question", "conversation_context"],
        template="""
Bạn là trợ lý AI chuyên giải các bài toán.

{conversation_context}

Dựa vào thông tin sau:
{context}
Hãy giải bài toán sau đây từng bước một, không nhắc lại, không hiện suy nghĩ, hiển thị các công thức trong khối LaTeX (dùng $$):
Câu hỏi: {question}
Đầu ra:
1. Phân tích bài toán.
2. Giải các bước chi tiết kèm công thức.
3. Kết luận câu trả lời cuối cùng.
"""
    )
    prompt_text = math_template.format(
        context=context, 
        question=question, 
        conversation_context=conversation_context
    )
    
    # Gọi API
    raw = call_qwen_4b(prompt_text, ngrok_url)
    
    # Xử lý
    answer = raw.strip()
    
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


# Hàm giải toán không dùng retrieval - chỉ dùng model trực tiếp
def solve_math_direct_4b(question: str, ngrok_url: str = NGROK_URL, conversation_history: list = None):
    """
    Giải toán trực tiếp bằng Qwen 4B không cần retrieval documents
    
    Args:
        question: Câu hỏi toán học
        ngrok_url: URL của ngrok server
        conversation_history: Lịch sử trò chuyện
    """
    try:
        # Xây dựng conversation context
        conversation_context = ""
        if conversation_history and conversation_manager.should_use_context(question, conversation_history):
            conversation_context = conversation_manager.build_conversation_context(conversation_history, question)
            print(f"🔄 Sử dụng conversation context: {len(conversation_context)} ký tự")
        
        # Tạo prompt giải toán trực tiếp
        math_prompt = f"""
Bạn là trợ lý AI chuyên giải các bài toán.

{conversation_context}

Hãy giải bài toán sau đây từng bước một, hiển thị các công thức trong khối LaTeX (đặt giữa $$):

Câu hỏi: {question}

Hãy làm theo các bước:
1. Phân tích đề bài và xác định phương pháp giải
2. Giải chi tiết từng bước  
3. Đưa ra kết luận cuối cùng

Trả lời:
"""

        # Gọi API thông qua ngrok
        answer = call_qwen_4b(math_prompt, ngrok_url)

        # Xử lý nếu mô hình lặp lại câu hỏi
        if question in answer:
            answer = answer.split(question)[-1].strip(": \n")

        # Nếu không có câu trả lời rõ ràng, fallback
        if not answer.strip():
            fallback_prompt = f"Giải bài toán: {question}"
            answer = call_qwen_4b(fallback_prompt, ngrok_url)

        # Trả về với source_docs và rewrite_queries rỗng vì không dùng retrieval
        return answer, [], []
    
    except Exception as e:
        return f"Lỗi khi xử lý câu hỏi: {str(e)}", [], []