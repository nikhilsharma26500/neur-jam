from fastapi import FastAPI

from handlers.gemini_handler import GeminiAIHandler
from handlers.openai_handler import OpenAIHandler
from handlers.mistral_handler import MistralAIHandler
from handlers.llama_handler import LlamaAIHandler

from db_functions import add_conversation
from db_schema import table_session
import os

import uuid

app = FastAPI()

handler_gemini = GeminiAIHandler()
handler_openAI = OpenAIHandler()
handler_mistral = MistralAIHandler()
handler_llama = LlamaAIHandler()


@app.post("/gemini_ai/{model}")
async def gemini_ai(model: str, user_query: str):
    session = table_session()

    # GEMININ_API_KEY = os.getenv("GEMININ_API_KEY")

    response = handler_gemini.get_response_gemini(model, user_query, api_key= os.getenv("GEMININ_API_KEY"))

    add_conversation(
        uid="a6d3af6b4faa4766b23a4d70662f6abc",
        chat_id=uuid.uuid4().hex,
        model=model,
        user_query=user_query,
        model_response=response,
    )

    session.close()

    return {"response from Gemini": response}


@app.post("/open_ai/{model}")
async def open_ai(model: str, system_message: str, user_query: str):
    session = table_session()

    response = handler_openAI.get_response_openAI(model=model, system_message=system_message, user_query=user_query, api_key=os.getenv("OPENAI_API_KEY"))

    add_conversation(
        uid="a6d3af6b4faa4766b23a4d70662f6abc",
        chat_id=uuid.uuid4().hex,
        model=model,
        user_query=user_query,
        model_response=response,
    )

    session.close()

    return {"response from OpenAI": response}


@app.post("/mistral_ai/{model}")
async def mistral_ai(model: str, system_message: str, user_query: str):
    
    response = handler_mistral.get_response_MistralAI(model=model, system_message=system_message, user_query=user_query, api_key=os.getenv("FIREWORKS_API_KEY"))
    
    add_conversation(
        uid="a6d3af6b4faa4766b23a4d70662f6abc",
        chat_id=uuid.uuid4().hex,
        model=model,
        user_query=user_query,
        model_response=response,
    )
    
    return {"response from Mistral": response}


@app.post("/llama_ai/{model}")
async def llama_ai(model: str, system_message: str, user_query: str):
    
    response = handler_llama.get_response_llama(model=model, system_message=system_message, user_query=user_query, api_key=os.getenv("FIREWORKS_API_KEY"))
    
    add_conversation(
        uid="a6d3af6b4faa4766b23a4d70662f6abc",
        chat_id=uuid.uuid4().hex,
        model=model,
        user_query=user_query,
        model_response=response,
    )
    
    return {"response from Llama": response}