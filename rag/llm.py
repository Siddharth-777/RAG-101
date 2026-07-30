import ollama



class OllamaLLM:


    def __init__(
        self,
        model="llama3:latest"
    ):

        self.model = model



    def generate(
        self,
        prompt: str
    ):

        """
        Sends prompt to Ollama
        and returns generated response.
        """


        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )


        return response["message"]["content"]