import json
import os
from dotenv import load_dotenv, find_dotenv
import google.generativeai as gemini_AI

class GeminiAIHandler:
    
    def __init__(
        self,
        # user_model
    ):
        load_dotenv(find_dotenv())
        GEMININAI_API_KEY = os.getenv("GEMININ_API_KEY")
        gemini_AI.configure(api_key=GEMININAI_API_KEY)
        
        if GEMININAI_API_KEY == None:
            raise ValueError("Setup the GEMININAI_API_KEY in the environment file")
        
        # self.model = user_model
        
    def get_response(self, model, query):
        
        # user_model = self.user_model
        
        model = gemini_AI.GenerativeModel(model)
        
        response = model.generate_content(query)
        
        try:
            return response.text
        except:
            raise ValueError("The response is not found, try again!")
        