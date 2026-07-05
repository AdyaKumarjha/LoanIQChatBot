from fastapi import APIRouter
from pydantic import BaseModel

from services.chatbot import chatbot

router = APIRouter(prefix="/chat", tags=["Chatbot"])


class ChatRequest(BaseModel):
    message: str


@router.post("/")
def chat(request: ChatRequest):

    return {
        "question": request.message,
        "answer": chatbot.reply(request.message)
    }