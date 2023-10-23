from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, constr, field_validator
from pydantic_core.core_schema import FieldValidationInfo
from core.validation import password_pattern


class User(BaseModel):
    id: int
    username: str
    password: str
    first_name: str
    middle_name: Optional[str]
    last_name: str
    email: EmailStr
    is_admin: bool
    created_at: datetime
    updated_at: datetime


class UserIn(BaseModel):
    username: str
    password1: constr(min_length=6)
    password2: str
    first_name: str
    middle_name: Optional[str]
    last_name: str
    email: EmailStr

    @field_validator('password2')
    @classmethod
    def validate_password(cls, value: str, values: FieldValidationInfo, **kwargs) -> str:
        if value != values.data.get('password1'):
            raise ValueError('passwords don`t match')
        if ' ' in value:
            raise ValueError('password must not contain any spaces')
        if not password_pattern.search(value):
            raise ValueError('password must contain at least one capital letter or one special character')

        return value
