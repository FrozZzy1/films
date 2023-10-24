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
    actors_id: Optional[ActorModel]
    description: str
    photo: str
    photo_gallery: Optional[str]
    similar_movies: Optional[MovieModel]
    rating: Optional[float]
    rating_MPAA: Optional[RatingMPAA]
    comment_list: Optional[CommentModel]
    movie_submitter: Optional[UserModel]
    receptionist: Optional[UserModel]
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
