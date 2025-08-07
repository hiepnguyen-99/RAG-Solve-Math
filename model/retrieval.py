import torch

from FlagEmbedding import FlagReranker
from langchain.load import dumps, loads


def rerank_docs_with_model(query, docs, reranker, metadata_fields=["title", "section", "subsection"], num_doc = 3):
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
    docs = [doc for doc, _ in ranked_docs]
    num_doc = len(docs) if len(docs) < num_doc else num_doc
    return docs[:num_doc]


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


def reciprocal_rank_fusion(matrix: list[list], k=60, num_docs=3):
    fused_scores = {}
    doc_map = {}

    for query_result in matrix:
        for rank, doc in enumerate(query_result):
            doc_id = doc.page_content  # hoặc dùng hash(doc.page_content + str(doc.metadata))
            if doc_id not in fused_scores:
                fused_scores[doc_id] = 0
                doc_map[doc_id] = doc  # Lưu lại object gốc

            fused_scores[doc_id] += 1 / (rank + k)

    # Sắp xếp theo điểm giảm dần
    reranked = sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)

    return [doc_map[doc_id] for doc_id, _ in reranked][:num_docs]


def split_combined_content(combined_content):
    try:
        return combined_content.split("|||", 1)[-1]
    except Exception as e:
        print("Lỗi khi tách nội dung:", e)
        return None
