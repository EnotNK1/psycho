import uuid

from fastapi import APIRouter, Cookie, Depends
from starlette.websockets import WebSocket

from schemas.users import Creds, Reg, EmailRequest, ResetPasswordRequest, UpdateUser, AuthToken, UserResponse, UserData
from services.users import user_service
from starlette.responses import JSONResponse, Response

router = APIRouter()


@router.post(
    "/users/reg",
    tags=["Users"],
    response_model=UserResponse,
)
def register_user(data: Reg, response: Response):
    return user_service.register(data, response)


@router.post(
    "/users/auth",
    tags=["Users"],
    response_model=UserResponse,
)
def auth_user(data: Creds, response: Response):
    return user_service.authorization(data, response)


@router.post(
    "/users/auth_token",
    tags=["Users"],
    response_model=UserResponse,
)
def auth_token_user(data: AuthToken, response: Response):
    return user_service.authorization_token(data, response)


@router.get(
    "/users/get",
    tags=["Users"],
    status_code=200,
    response_model=None,
)
def get_users(access_token: str = Cookie(None)):
    return user_service.get_users(access_token)


@router.get(
    "/users/user_data",
    tags=["Users"],
    status_code=200,
    response_model=UserData,
)
def get_data_user(access_token: str = Cookie(None)):
    return user_service.get_data_user(access_token)


@router.post(
    "/users/reset_password_request",
    tags=["Users"],
    response_model=None,
)
def reset_password_request(data: EmailRequest):
    return user_service.reset_password_request(data)

@router.post(
    "/users/reset_password",
    tags=["Users"],
    response_model=None,
)
def reset_password(data: ResetPasswordRequest):
    return user_service.reset_password(data)


@router.patch(
    "/users/update_user",
    tags=["Users"],
    response_model=None,
)
def update_user(data: UpdateUser, access_token: str = Cookie(None)):
    return user_service.update_user(data, access_token)


# @router.websocket(
#     "/users/ws"
# )
# async def ws(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         print(data)
#         await websocket.send_text(data)
