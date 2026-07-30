from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore



class Retriever:


    def __init__(
        self,
        vector_store: VectorStore,
        embedding_model: EmbeddingModel
    ):

        self.vector_store = vector_store

        self.embedding_model = embedding_model



    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        """
        Retrieves most relevant chunks
        based on semantic similarity.
        """


        # Convert user query into embedding

        query_embedding = (
            self.embedding_model
            .generate_embeddings(
                [query]
            )[0]
        )


        # Search FAISS

        results = (
            self.vector_store
            .search(
                query_embedding,
                top_k
            )
        )


        return results