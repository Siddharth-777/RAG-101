from pathlib import Path

import fitz   # PyMuPDF
from docx import Document

from rag.schemas import DocumentPage
from rag.cleaner import clean_text



def parse_pdf(file_path: str):

    pages = []

    document = fitz.open(file_path)


    for index, page in enumerate(document):

        text = page.get_text()


        cleaned_text = clean_text(text)


        if cleaned_text:

            pages.append(
                DocumentPage(
                    page_number=index + 1,
                    text=cleaned_text
                )
            )


    document.close()


    return pages



def parse_docx(file_path: str):

    document = Document(file_path)

    text = "\n".join(
        [
            paragraph.text
            for paragraph in document.paragraphs
        ]
    )


    cleaned_text = clean_text(text)


    if cleaned_text:

        return [
            DocumentPage(
                page_number=1,
                text=cleaned_text
            )
        ]


    return []



def parse_txt(file_path: str):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        text = file.read()


    cleaned_text = clean_text(text)


    if cleaned_text:

        return [
            DocumentPage(
                page_number=1,
                text=cleaned_text
            )
        ]


    return []



def parse_document(file_path: str):

    """
    Detect file type and extract content.
    """

    extension = Path(file_path).suffix.lower()


    if extension == ".pdf":

        return parse_pdf(file_path)


    elif extension == ".docx":

        return parse_docx(file_path)


    elif extension == ".txt":

        return parse_txt(file_path)


    else:

        raise ValueError(
            f"Unsupported file type: {extension}"
        )

        