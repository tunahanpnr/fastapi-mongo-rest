from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    username: Optional[str]
    email: Optional[EmailStr]


class UserCreate(UserBase):
    name: str
    surname: str
    username: str
    email: EmailStr
    password: str
    is_active: bool = False
    is_admin: bool = False


class UserSignUp(UserBase):
    name: str
    surname: str
    username: str
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None
    is_active: Optional[bool] = False
    is_admin: Optional[bool] = False


class UserDTO(UserBase):
    pass
