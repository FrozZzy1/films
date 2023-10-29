from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean, Integer

from .base import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=True)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
