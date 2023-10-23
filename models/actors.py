from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class Actor(BaseModel):
    id: int
    full_name: str
    birthday: Optional[date]
    photo: str
    photo_gallery: Optional[str]
    created_at: datetime
    updated_at: datetime


class ActorIn(BaseModel):
    full_name: str
    birthday: Optional[date]
    photo: str
    photo_gallery: Optional[str]

