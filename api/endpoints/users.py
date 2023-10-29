from fastapi import APIRouter, Depends

from api.depends.repositories import get_user_repository
from models.users import User, UserIn
from repositories.users import UserRepository

router = APIRouter()


@router.get('/')
async def read_users(
        users: UserRepository = Depends(get_user_repository),
        limit: int = 100,
        skip: int = 0, ):
    return await users.get_all(limit=limit, skip=skip)


@router.post('/', response_model=User)
async def create(
        user: UserIn,
        users: UserRepository = Depends(get_user_repository), ) -> User:
    return await users.create(u=user)
