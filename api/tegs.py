from services.tegs import tegs_service

from fastapi import Cookie, APIRouter

router = APIRouter()


@router.get(
    "/tegs/get_list_tegs",
    response_model=None,
)
def get_list_tegs(access_token: str = Cookie(None)):
    return tegs_service.get_list_tegs(access_token)