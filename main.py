from fastapi import FastAPI, UploadFile, File, HTTPException, Security
from fastapi.security import APIKeyHeader
from pathlib import Path
from dotenv import load_dotenv
import os
from supabase_client import supabase
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

from models import ProcessRequest, ProcessResponse
from core import process
from rag.ingestion import ingest_document

# LOAD ENVIRONMENT VARIABLES
load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY not found in .env")

# API KEY SECURITY
api_key_header = APIKeyHeader(
    name="X-API-Key",
    scheme_name="API Key",
    description="Enter your API Key"
)

# CREATE FASTAPI APP
app = FastAPI(
    title="SID01",
    description="Template for Backend Deployment",
    version="1.0.0",
    docs_url="/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:8001",
        "http://localhost:8001",
        "null"      # allows opening index.html directly
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CREATE UPLOAD DIRECTORY
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


# VERIFY API KEY
def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    return api_key


# ROOT ENDPOINT
@app.get("/")
def root():
    return {
        "message": "SID01 Backend Running"
    }


# HEALTH CHECK ENDPOINT
@app.get("/health")
def health():
    return {
        "status": "OK"
    }


# FILE UPLOAD ENDPOINT
@app.post("/upload")
async def upload(
    file: UploadFile = File(...),
    api_key: str = Security(verify_api_key)
):

    try:

        # Read file content

        contents = await file.read()



        # Create storage path

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        storage_path = (
            f"raw_documents/{timestamp}_{file.filename}"
        )



        # Upload file to Supabase Storage

        storage_response = (
            supabase.storage
            .from_("raw_documents")
            .upload(
                path=storage_path,
                file=contents,
                file_options={
                    "content-type": file.content_type
                }
            )
        )



        # Store metadata in database

        metadata = {

            "filename": file.filename,

            "file_type": file.content_type,

            "size": len(contents),

            "storage_path": storage_path

        }



        db_response = (
            supabase
            .table("document_metadata")
            .insert(metadata)
            .execute()
        )



        # -----------------------------
        # TEMPORARY LOCAL FILE
        # FOR RAG INGESTION
        # -----------------------------


        temp_dir = Path(
            "temp_documents"
        )


        temp_dir.mkdir(
            exist_ok=True
        )


        temp_file_path = (
            temp_dir / file.filename
        )


        with open(
            temp_file_path,
            "wb"
        ) as f:

            f.write(contents)



        # -----------------------------
        # RUN RAG INGESTION PIPELINE
        # -----------------------------


        ingest_document(
            str(temp_file_path)
        )



        return {

            "message":
                "File uploaded and indexed successfully",

            "filename":
                file.filename,

            "storage_path":
                storage_path,

            "size":
                len(contents)

        }



    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# MAIN APPLICATION ENDPOINT
@app.post("/process",response_model=ProcessResponse)
def process_endpoint(
    data: ProcessRequest,
    api_key: str = Security(verify_api_key)
):

    result = process(data)

    return ProcessResponse(
        result=result
    )