from sentence_transformers import SentenceTransformer
import numpy as np
import fitz  # PyMuPDF
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 1. Extract text from PDF
doc = fitz.open("Attention.pdf")
text = ""
for page in doc:
    text += page.get_text()

# Optional: Save raw PDF text to a file
with open("paper_text.txt", "w", encoding="utf-8") as f:
    f.write(text)

# 2. Split PDF text into smaller chunks or sentences
def chunk_text(text, chunk_size=40):
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

documents = chunk_text(text, chunk_size=40)  # You can adjust chunk_size

# Optional: filter very short/empty chunks
documents = [doc.strip() for doc in documents if len(doc.strip().split()) > 5]

# 3. Create embeddings
embedder = SentenceTransformer("all-MiniLM-L6-v2")
doc_embeddings = embedder.encode(documents, convert_to_numpy=True)

# 4. Save embeddings for later use
np.save("doc_embeddings.npy", doc_embeddings)
np.save("doc_chunks.npy", np.array(documents))

# 5. Visualize using PCA (optional, but cool)
pca = PCA(n_components=2)
reduced = pca.fit_transform(doc_embeddings)

plt.figure(figsize=(12, 8))
plt.scatter(reduced[:, 0], reduced[:, 1], alpha=0.6)
for i, sentence in enumerate(documents[:30]):  # limit to avoid clutter
    plt.annotate(sentence[:40] + "...", (reduced[i, 0], reduced[i, 1]), fontsize=8)
plt.title("PDF Sentence Embeddings (PCA Projection)")
plt.show()
