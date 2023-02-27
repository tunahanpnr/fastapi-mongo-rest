from pydantic import EmailStr

from app.models.base import Base


class User(Base):
    name: str
    surname: str
    username: str
    email: EmailStr
    is_active: bool = False
    is_admin: bool = False
