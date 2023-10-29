from datetime import datetime

from databases.interfaces import Record
from sqlalchemy import insert, select

from core.security import hash_password
from db.users import UserModel
from models.users import UserIn, User
from repositories.base import BaseRepository


class UserRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0) -> list[Record]:
        query = select(UserModel).limit(limit).offset(skip)

        return await self.database.fetch_all(query=query)

    async def create(self, u: UserIn) -> User:
        created_time = datetime.utcnow()

        user = User(
            username=u.username,
            password=hash_password(u.password1),
            first_name=u.first_name,
            middle_name=u.middle_name,
            last_name=u.last_name,
            email=u.email,
            created_at=created_time,
            updated_at=created_time,
        )

        values = user.model_dump(exclude={'id'})
        query = insert(UserModel).values(**values)
        user.id = await self.database.execute(query)

        return user
