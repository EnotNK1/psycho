import uuid

from fastapi import APIRouter, Cookie

from schemas.users import TaskId
from schemas.test import ResponseGetClient, ResponseGetListClient
from services.client import client_service
from typing import List

router = APIRouter()

@router.get(
    "/psychologist/get_client/{client_id}",
    tags=["Client"],
    response_model=ResponseGetClient,
)
def get_client(client_id: str, access_token: str = Cookie(None)):
    return client_service.get_client(client_id, access_token)


@router.get(
    "/psychologist/get_list_client",
    tags=["Client"],
    response_model=List[ResponseGetListClient],
)
def get_list_client(access_token: str = Cookie(None)):
    return client_service.get_list_client(access_token)

@router.get(
    "/client/get_tasks",
    tags=["Client"],
    response_model=None,
)
def get_tasks(access_token: str = Cookie(None)):
    return client_service.get_tasks(access_token)

@router.get(
    "/client/get_given_tasks",
    tags=["Client"],
    response_model=None,
)
def get_given_tasks(access_token: str = Cookie(None)):
    return client_service.get_given_tasks(access_token)

@router.post(
    "/client/complete_task",
    tags=["Client"],
    response_model=None,
)
def complete_task(data: TaskId, access_token: str = Cookie(None)):
    return client_service.complete_task(data, access_token)

@router.delete(
    "/client/delete_task",
    tags=["Client"],
    response_model=None,
)
def delete_task(data: TaskId, access_token: str = Cookie(None)):
    return client_service.delete_task(data, access_token)

@router.delete(
    "/client/delete_incorrect_tasks",
    tags=["Client"],
    response_model=None,
)
def delete_incorrect_tasks(access_token: str = Cookie(None)):
    return client_service.delete_incorrect_tasks(access_token)

@router.post(
    "/client/unfulfilled_task",
    tags=["Client"],
    response_model=None,
)
def unfulfilled_task(data: TaskId, access_token: str = Cookie(None)):
    return client_service.unfulfilled_task(data, access_token)

@router.get(
    "/client/get_your_psychologist",
    tags=["Client"],
    response_model=None,
)
def get_your_psychologist(access_token: str = Cookie(None)):
    return client_service.get_your_psychologist(access_token)