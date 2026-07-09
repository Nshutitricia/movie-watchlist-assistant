from fastapi import APIRouter, Request, Response
from pydantic import BaseModel
from sqlmodel import Session

from app.database import engine
from app.session import get_session_id, get_history
from app.services.claude_service import get_response

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(payload: ChatRequest, request: Request, response: Response):
    session_id = get_session_id(request, response)
    history = get_history(session_id)

    history.append({"role": "user", "content": payload.message})

    with Session(engine) as db_session:
        reply = get_response(history, db_session)

    history.append({"role": "assistant", "content": reply})

    return {"reply": reply}