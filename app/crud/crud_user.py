from typing import Optional

from pydantic import EmailStr
from pymongo.collection import Collection

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserUpdate, UserCreate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_by_email(self, db: Collection, email: EmailStr) -> Optional[User]:
        return db.find_one({'email': email})

    async def get_by_username(self, db: Collection, username: str) -> Optional[User]:
        return db.find_one({'email': username})

    async def check_user_exists(self, db: Collection, username: str, email: EmailStr) -> bool:
        return await db.find_one({"$or": [{"username": username}, {"email": email}]})


user = CRUDUser(User)
