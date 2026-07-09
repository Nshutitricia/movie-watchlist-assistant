from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class Movie(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    genre: str
    date_added: datetime = Field(default_factory= datetime.utcnow)