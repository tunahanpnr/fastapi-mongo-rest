from fastapi import FastAPI

from app.api.api_v1.api import api_router
from app.core.config import config

app = FastAPI(
    title=config.PROJECT_NAME
)

app.include_router(api_router)
