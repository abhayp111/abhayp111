# chatbot/chatbot.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from transformers import pipeline
import torch


# ✅ Load embeddings + text chunks
documents = np.load("doc_chunks.npy", allow_pickle=True).tolist()
doc_embeddings = np.load("doc_embeddings.npy")

# ✅ Load embedder for queries
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ Load a CPU-friendly, instruction-tuned model (Flan-T5)
rag_pipeline = pipeline(
    "text2text-generation",  # ✅ Correct for encoder-decoder models
    model="google/flan-t5-small",
    device=0 if torch.cuda.is_available() else -1,  # -1 for CPU
    max_new_tokens=100,
    do_sample=True,
    temperature=0.7,
)

def chat(query, top_k=3):
    # 1. Embed the query
    query_embedding = embedder.encode([query], convert_to_numpy=True)

    # 2. Find most similar chunks
    similarities = cosine_similarity(query_embedding, doc_embeddings)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    retrieved_docs = [documents[i] for i in top_indices]
    context = " ".join(retrieved_docs)

    # 3. Format the prompt
    prompt = f"Context: {context}\n\nQuestion: {query}"

    # 4. Generate answer
    response = rag_pipeline(prompt)[0]["generated_text"]

    # 5. Clean result
    if response.startswith(prompt):
        response = response[len(prompt):].strip()
    if "Answer:" in response:
        return response.split("Answer:")[-1].strip()
    return response.strip()


# chatbot/main.py

if __name__ == "__main__":
    print("📘 PDF Chatbot Ready!")
    while True:
        query = input("Ask a question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        answer = chat(query)
        print("Answer:", answer)
        print("-" * 80)
