from schemas.users import Manager, GiveTask
from services.manager import manager_service
from fastapi import Cookie, APIRouter

router = APIRouter()


@router.post(
    "/manager/send_manager",
    tags=["Manager"],
    response_model=None,
)
def manager_send(data: Manager, access_token: str = Cookie(None)):
    return manager_service.manager_send(data, access_token)

@router.post(
    "/manager/give_task",
    tags=["Manager"],
    response_model=None,
)
def give_task(data: GiveTask, access_token: str = Cookie(None)):
    return manager_service.give_task(data, access_token)

