from fastapi import FastAPI
from gemini_handler import GeminiAIHandler
from db_functions import add_conversation
from db_schema import table_session

import uuid

app = FastAPI()

handler = GeminiAIHandler()


@app.post("/gemini_ai")
async def gemini_ai(model: str, query: str):
    session = table_session()
    response = handler.get_response(model, query)
    add_conversation(
        uid="a6d3af6b4faa4766b23a4d70662f6abc",
        chat_id=uuid.uuid4().hex,
        model=model,
        user_query=query,
        model_response=response,
    )
    session.close()
    return {"response from Gemini": response}
