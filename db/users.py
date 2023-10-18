from datetime import datetime
from sqlalchemy import Column, String, DateTime

from db.abstract import AbstractModel


class UserModel(AbstractModel):
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
