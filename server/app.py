from fastapi import FastAPI
from gemini_handler import GeminiAIHandler
from db_functions import add_conversation
from db_schema import table_session
import os

import uuid

app = FastAPI()

handler = GeminiAIHandler()


@app.post("/gemini_ai/{model}")
async def gemini_ai(model: str, query: str, GEMININ_API_KEY):
    session = table_session()

    # GEMININ_API_KEY = os.getenv("GEMININ_API_KEY")

    response = handler.get_response_gemini(model, query, GEMININ_API_KEY)

    add_conversation(
        uid="a6d3af6b4faa4766b23a4d70662f6abc",
        chat_id=uuid.uuid4().hex,
        model=model,
        user_query=query,
        model_response=response,
    )

    session.close()

    return {"response from Gemini": response}
