from datetime import datetime
from pydantic import BaseModel, constr

from db.users import UserModel


class Comment(BaseModel):
    id: int
    creator: UserModel
    text: str
    rating: float
    created_at: datetime
    updated_at: datetime


class CommentIn(BaseModel):
    text: constr(max_length=1024)
