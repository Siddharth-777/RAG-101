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