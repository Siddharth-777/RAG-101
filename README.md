# RAG-101

A simple Retrieval-Augmented Generation (RAG) system built using **FastAPI**, **FAISS**, **Sentence Transformers**, **Supabase**, and **Ollama**. The application allows users to upload documents, index them into a vector database, and ask questions based on the uploaded documents using a local Large Language Model (LLM).

---

## Features

* Upload PDF documents
* Store raw documents in Supabase Storage
* Store document metadata in Supabase Database
* Parse and clean document text
* Create overlapping text chunks
* Generate embeddings using Sentence Transformers
* Store embeddings in FAISS
* Perform semantic similarity search
* Generate responses using Ollama
* FastAPI backend with Swagger documentation
* Minimal HTML, CSS and JavaScript frontend

---

## Tech Stack

### Backend

* Python
* FastAPI
* FAISS
* Sentence Transformers
* Ollama
* Supabase
* PyMuPDF
* Pydantic

### Frontend

* HTML
* CSS
* JavaScript

---

## Project Structure

```text
RAG-101/

├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── rag/
│   ├── parser.py
│   ├── cleaner.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── prompt.py
│   ├── llm.py
│   ├── ingestion.py
│   ├── schemas.py
│   └── resources.py
│
├── main.py
├── core.py
├── models.py
├── supabase_client.py
├── requirements.txt
├── .env
└── README.md
```

---

## How It Works

1. Upload a PDF document.
2. Store the original file in Supabase Storage.
3. Save document metadata in Supabase.
4. Extract text from the document.
5. Clean the extracted text.
6. Split the text into overlapping chunks.
7. Generate vector embeddings for each chunk.
8. Store embeddings in a FAISS vector database.
9. Convert the user's question into an embedding.
10. Retrieve the most relevant chunks using semantic search.
11. Create a prompt using the retrieved context and the user query.
12. Send the prompt to Ollama.
13. Return the generated answer.

---

## API Endpoints

### GET /

Returns a simple message indicating that the backend is running.

---

### GET /health

Returns the current health status of the backend.

---

### POST /upload

Uploads a document to the system.

This endpoint:

* Uploads the file to Supabase Storage
* Saves document metadata
* Parses the document
* Cleans the extracted text
* Creates overlapping chunks
* Generates embeddings
* Stores vectors in FAISS

---

### POST /process

Accepts a user query and returns an answer.

This endpoint:

* Converts the query into an embedding
* Retrieves the Top-K most relevant chunks
* Creates the prompt
* Sends the prompt to Ollama
* Returns the generated response

---

## Project Modules

### main.py

Main FastAPI application.

Responsibilities:

* API endpoints
* Authentication
* File uploads
* Document ingestion
* Processing user queries

---

### core.py

Implements the RAG pipeline.

Responsibilities:

* Retrieve relevant chunks
* Generate prompts
* Query the LLM
* Return the final response

---

### models.py

Contains the request and response models used by FastAPI.

---

### supabase_client.py

Initializes the Supabase client using credentials from the `.env` file.

---

### parser.py

Extracts text from PDF documents while preserving page numbers.

---

### cleaner.py

Removes unnecessary spaces and unwanted characters from extracted text.

---

### chunker.py

Splits cleaned text into overlapping chunks and stores chunk metadata.

---

### embeddings.py

Generates sentence embeddings using the **all-MiniLM-L6-v2** model.

---

### vector_store.py

Handles FAISS operations.

Functions include:

* Add vectors
* Search vectors
* Save index
* Load index

---

### retriever.py

Performs semantic similarity search and returns the most relevant chunks.

---

### prompt.py

Builds the prompt by combining the retrieved chunks with the user's query.

---

### llm.py

Communicates with the locally running Ollama model and returns the generated response.

---

### ingestion.py

Runs the complete indexing pipeline:

* Parse
* Clean
* Chunk
* Embed
* Store in FAISS

---

### schemas.py

Contains the Pydantic models used throughout the RAG pipeline.

---

### resources.py

Initializes shared resources such as the embedding model and vector store.

---

## Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=rag101

SUPABASE_URL=your_supabase_url

SUPABASE_KEY=your_supabase_service_key

OLLAMA_MODEL=llama3:latest
```

---

## Installation

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Backend

Start the FastAPI server.

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Running Ollama

Start the Ollama server.

```bash
ollama serve
```

Verify the installed model.

```bash
ollama list
```

---

## Running the Frontend

Navigate to the frontend folder.

```bash
cd frontend
```

Start a simple web server.

```bash
python -m http.server 5500
```

Open the application in your browser.

```
http://localhost:5500
```

---

## Future Improvements

* Support DOCX and TXT files
* Source citations with page references
* Conversation history
* Streaming responses
* Hybrid search
* User authentication
* Cloud vector database support
* Docker deployment
* Production-ready logging and monitoring

---

## Author

**Siddharth Srinivasan**

**RAG-101** — A Basic Retrieval-Augmented Generation System built using FastAPI, FAISS, Supabase and Ollama.
