import uuid

from fastapi import APIRouter, Cookie

from schemas.users import GetClient
from schemas.test import ResponseGetClient, ResponseGetListClient
from services.client import client_service
from typing import List

router = APIRouter()

@router.post(
    "/psychologist/get_client",
    response_model=ResponseGetClient,
)
def get_client(data: GetClient, access_token: str = Cookie(None)):
    return client_service.get_client(data, access_token)


@router.get(
    "/psychologist/get_list_client",
    response_model=List[ResponseGetListClient],
)
def get_list_client(access_token: str = Cookie(None)):
    return client_service.get_list_client(access_token)

@router.post(
    "/client/get_tasks",
    response_model=None,
)
def get_tasks(access_token: str = Cookie(None)):
    return client_service.get_tasks(access_token)