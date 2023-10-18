from sqlalchemy import Column, Integer
from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative
class AbstractModel:
    __tablename__ = 'abstactmodel'

    id = Column(Integer, autoincrement=True, primary_key=True)
