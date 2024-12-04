import uuid

from fastapi import APIRouter, Cookie, Depends
from services.user_statistics import user_statistics_service
from starlette.responses import JSONResponse, Response

router = APIRouter()


@router.get(
    "/user_statistics/general_test_results/{psychologist_id}",
    tags=["User_statistics"],
    response_model=None,
)
def general_test_results(psychologist_id: uuid.UUID, access_token: str = Cookie(None)):
    return user_statistics_service.general_test_results(psychologist_id, access_token)




