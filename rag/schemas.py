from pydantic import BaseModel


class DocumentPage(BaseModel):
    page_number: int
    text: str



class DocumentChunk(BaseModel):
    chunk_id: int
    text: str
    page_number: int
    filename: str