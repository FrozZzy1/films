from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel

from db.actors import ActorModel
from db.comments import CommentModel
from db.movies import Genre, MovieModel
from db.users import UserModel


class RatingMPAA(str, Enum):
    G = 'G'
    PG = 'PG'
    PG_13 = 'PG-13'
    R = 'R'
    NC_17 = 'NC-17'


class Movie(BaseModel):
    id: int
    title: str
    year: date
    country: str
    genre_id: Genre
    actors_id: Optional[ActorModel] = None
    description: str
    photo: str
    photo_gallery: Optional[str] = None
    similar_movies: Optional[MovieModel] = None
    rating: Optional[float] = 0
    rating_MPAA: Optional[RatingMPAA] = None
    comment_list: Optional[CommentModel] = None
    movie_submitter: UserModel
    receptionist: Optional[UserModel] = None
    created_at: datetime
    updated_at: datetime


class MovieIn(BaseModel):
    title: str
    year: date
    country: str
    genre_id: Genre
    actors_id: Optional[ActorModel]
    description: str
    photo: str
    photo_gallery: Optional[str]
    similar_movies: Optional[MovieModel]
    rating_MPAA: Optional[RatingMPAA]
