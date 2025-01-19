from typing import List, Optional
from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    year: int
    director: str
    description: Optional[str] = None


class MovieCreate(MovieBase):
    """Schema for creating a new movie."""
    pass


class Movie(MovieBase):
    id: int
    actors: List['Actor'] = []

    class Config:
        from_attributes = True  # Replaces orm_mode


class ActorBase(BaseModel):
    name: str
    surname: str


class ActorCreate(ActorBase):
    """Schema for creating a new actor."""
    pass


class Actor(ActorBase):
    id: int

    class Config:
        from_attributes = True  # Replaces orm_mode
