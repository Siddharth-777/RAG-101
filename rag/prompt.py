def create_prompt(
    query: str,
    chunks: list
):

    """
    Creates RAG prompt using retrieved chunks.

    Args:
        query:
            User question

        chunks:
            Retrieved FAISS metadata

    Returns:
            Formatted prompt for LLM
    """


    context = ""


    for chunk in chunks:

        context += (
            f"""
Source:
File: {chunk['filename']}
Page: {chunk['page_number']}

Content:
{chunk['text']}

-------------------------
"""
        )


    prompt = f"""
You are a helpful AI assistant.

Answer the user's question only using the provided context.

If the answer is not available in the context, reply:
"I could not find the answer in the provided documents."

Do not make assumptions.
Do not use outside knowledge.

CONTEXT:
{context}


USER QUESTION:
{query}


ANSWER:
"""


    return prompt