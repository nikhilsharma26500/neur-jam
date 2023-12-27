import os
from dotenv import load_dotenv, find_dotenv
import requests


class MistralAIHandler:
    def get_response_MistralAI(self, model: str, user_query: str, api_key: str):
        API_URL = f"https://api-inference.huggingface.co/models/mistralai/{model}"

        MISTRAL_API_KEY = api_key

        if MISTRAL_API_KEY:
            headers = {"Authorization": f"Bearer {MISTRAL_API_KEY}"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)

                return response.json()

            output = query({"inputs": user_query})

            return output[0]["generated_text"]

        else:
            raise ValueError("API key not found")