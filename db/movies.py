import enum

from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Enum, DateTime

from db.abstract import AbstractModel


class RatingMPAAEnum(enum.Enum):
    G = 'G'
    PG = 'PG'
    PG_13 = 'PG-13'
    R = 'R'
    NC_17 = 'NC-17'


class Genre(AbstractModel):
    __tablename__ = 'genres'

    title = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)


class MovieModel(AbstractModel):
    __tablename__ = 'movies'

    title = Column(String, unique=True, nullable=False)
    year = Column(Integer, nullable=False)
    country = Column(String, nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'), nullable=False)
    actors_id = Column(Integer, ForeignKey('actors.id'))
    description = Column(String, nullable=False)
    photo = Column(String, nullable=False)
    photo_gallery = Column(String, nullable=True)
    similar_movies = Column(String, nullable=True)
    rating = Column(Float, default=0, nullable=True)
    rating_MPAA = Column(Enum(RatingMPAAEnum), nullable=False)
    comment_list = Column(Integer, ForeignKey('comments.id'), nullable=True)
    movie_submitter = Column(Integer, ForeignKey('users.id'), nullable=True)
    receptionist = Column(Integer, ForeignKey('users.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
