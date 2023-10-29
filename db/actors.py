from datetime import datetime
from sqlalchemy import Column, String, Date, DateTime, Integer
from .base import Base


class ActorModel(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    birthday = Column(Date, nullable=True)
    photo = Column(String, nullable=False)
    photo_gallery = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
