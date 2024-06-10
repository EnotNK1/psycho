import uuid

from fastapi import APIRouter, Cookie
from schemas.users import Creds, Reg, ResetPassword, UpdateUser, AuthToken, UserResponse
from services.users import user_service
from starlette.responses import JSONResponse, Response

router = APIRouter()


@router.post(
    "/users/reg",
    response_model=UserResponse,
)
def register_user(data: Reg):
    return user_service.register(data)


@router.post(
    "/users/auth",
    response_model=UserResponse,
)
def auth_user(data: Creds, response: Response):
    return user_service.authorization(data, response)


@router.post(
    "/users/auth_token",
    response_model=UserResponse,
)
def auth_token_user(data: AuthToken, response: Response):
    return user_service.authorization_token(data, response)


@router.get(
    "/users/get",
    status_code=200,
    response_model=None,
)
def get_users(access_token: str = Cookie(None)):
    return user_service.get_users(access_token)


@router.post(
    "/users/reset_password",
    response_model=None,
)
def reset_password(data: ResetPassword):
    return user_service.reset_password(data)


@router.post(
    "/users/update_user",
    response_model=None,
)
def update_user(data: UpdateUser, access_token: str = Cookie(None)):
    return user_service.update_user(data, access_token)
