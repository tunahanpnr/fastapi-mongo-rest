from typing import Any, Dict, Generic, List, Type, TypeVar, Union

from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from pymongo.database import Collection

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: Collection, id: Any) -> ModelType:
        data = await db.find_one({'_id': id})

        return data

    async def get_multi(
            self, db: Collection, skip: int = 0, limit: int = 100
    ) -> List[ModelType]:
        data: List[ModelType] = []
        cursor = db.find({}).skip(skip).limit(limit)
        async for document in cursor:
            data.append(document)

        return data

    async def create(self, db: Collection, obj_in: CreateSchemaType) -> ObjectId:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        del db_obj.id
        res = await db.insert_one(dict(db_obj))
        return res.inserted_id

    async def update(
            self,
            db: Collection,
            id: ObjectId,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> bool:
        filter = {'_id': id}
        update = {'$set': obj_in}
        db_obj = await db.update_one(filter, update)

        return db_obj.acknowledged and db_obj.modified_count == 1

    async def remove(self, db: Collection, id: int) -> bool:
        result = await db.delete_one({'_id': id})
        return result is not None
