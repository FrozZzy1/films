from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

from core.config import settings

database = Database(settings.DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    settings.DATABASE_URL,
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()
