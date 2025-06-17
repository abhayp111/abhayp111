# chatbot/embed.py
from sentence_transformers import SentenceTransformer
import numpy as np

# Documents to embed
documents = [
    "RAG stands for Retrieval-Augmented Generation. It combines document retrieval with language generation.",
    "Transformers are models based on self-attention mechanisms for NLP tasks.",
    "HuggingFace provides pre-trained transformer models and tokenizers.",
    "PyTorch is an open-source deep learning framework developed by Meta.",
    "Sentence embeddings capture the meaning of a sentence in vector form.",
    "Abhay is Senior Software Engineer at TIAA",
    "Abhay has done MBA from Manipal",
    "Abhay is a good guy",
    "Abhay was born in 1996"
]

# Save documents to disk
with open("documents.txt", "w") as f:
    for doc in documents:
        f.write(doc + "\n")

# Create embeddings
embedder = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = embedder.encode(documents, convert_to_numpy=True)

for i, emb in enumerate(doc_embeddings):
    print(f"Sentence: {documents[i]}")
    print(f"Embedding (shape {emb.shape}):")
    print(emb)
    print("-" * 50)


# Save embeddings
np.save("doc_embeddings.npy", doc_embeddings)

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

pca = PCA(n_components=2)
reduced = pca.fit_transform(doc_embeddings)

plt.scatter(reduced[:,0], reduced[:,1])
for i, sentence in enumerate(documents):
    plt.annotate(sentence, (reduced[i,0], reduced[i,1]))
plt.title("Sentence Embeddings (PCA Projection)")
plt.show()

