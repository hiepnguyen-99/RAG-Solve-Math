import re
import os
import torch
import glob
import hashlib

from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain.document_loaders import TextLoader, DirectoryLoader
from sentence_transformers import SentenceTransformer
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from google.generativeai import genai
from langchain_community.rerankers import FlagReranker


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
raw_data_folder = "../TEST"
model_name = "math-similarity/Bert-MLM_arXiv-MP-class_zbMath"
persist_directory = "../chroma_db"
rerank_model = "BAAI/bge-reranker-base"


embedding_model = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs={"device": DEVICE},
    encode_kwargs={"normalize_embeddings": True}
)

vectorstore = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding_model,
    collection_name="math_vectors"
)

genai.configure(api_key="AIzaSyD-0XwdOenWyJyQo5nB2BEYQUjpfYhlhrs")
model = genai.GenerativeModel("gemini-2.5-flash-lite")


def rewrite_query(query):
    query_rewrite_prompt = f"""Viết lại truy vấn sau theo cách phổ biến và đơn giản nhất để tra cứu thông tin trong tài liệu toán học. Nếu có từ đồng nghĩa hoặc cách diễn đạt khác sát nghĩa hơn, hãy ưu tiên dùng:
    Gốc: "{query}"
    (Chỉ in ra truy vấn đã viết lại)
    """
    response = model.generate_content(query_rewrite_prompt)
    return response.text.strip()


def rerank_docs_with_model(query, docs, reranker):
    pairs = [(query, doc.page_content) for doc in docs]
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
