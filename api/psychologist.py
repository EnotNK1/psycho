from schemas.test import ConfirmApplication
from schemas.users import Psychologist, GetClient
from services.psychologist import psychologist_service

from fastapi import Cookie, APIRouter

router = APIRouter()


@router.post(
    "/psychologist/send_psychologist",
    response_model=None,
)
def psychologist_sent(data: Psychologist, access_token: str = Cookie(None)):
    return psychologist_service.psychologist_sent(data, access_token)


@router.post(
    "/psychologist/get_client",
    response_model=None,
)
def get_client(data: GetClient, access_token: str = Cookie(None)):
    return psychologist_service.get_client(data, access_token)


@router.get(
    "/psychologist/get_list_client",
    response_model=None,
)
def get_list_client(access_token: str = Cookie(None)):
    return psychologist_service.get_list_client(access_token)


@router.post(
    "/psychologist/confirm_application",
    response_model=None,
)
def confirm_application(data: ConfirmApplication, access_token: str = Cookie(None)):
    return psychologist_service.confirm_application(data, access_token)


@router.post(
    "/client/get_psycholog",
    response_model=None,
)
def get_psycholog(data: GetClient, access_token: str = Cookie(None)):
    return psychologist_service.get_psycholog(data, access_token)


@router.get(
    "/client/get_list_get_psycholog",
    response_model=None,
)
def get_list_get_psycholog(access_token: str = Cookie(None)):
    return psychologist_service.get_list_psycholog(access_token)
