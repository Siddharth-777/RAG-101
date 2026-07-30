from rag.schemas import DocumentPage, DocumentChunk



def create_chunks(
    pages: list[DocumentPage],
    filename: str,
    chunk_size: int = 500,
    overlap: int = 100
):

    """
    Creates overlapping text chunks.

    chunk_size:
        Number of words per chunk

    overlap:
        Number of words repeated between chunks
    """


    chunks = []

    chunk_id = 0


    for page in pages:

        words = page.text.split()


        start = 0


        while start < len(words):

            end = start + chunk_size


            chunk_words = words[start:end]


            chunk_text = " ".join(chunk_words)


            chunks.append(
                DocumentChunk(
                    chunk_id=chunk_id,
                    text=chunk_text,
                    page_number=page.page_number,
                    filename=filename
                )
            )


            chunk_id += 1


            # Move forward while keeping overlap
            start += chunk_size - overlap



    return chunks