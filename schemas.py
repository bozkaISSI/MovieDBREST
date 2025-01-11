from typing import List, Optional
from pydantic import BaseModel

class Actor(BaseModel):
    id: int
    name: str
    surname: str

    class Config:
        orm_mode = True

class Movie(BaseModel):
    id: int
    title: str
    director: str
    year: int
    description: Optional[str]
    actors: List[Actor] = []

    class Config:
        orm_mode = True
