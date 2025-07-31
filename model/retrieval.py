import torch

from FlagEmbedding import FlagReranker
from langchain.load import dumps, loads


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


def retrieve_docs(query, k=5, rerank=False, vectorstore=None, rerank_model=None):
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    docs = retriever.get_relevant_documents(query)
    if rerank:
        reranker = FlagReranker(rerank_model, use_fp16=True)
        docs = rerank_docs_with_model(query, docs, reranker)
    return docs


def retrieve_docs_RAG_fuson(queries, k=5, rerank=False, vectorstore=None, reranker=None):
    docs = []
    for query in queries:
        retriever = vectorstore.as_retriever(search_kwargs={"k": k})
        doc = retriever.get_relevant_documents(query)
        if rerank:
            doc = rerank_docs_with_model(query, doc, reranker)
        docs.extend([doc])
    return docs


def reciprocal_rank_fusion(matrix: list[list], k=60, num_docs=5):
    fused_scores = {}

    for query_result in matrix: 
        for rank, doc in enumerate(query_result):
            doc_str = dumps(doc) 
            if doc_str not in fused_scores:
                fused_scores[doc_str] = 0
            fused_scores[doc_str] += 1 / (rank + k)

    reranked_results = [
        (loads(doc_str), score)
        for doc_str, score in sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)
    ]
    return [doc for doc, _ in reranked_results][:num_docs] 

# Example usage
# dos.metadata.get("source") sẽ chứa đường dẫn đến file gốc
