from datetime import timedelta
from typing import Any

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pymongo.database import Database

from app import crud, schemas
from app.core import security
from app.db.session import get_mongodb
from app.schemas.user import UserDTO, UserSignUp

router = APIRouter()


@router.post("/signin", response_model=schemas.Token)
async def signin(db: Database = Depends(get_mongodb), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
        OAuth2 compatible token login, get an access token for future requests
    """
    user = await crud.user.authenticate(
        db['users'], username=form_data.username, password=form_data.password
    )

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    return {
        "access_token": security.create_access_token(user.id),
        "token_type": "bearer",
    }


@router.post("/signup")
async def signup(user: UserSignUp, db: Database = Depends(get_mongodb)) -> UserDTO:
    is_exists: bool = await crud.user.is_user_exist(db['users'], user.username, user.email)
    if is_exists:
        raise HTTPException(
            status_code=400,
            detail="Username or email already exists.",
        )

    db_user = await crud.user.create(db['users'], user)

    return db_user
