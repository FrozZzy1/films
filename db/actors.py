from datetime import datetime
from sqlalchemy import Column, String, Date, DateTime

from db.abstract import AbstractModel


class ActorModel(AbstractModel):
    full_name = Column(String, nullable=False)
    birthday = Column(Date, nullable=True)
    photo = Column(String, nullable=False)
    photo_gallery = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
