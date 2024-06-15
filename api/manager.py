from schemas.users import Manager
from services.manager import manager_service
from fastapi import Cookie, APIRouter

router = APIRouter()


@router.post(
    "/manager/send_manager",
    response_model=None,
)
def manager_send(data: Manager, access_token: str = Cookie(None)):
    return manager_service.manager_send(data, access_token)
