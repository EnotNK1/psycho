import uuid

from fastapi import APIRouter, Cookie

from schemas.users import GetClient
from services.client import client_service

router = APIRouter()

@router.post(
    "/psychologist/get_client",
    response_model=None,
)
def get_client(data: GetClient, access_token: str = Cookie(None)):
    return client_service.get_client(data, access_token)


@router.get(
    "/psychologist/get_list_client",
    response_model=None,
)
def get_list_client(access_token: str = Cookie(None)):
    return client_service.get_list_client(access_token)