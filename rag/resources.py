from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


# Load embedding model once

embedding_model = EmbeddingModel()



# Create FAISS vector store once

vector_store = VectorStore(
    dimension=384
)



# Load existing FAISS index if available

vector_store.load(
    "faiss_index"
)