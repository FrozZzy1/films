from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from pydantic import BaseModel

from core.security import verify_password, create_access_token, create_refresh_token
from db.base import db
from db.users import UserModel

router = APIRouter()


class Token(BaseModel):
    access_token: str
    refresh_token: str


@router.post('/login', summary='User auth', response_model=Token)
async def authentication_user(data: OAuth2PasswordRequestForm = Depends()):
    user = db.query(UserModel).filter(UserModel.username == data.username).one()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect email/username or password'
        )

    if not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect email/username or password'
        )
    access_token = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})

    return {
        "access_token": access_token,
        'refresh_token': refresh_token,
    }
