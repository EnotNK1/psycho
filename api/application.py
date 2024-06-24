from schemas.test import SendАpplication, ConfirmApplication, ResponseSendАpplication, ResponseWatchApplication
from services.application import application_service

from fastapi import Cookie, APIRouter
from typing import List

router = APIRouter()


@router.get(
    "/application/get_list_applications",
    tags=["Application"],
    response_model=List[ResponseSendАpplication],
)
def get_list_applications(access_token: str = Cookie(None)):
    return application_service.get_list_applications(access_token)


@router.get(
    "/application/watch_application/{app_id}",
    tags=["Application"],
    response_model=ResponseWatchApplication,
)
def watch_application(app_id: str, access_token: str = Cookie(None)):
    return application_service.watch_application(app_id, access_token)


@router.post(
    "/client/send_application",
    tags=["Application"],
    response_model=str,
)
def send_application(data: SendАpplication, access_token: str = Cookie(None)):
    return application_service.send_application(data, access_token)


@router.post(
    "/psychologist/confirm_application",
    tags=["Application"],
    response_model=str,
)
def confirm_application(data: ConfirmApplication, access_token: str = Cookie(None)):
    return application_service.confirm_application(data, access_token)