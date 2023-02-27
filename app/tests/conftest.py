import asyncio

import pytest
from fastapi.testclient import TestClient
from mongomock.database import Database
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import config
from app.main import app


# this one solved "Event loop is closed" error
# happened due to asyncio
@pytest.yield_fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='module')
def test_client():
    return TestClient(app)


@pytest.fixture(scope='module')
def get_db() -> Database:
    client: AsyncIOMotorClient = AsyncIOMotorClient(
        f"mongodb://{config.MONGO_URI}:{config.MONGO_PORT}", maxPoolSize=100
    )
    db = client.get_database(config.MONGO_DB_NAME_MOCK)
    yield db
    try:
        client.drop_database(config.MONGO_DB_NAME_MOCK)
    except Exception as e:
        print(e)


@pytest.mark.asyncio
@pytest.fixture(scope='function')
def mock_db(monkeypatch):
    from app.tests.db import get_mongodb_mock
    monkeypatch.setattr('app.db.session.get_mongodb', get_mongodb_mock)

# each collection can be initialized like below if it is necessary
# @pytest.fixture(scope='function')
# def items_collection(database):
#     return database.items
