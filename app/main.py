from fastapi import FastAPI
from app.database import init_db
from app.routes.chat import router as chat_router

app = FastAPI(title="Movie Watchlist Assistant")


@app.on_event("startup")
def on_startup():
    init_db()


app.include_router(chat_router)
