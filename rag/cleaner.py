import re


def clean_text(text: str) -> str:
    """
    Cleans extracted document text.

    Removes:
    - Extra spaces
    - Multiple new lines
    - Unwanted symbols

    Returns:
    - Cleaned text
    """

    if not text:
        return ""


    # Remove multiple spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )


    # Remove unnecessary symbols
    text = re.sub(
        r"[•●■◆]",
        "",
        text
    )


    # Remove leading/trailing spaces
    text = text.strip()


    return text



def clean_documents(pages):
    """
    Cleans extracted document pages.

    Input:
    [
        DocumentPage(
            page_number=1,
            text="raw text"
        )
    ]

    Output:
    [
        DocumentPage(
            page_number=1,
            text="cleaned text"
        )
    ]
    """


    cleaned_pages = []


    for page in pages:


        cleaned_text = clean_text(
            page.text
        )


        page.text = cleaned_text


        cleaned_pages.append(
            page
        )


    return cleaned_pages