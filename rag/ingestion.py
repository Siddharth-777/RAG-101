from rag.parser import parse_document
from rag.cleaner import clean_documents
from rag.chunker import create_chunks
from rag.resources import (
    embedding_model,
    vector_store
)
import os



def ingest_document(file_path):


    print(
        "Starting ingestion..."
    )


    # 1. Parse PDF

    pages = parse_document(
        file_path
    )


    print(
        "Pages extracted:",
        len(pages)
    )



    # 2. Clean text

    cleaned_pages = clean_documents(
        pages
    )


    print(
        "Cleaning completed"
    )

    filename = os.path.basename(file_path)



    # 3. Create chunks

    chunks = create_chunks(
        cleaned_pages,
        filename
    )


    print(
        "Chunks created:",
        len(chunks)
    )



    # 4. Generate embeddings

    texts = [
    chunk.text
    for chunk in chunks
    ]


    embeddings = embedding_model.generate_embeddings(
        texts
    )


    print(
        "Embeddings generated:",
        len(embeddings)
    )



    # 5. Add vectors to FAISS

    vector_store.add_vectors(
        embeddings,
        chunks
    )



    print(
        "FAISS vectors:",
        vector_store.index.ntotal
    )


    print(
        "Metadata count:",
        len(vector_store.metadata)
    )



    # 6. Save FAISS index

    vector_store.save(
        "faiss_index"
    )


    print(
        "FAISS saved successfully"
    )


    return True