from databases.interfaces import Record

from db.users import UserModel
from repositories.base import BaseRepository


class UserRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0) -> list[Record]:
        query = UserModel.select().limit(limit).offset(skip)

        return await self.database.fetch_all(query=query)
