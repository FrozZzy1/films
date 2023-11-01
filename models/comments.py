from datetime import datetime
from typing import Optional

from pydantic import BaseModel, constr

from db.users import UserModel


class Comment(BaseModel):
    id: Optional[int] = None
    creator: UserModel
    text: str
    rating: float
    created_at: datetime
    updated_at: datetime


class CommentIn(BaseModel):
    text: constr(max_length=1024)
