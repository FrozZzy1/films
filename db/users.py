from datetime import datetime
from sqlalchemy import Column, String, DateTime

from db.abstract import AbstractModel


class UserModel(AbstractModel):
    username = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String)
    middle_name = Column(String, nullable=True)
    last_name = Column(String)
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
