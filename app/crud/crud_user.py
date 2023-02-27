from typing import Optional

from bson import ObjectId
from pydantic import EmailStr
from pymongo.collection import Collection

from app.core.security import verify_password, get_password_hash
from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.user import UserUpdate, UserCreate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_by_email(self, db: Collection, email: EmailStr) -> Optional[User]:
        return await db.find_one({'email': email})

    async def get_by_username(self, db: Collection, username: str) -> Optional[User]:
        db_user = await db.find_one({'username': username})
        return User(**db_user)

    async def is_user_exist(self, db: Collection, username: str, email: EmailStr) -> bool:
        return await db.find_one({"$or": [{"username": username}, {"email": email}]})

    async def create(self, db: Collection, obj_in: UserCreate) -> ObjectId:
        obj_in.password = get_password_hash(obj_in.password)

        return await super().create(db, obj_in)

    async def authenticate(self, db: Collection, username: str, password: str) -> Optional[User]:
        db_user = await self.get_by_username(db, username=username)

        if not db_user:
            return None
        if not verify_password(password, db_user.password):
            return None

        return db_user


user = CRUDUser(User)
