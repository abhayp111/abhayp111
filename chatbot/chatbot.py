# chatbot/chatbot.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline
import numpy as np

# Load documents
with open("documents.txt", "r") as f:
    documents = [line.strip() for line in f.readlines()]

# Load embeddings and models
doc_embeddings = np.load("doc_embeddings.npy")
embedder = SentenceTransformer("all-MiniLM-L6-v2")
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def chat(query, top_k=3):
    query_embedding = embedder.encode([query], convert_to_numpy=True)
    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    retrieved_docs = [documents[i] for i in top_indices]
    context = " ".join(retrieved_docs)

    result = qa_pipeline(question=query, context=context)
    return result["answer"]
