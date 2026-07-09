from sqlmodel import Session, select
from app.models import Movie


def add_movie(session: Session, title: str, genre: str):
    movies = session.exec(select(Movie)).all()
    for m in movies:
        if m.title.strip().lower() == title.strip().lower():
            return None

    movie = Movie(title=title.strip(), genre=genre.strip())
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return movie


def list_movies(session: Session):
    return session.exec(select(Movie)).all()


def remove_movie(session: Session, title: str):
    movies = session.exec(select(Movie)).all()
    for m in movies:
        if m.title.strip().lower() == title.strip().lower():
            session.delete(m)
            session.commit()
            return m
    return None


def pick_random_movie(session: Session):
    movies = list_movies(session)
    if not movies:
        return None
    import random
    return random.choice(movies)