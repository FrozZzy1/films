from fastapi import FastAPI

from api.endpoints import users
from db.base import database, engine, Base

app = FastAPI(
    title='Films',
)
app.include_router(users.router, prefix='/users')


@app.on_event('startup')
async def startup():
    await database.connect()
    Base.metadata.create_all(bind=engine)


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()
