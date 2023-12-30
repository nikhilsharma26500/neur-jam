import json
import os
from dotenv import load_dotenv, find_dotenv
import google.generativeai as gemini_AI


class GeminiAIHandler:

    def get_response_gemini(
        self,
        model: str,
        user_query: str,
        api_key: str,
    ):
        gemini_AI.configure(api_key=api_key)
        model = gemini_AI.GenerativeModel(model)

        response = model.generate_content(user_query)

        try:
            return response.text
        except:
            raise ValueError("The response is not found, try again!")
