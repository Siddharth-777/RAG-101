from fastapi import FastAPI, UploadFile, File, HTTPException, Security
from fastapi.security import APIKeyHeader
from pathlib import Path
from dotenv import load_dotenv
import os

from models import ProcessRequest, ProcessResponse
from core import process

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
async def upload(file: UploadFile = File(...),api_key: str = Security(verify_api_key)):
    try:
        contents = await file.read()

        file_path = UPLOAD_DIR / Path(file.filename).name

        with open(file_path, "wb") as f:
            f.write(contents)

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "size": len(contents)
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )


# MAIN APPLICATION ENDPOINT
@app.post("/process", response_model=ProcessResponse)
def process_endpoint(data: ProcessRequest,api_key: str = Security(verify_api_key)):
    try:
        result = process(data)

        return ProcessResponse(result=result)

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )