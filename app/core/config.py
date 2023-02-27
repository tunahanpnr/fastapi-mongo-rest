import secrets

from pydantic import AnyHttpUrl, BaseSettings


class Config(BaseSettings):
    PROJECT_NAME: str = 'fastapi-mongo-rest'

    SERVER_HOST: AnyHttpUrl = 'http://127.0.0.1:8000/'

    # MongoDB attributes
    MONGO_URI: str = 'localhost'
    MONGO_PORT: int = 27017
    MONGO_DB_NAME: str = "fastapidb"
    MONGO_DB_NAME_MOCK: str = "fastapi-db-test"

    # security configs
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 7 days = 1 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


config = Config()
