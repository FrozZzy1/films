from pydantic import BaseModel


class Genre(BaseModel):
    id: int
    title: str
    description: str


class GenreIn(BaseModel):
    title: str
    description: str
