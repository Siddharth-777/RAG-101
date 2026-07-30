# RAG-101 Backend Documentation

## Overview

RAG-101 is a FastAPI backend foundation for building a Retrieval-Augmented Generation (RAG) system.

The current backend provides:

* FastAPI application setup
* API key authentication
* Health check endpoint
* Document upload endpoint
* Supabase integration
* Raw document storage using Supabase Storage
* Document metadata storage using Supabase PostgreSQL
* Request and response validation

The backend will later be extended with:

* Document parsing
* Text cleaning
* Document chunking
* Embedding generation
* FAISS vector database integration
* Semantic search
* Ollama LLM integration

---

# Project Structure

```
RAG-101/
│
├── main.py
├── core.py
├── models.py
├── supabase_client.py
├── requirements.txt
├── .env
│
└── Supabase
    │
    ├── Storage Bucket
    │      └── raw_documents
    │
    └── Database Table
           └── document_metadata
```

---

# Files Documentation

---

# 1. main.py

## Purpose

`main.py` is the main entry point of the FastAPI backend.

It handles:

* Creating the FastAPI application
* Loading environment variables
* API key authentication
* Defining API routes
* Handling document uploads
* Connecting API requests with backend logic

---

## FastAPI Application

The application is created using FastAPI.

It provides:

* REST API endpoints
* Request handling
* Swagger API documentation
* Error handling

Swagger documentation is available at:

```
/docs
```

---

# API Authentication

RAG-101 uses API key-based authentication.

The API key is stored inside `.env`.

Example:

```env
API_KEY=my_secret_key
```

Protected endpoints require:

```
X-API-Key: my_secret_key
```

Protected routes:

| Endpoint   | Method |
| ---------- | ------ |
| `/upload`  | POST   |
| `/process` | POST   |

---

# Endpoints

## GET /

### Description

Checks whether the backend is running.

### Response

```json
{
    "message": "RAG-101 Backend Running"
}
```

---

## GET /health

### Description

Health monitoring endpoint.

Used for checking whether the API service is active.

### Response

```json
{
    "status": "OK"
}
```

---

## POST /upload

### Description

Uploads raw documents to Supabase Storage.

The uploaded documents are stored inside the `raw_documents` Supabase bucket.

The endpoint performs:

* Receiving the uploaded file
* Reading file contents
* Uploading the file to Supabase Storage
* Storing document metadata in PostgreSQL

### Request

Type:

```
multipart/form-data
```

Required field:

```
file
```

Example:

```
document.pdf
```

---

### Response

Example:

```json
{
    "message": "File uploaded successfully",
    "filename": "document.pdf",
    "storage_path": "raw_documents/document.pdf",
    "size": 12345
}
```

---

## POST /process

### Description

Main processing endpoint.

Currently, it calls the processing function from `core.py`.

Future functionality:

* Generate query embeddings
* Search relevant documents
* Retrieve context
* Generate response using LLM

---

### Request Body

```json
{
    "text": "Explain Retrieval Augmented Generation"
}
```

---

### Response

```json
{
    "result": "Done"
}
```

---

# 2. models.py

## Purpose

`models.py` contains Pydantic models used for request and response validation.

It ensures that API inputs and outputs follow a fixed structure.

Benefits:

* Automatic validation
* Type checking
* Cleaner API handling
* Swagger documentation support

---

# ProcessRequest

Used for receiving input data.

Code:

```python
class ProcessRequest(BaseModel):
    text: str
```

Expected request:

```json
{
    "text": "Hello World"
}
```

---

# ProcessResponse

Used for sending API responses.

Code:

```python
class ProcessResponse(BaseModel):
    result: str
```

Response:

```json
{
    "result": "Done"
}
```

---

# 3. core.py

## Purpose

`core.py` contains the main business logic of the application.

The API layer calls functions from this file instead of containing processing logic directly.

---

## Current Implementation

Currently:

```python
def process(data):

    return "Done"
```

It acts as a placeholder for future RAG processing.

---

## Future Responsibilities

This file will later handle:

* Query processing
* Embedding generation
* Vector database search
* Context retrieval
* LLM response generation

---

# 4. supabase_client.py

## Purpose

`supabase_client.py` manages the connection between the FastAPI backend and Supabase.

It creates a reusable Supabase client that can be used throughout the project.

---

## Responsibilities

* Load Supabase credentials
* Create Supabase connection
* Provide access to:

  * Supabase Storage
  * PostgreSQL database

---

## Environment Variables Required

The file requires:

```env
SUPABASE_URL=
SUPABASE_KEY=
```

Example:

```env
SUPABASE_URL=https://project-id.supabase.co
SUPABASE_KEY=service-role-key
```

---

## Usage

The client is imported into backend files:

```python
from supabase_client import supabase
```

It is used for:

* Uploading documents
* Storing metadata
* Accessing Supabase services

---

# 5. Supabase Storage

## Purpose

Supabase Storage is used to store the original uploaded documents.

Instead of saving files locally, documents are stored in the cloud.

---

## Storage Bucket

Bucket name:

```
raw_documents
```

Example stored files:

```
raw_documents/
    research.pdf
    report.docx
    notes.txt
```

---

## Why Store Raw Documents?

The original documents are required as the source for the RAG pipeline.

They will later be used for:

* Text extraction
* Cleaning
* Chunk generation
* Embedding creation

---

# 6. Supabase Database

## Purpose

The PostgreSQL database stores metadata about uploaded documents.

Table name:

```
document_metadata
```

---

## Table Schema

| Column       | Type      |
| ------------ | --------- |
| id           | uuid      |
| filename     | text      |
| file_type    | text      |
| size         | bigint    |
| storage_path | text      |
| created_at   | timestamp |

---

## Example Record

```json
{
    "filename": "research.pdf",
    "file_type": "application/pdf",
    "size": 50000,
    "storage_path": "raw_documents/research.pdf"
}
```

---

# 7. requirements.txt

## Purpose

Contains all Python dependencies required to run the backend.

Current dependencies:

```
fastapi
uvicorn
supabase
python-dotenv
```

---

## Dependencies

### FastAPI

Used for:

* Creating APIs
* Handling requests
* Managing routes

---

### Uvicorn

Used as the ASGI server to run FastAPI.

Command:

```
uvicorn main:app --reload
```

---

### Supabase

Python SDK used for:

* Storage operations
* Database operations

---

### python-dotenv

Used for loading environment variables from `.env`.

---

# 8. .env

## Purpose

Stores sensitive configuration values.

Example:

```env
API_KEY=my_secret_key

SUPABASE_URL=https://project.supabase.co

SUPABASE_KEY=my_service_key
```

---

## Security

The `.env` file should never be committed to GitHub.

Add it to:

```
.gitignore
```

---

# Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Backend Server

```bash
uvicorn main:app --reload
```

---

## Access API

Backend:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# Current Implementation Status

## Completed

* FastAPI backend setup
* API key authentication
* Root endpoint
* Health endpoint
* File upload API
* Supabase connection
* Raw document storage
* Metadata storage
* Request/response validation

---

## Pending

* Document parsing
* Text cleaning
* Chunk creation
* Metadata extraction
* Embedding generation
* FAISS vector database
* Semantic search
* Ollama LLM integration

---

# Summary

RAG-101 currently provides the backend foundation required for building a complete RAG application.

The current system handles document ingestion and storage, while future modules will extend it into a complete retrieval and generation pipeline.
