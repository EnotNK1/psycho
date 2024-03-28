import uuid

from fastapi import APIRouter, Cookie
from schemas.users import Creds, Reg, ResetPassword, AddProblem, SaveTestRes, CreateTest, GetTestRes
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
    return user_service.authorization(data, response)


@router.get(
    "/users",
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
    "/users/new_problem",
    response_model=None,
)
def add_problem(data: AddProblem, access_token: str = Cookie(None)):
    return user_service.add_problem(data, access_token)

@router.post(
    "/users/save_test_result",
    response_model=None,
)
def save_test_result(data: SaveTestRes, access_token: str = Cookie(None)):
    return user_service.save_test_result(data, access_token)

@router.post(
    "/users/create_test",
    response_model=None,
)
def create_test(data: CreateTest, access_token: str = Cookie(None)):
    return user_service.create_test(data, access_token)

@router.post(
    "/users/get_test_result",
    response_model=None,
)
def get_test_res(data: GetTestRes, access_token: str = Cookie(None)):
    return user_service.get_test_res(data, access_token)
