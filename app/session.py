import uuid
from fastapi import Request, Response

conversations: dict[str, list[dict]] = {}

COOKIE_NAME = "watchlist_session_id"


def get_session_id(request: Request, response: Response) -> str:
    session_id = request.cookies.get(COOKIE_NAME)

    if not session_id:
        session_id = str(uuid.uuid4())
        response.set_cookie(key=COOKIE_NAME, value=session_id, httponly=True)

    if session_id not in conversations:
        conversations[session_id] = []

    return session_id


def get_history(session_id: str) -> list[dict]:
    return conversations[session_id]