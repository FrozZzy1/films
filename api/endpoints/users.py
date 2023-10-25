from fastapi import APIRouter, Depends

from api.depends.repositories import get_user_repository
from repositories.users import UserRepository

router = APIRouter()


@router.get('/')
async def read_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 0,):
    return await users.get_all(limit=limit, skip=skip)
