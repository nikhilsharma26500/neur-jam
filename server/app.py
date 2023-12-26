from fastapi import FastAPI
from gemini_handler import GeminiAIHandler


app = FastAPI()

handler = GeminiAIHandler()

@app.post("/gemini_ai")
async def gemini_ai(model:str, query: str):
    response = handler.get_response(model, query)
    return {"response from Gemini": response}