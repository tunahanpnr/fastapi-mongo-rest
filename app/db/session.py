from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.database import Database

from app.core.config import config

# create a connection pool using AsyncIOMotorClient
client: AsyncIOMotorClient = AsyncIOMotorClient(
    f"mongodb://{config.MONGO_URI}:{config.MONGO_PORT}", maxPoolSize=100
)


# inject the database connection into the endpoints using dependency injection
async def get_mongodb() -> Database:
    return client.get_database(config.MONGO_DB_NAME)
