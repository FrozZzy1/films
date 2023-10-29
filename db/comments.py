from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float

from .base import Base


class CommentModel(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    creator = Column(Integer, ForeignKey('users.id'), nullable=False)
    text = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
