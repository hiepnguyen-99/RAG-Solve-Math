import torch

from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.rerankers import FlagReranker


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
raw_data_folder = "../TEST"
embedding_model_name = "Qwen/Qwen3-Embedding-0.6B"
persist_directory = "../chroma_db"
rerank_model = "BAAI/bge-reranker-base"


embedding_model = HuggingFaceEmbeddings(
    model_name=embedding_model_name,
    model_kwargs={"device": DEVICE},
    encode_kwargs={"normalize_embeddings": True}
)

vectorstore = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding_model,
    collection_name="math_vectors"
)


def rerank_docs_with_model(query, docs, reranker, metadata_fields=["title", "section", "subsection"]):
    pairs = []
    for doc in docs:
        # Kết hợp nhiều trường metadata lại thành một chuỗi
        content_parts = [doc.metadata.get(field, "") for field in metadata_fields]
        content_for_rerank = " - ".join(part for part in content_parts if part)  # loại bỏ rỗng
        pairs.append((query, content_for_rerank))

    # Reranker trả về list điểm tương ứng
    scores = reranker.compute_score(pairs)

    scored_docs = list(zip(docs, scores))
    ranked_docs = sorted(scored_docs, key=lambda x: x[1], reverse=True)
    return [doc for doc, _ in ranked_docs]


def retrieve_docs(query, k=5, rerank=False):
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    docs = retriever.get_relevant_documents(query)
    if rerank:
        reranker = FlagReranker(rerank_model, use_fp16=True)
        docs = rerank_docs_with_model(query, docs, reranker)
    return docs



# Example usage
# dos.metadata.get("source") sẽ chứa đường dẫn đến file gốc
