from schemas.users import Psychologist
from services.psychologist import psychologist_service
from fastapi import Cookie, APIRouter

router = APIRouter()


@router.post(
    "/psychologist/send_psychologist",
    tags=["Psychologist"],
    response_model=None,
)
def psychologist_sent(data: Psychologist, access_token: str = Cookie(None)):
    return psychologist_service.psychologist_sent(data, access_token)


@router.get(
    "/client/get_psycholog/{psycholog_id}",
    tags=["Psychologist"],
    response_model=None,
)
def get_psycholog(psycholog_id: str, access_token: str = Cookie(None)):
    return psychologist_service.get_psycholog(psycholog_id, access_token)


# @router.get(
#     "/client/get_list_get_psycholog",
#     tags=["Psychologist"],
#     response_model=None,
# )
# def get_list_get_psycholog(access_token: str = Cookie(None)):
#     return psychologist_service.get_list_psycholog(access_token)

@router.get(
    "/client/get_all_psycholog",
    tags=["Psychologist"],
    response_model=None,
)
def get_all_psycholog(access_token: str = Cookie(None)):
    return psychologist_service.get_all_psycholog(access_token)
