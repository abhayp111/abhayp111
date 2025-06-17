import tensorflow_hub as hub
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap

# 1. Load Universal Sentence Encoder from TensorFlow Hub
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# 2. Example sentences
sentences = [
    "The cat sat on the mat.",
    "A dog was barking loudly.",
    "The sun is shining today.",
    "Rainy days make me sad.",
    "I love programming in Python.",
    "Machine learning is fascinating.",
    "I had pizza for lunch.",
    "The pizza was delicious.",
    "She enjoys reading books.",
    "He went to the library."
]

# 3. Get embeddings
embeddings = embed(sentences).numpy()  # shape: (10, 512)

# 4. Dimensionality Reduction

# PCA
pca_result = PCA(n_components=2).fit_transform(embeddings)

# t-SNE
tsne_result = TSNE(n_components=2, perplexity=5, random_state=42).fit_transform(embeddings)

# UMAP
umap_result = umap.UMAP(n_components=2, random_state=42).fit_transform(embeddings)

# 5. Plotting Function
def plot_2d(points, title):
    plt.figure(figsize=(6, 5))
    plt.scatter(points[:, 0], points[:, 1])
    for i, text in enumerate(sentences):
        plt.annotate(text[:20] + "...", (points[i, 0], points[i, 1]), fontsize=8)
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 6. Visualize all three
plot_2d(pca_result, "PCA Visualization")
plot_2d(tsne_result, "t-SNE Visualization")
plot_2d(umap_result, "UMAP Visualization")
