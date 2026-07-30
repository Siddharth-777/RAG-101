import faiss
import numpy as np
import pickle



class VectorStore:


    def __init__(
        self,
        dimension
    ):

        self.dimension = dimension


        self.index = faiss.IndexFlatL2(
            dimension
        )


        self.metadata = []



    def add_vectors(
        self,
        embeddings,
        chunks
    ):

        embeddings = np.array(
            embeddings
        ).astype("float32")


        self.index.add(
            embeddings
        )


        for chunk in chunks:

            self.metadata.append(
                chunk.model_dump()
            )



    def search(
        self,
        query_embedding,
        top_k=5
    ):


        query_embedding = np.array(
            [query_embedding]
        ).astype("float32")


        distances, indices = self.index.search(
            query_embedding,
            top_k
        )


        results = []


        for index in indices[0]:

            if index < len(self.metadata):

                results.append(
                    self.metadata[index]
                )


        return results



    def save(
        self,
        path="faiss_index"
    ):


        faiss.write_index(
            self.index,
            f"{path}.index"
        )


        with open(
            f"{path}.pkl",
            "wb"
        ) as file:

            pickle.dump(
                self.metadata,
                file
            )



    def load(
        self,
        path="faiss_index"
    ):


        self.index = faiss.read_index(
            f"{path}.index"
        )


        with open(
            f"{path}.pkl",
            "rb"
        ) as file:

            self.metadata = pickle.load(
                file
            )