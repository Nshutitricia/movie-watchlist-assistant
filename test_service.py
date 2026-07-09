from sqlmodel import Session
from app.database import engine, init_db
from app.services import watchlist_service as ws

init_db()

with Session(engine) as session:
    print(ws.add_movie(session, "Inception", "Sci-Fi"))
    print(ws.list_movies(session))
    print(ws.add_movie(session, "inception", "Sci-Fi"))  # should print None (duplicate)
    print(ws.pick_random_movie(session))
    print(ws.remove_movie(session, "Inception"))
    print(ws.list_movies(session))