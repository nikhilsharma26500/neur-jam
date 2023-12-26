import json
import os
from dotenv import load_dotenv, find_dotenv
import google.generativeai as gemini_AI


class GeminiAIHandler:
    # def __init__(
    #     self,
    #     api_key: str = None,
    # ):
    # load_dotenv(find_dotenv())
    # GEMININAI_API_KEY = os.getenv("GEMININ_API_KEY")

    # if GEMININAI_API_KEY == None:
    # if GEMININAI_API_KEY == None:
    #     raise ValueError("Setup the GEMININAI_API_KEY in the environment file")

    def get_response_gemini(
        self,
        model: str,
        query: str,
        api_key: str,
    ):
        gemini_AI.configure(api_key=api_key)
        model = gemini_AI.GenerativeModel(model)

        response = model.generate_content(query)

        try:
            return response.text
        except:
            raise ValueError("The response is not found, try again!")
