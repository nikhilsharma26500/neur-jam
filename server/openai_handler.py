from openai  import AsyncOpenAI

class OpenAIHandler:
    
    def get_response_openAI(self, model: str, query: str, api_key: str):
        client = AsyncOpenAI()
        response = client.chat.completions

