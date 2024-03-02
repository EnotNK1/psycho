import uuid

from fastapi import APIRouter, Cookie
from schemas.users import Creds, Reg
from services.users import user_service
from starlette.responses import JSONResponse, Response

router = APIRouter()

@router.post(
    "/users",
    response_model=None,
)
def register_user(data: Reg):
    return user_service.register(data)

@router.post(
    "/users/auth",
    response_model=None,
)
def auth_user(data: Creds, response: Response):
    return user_service.authorization (data, response)

@router.get(
    "/users",
    status_code=200,
    response_model=None,
)
def get_users(access_token: str = Cookie(None)):
    return user_service.get_users(access_token)