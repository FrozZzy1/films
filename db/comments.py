from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from db.abstract import AbstractModel


class CommentModel(AbstractModel):
    __tablename__ = 'comments'

    creator = Column(Integer, ForeignKey('users.id'), nullable=False)
    text = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())