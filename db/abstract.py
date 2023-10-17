from sqlalchemy import Column, Integer
from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative
class AbstractModel:
    id = Column(Integer, autoincrement=True, primary_key=True)

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
