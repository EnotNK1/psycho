from schemas.test import WatchApplication, SendАpplication
from services.application import application_service

from fastapi import Cookie, APIRouter

router = APIRouter()


@router.get(
    "/application/get_list_applications",
    response_model=None,
)
def get_list_applications(access_token: str = Cookie(None)):
    return application_service.get_list_applications(access_token)


@router.post(
    "/application/watch_application",
    response_model=None,
)
def watch_application(data: WatchApplication, access_token: str = Cookie(None)):
    return application_service.watch_application(data, access_token)


@router.post(
    "/client/send_application",
    response_model=None,
)
def send_application(data: SendАpplication, access_token: str = Cookie(None)):
    return application_service.send_application(data, access_token)