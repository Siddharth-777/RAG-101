from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore
from rag.retriever import Retriever
from rag.prompt import create_prompt
from rag.llm import OllamaLLM



# Initialize models once

embedding_model = EmbeddingModel()



# Initialize FAISS

vector_store = VectorStore(
    dimension=384
)



# Load existing FAISS index

vector_store.load(
    "faiss_index"
)



# Retriever

retriever = Retriever(
    vector_store,
    embedding_model
)



# Ollama LLM

llm = OllamaLLM()



def process(data):


    query = data.text



    print("\nUSER QUERY:")
    print(query)



    print(
        "\nFAISS VECTOR COUNT:",
        vector_store.index.ntotal
    )


    print(
        "METADATA COUNT:",
        len(vector_store.metadata)
    )



    # Retrieve relevant chunks

    chunks = retriever.retrieve(
        query,
        top_k=5
    )



    print(
        "\nRETRIEVED CHUNKS:"
    )


    for chunk in chunks:

        print("----------------")
        print(chunk)



    # If no chunks found

    if not chunks:

        return (
            "I could not find the answer "
            "in the provided documents."
        )



    # Create prompt

    prompt = create_prompt(
        query,
        chunks
    )



    print(
        "\nGENERATED PROMPT:"
    )

    print(prompt)



    # Query Ollama

    response = llm.generate(
        prompt
    )



    return response