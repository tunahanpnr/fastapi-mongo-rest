from pydantic import AnyHttpUrl, BaseSettings


class Config(BaseSettings):
    PROJECT_NAME: str = 'fastapi-mongo-rest'

    SERVER_HOST: AnyHttpUrl = 'http://127.0.0.1:8000/'

    # MongoDB attributes
    MONGO_URI: str = 'localhost'
    MONGO_PORT: int = 27017
    MONGO_DB_NAME: str = "fastapidb"
    MONGO_DB_NAME_MOCK: str = "fastapidb"

    class Config:
        case_sensitive = True


config = Config()
