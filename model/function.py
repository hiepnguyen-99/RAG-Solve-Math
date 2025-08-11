import os
import torch
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from retrieval import *
from conversation_manager import conversation_manager

device = "cuda" if torch.cuda.is_available() else "cpu"
# ===== Khởi tạo embedding model chung =====
def get_embedding_model():
    """Trả về embedding model chung cho tất cả RAG systems"""
    return HuggingFaceEmbeddings(
        model_name="Qwen/Qwen3-Embedding-0.6B",
        model_kwargs={"device": device},
        encode_kwargs={"normalize_embeddings": True}
    )

# ===== Khởi tạo Chroma database =====
def get_chroma_db():
    """Trả về Chroma database instance"""
    chroma_path = "./chroma_db"
    embedding_model = get_embedding_model()
    return Chroma(
        persist_directory=chroma_path,
        embedding_function=embedding_model,
        collection_name="math_vectors"
    )