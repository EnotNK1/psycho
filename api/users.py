import uuid

from fastapi import APIRouter, Cookie
from schemas.users import Creds, Reg, ResetPassword, AddProblem, SaveTestRes, CreateTest, GetTestRes, UpdateUser, \
    Psychologist, GetClient, SendАpplication, ConfirmApplication
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
    "/users/update_user",
    response_model=None,
)
def update_user(data: UpdateUser, access_token: str = Cookie(None)):
    return user_service.update_user(data, access_token)


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


@router.post(
    "/users/send_psychologist",
    response_model=None,
)
def psychologist_sent(data: Psychologist, access_token: str = Cookie(None)):
    return user_service.psychologist_sent(data, access_token)


@router.post(
    "/users/get_client",
    response_model=None,
)
def get_client(data: GetClient, access_token: str = Cookie(None)):
    return user_service.get_client(data, access_token)


@router.get(
    "/users/get_list_client",
    response_model=None,
)
def get_list_client(access_token: str = Cookie(None)):
    return user_service.get_list_client(access_token)

@router.post(
    "/users/send_application",
    response_model=None,
)
def send_application(data: SendАpplication, access_token: str = Cookie(None)):
    return user_service.send_application(data, access_token)


@router.post(
    "/users/confirm_application",
    response_model=None,
)
def confirm_application(data: ConfirmApplication, access_token: str = Cookie(None)):
    return user_service.confirm_application(data, access_token)

@router.post(
    "/users/get_psycholog",
    response_model=None,
)
def get_psycholog(data: GetClient, access_token: str = Cookie(None)):
    return user_service.get_psycholog(data, access_token)


@router.get(
    "/users/get_list_get_psycholog",
    response_model=None,
)
def get_list_get_psycholog(access_token: str = Cookie(None)):
    return user_service.get_list_psycholog(access_token)
