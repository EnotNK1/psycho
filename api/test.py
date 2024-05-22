from schemas.test import SaveTestRes, CreateTest, GetTestRes
from services.test import test_service
from fastapi import Cookie, APIRouter

router = APIRouter()

@router.post(
    "/test/save_test_result",
    response_model=None,
)
def save_test_result(data: SaveTestRes, access_token: str = Cookie(None)):
    return test_service.save_test_result(data, access_token)


@router.post(
    "/test/create_test",
    response_model=None,
)
def create_test(data: CreateTest, access_token: str = Cookie(None)):
    return test_service.create_test(data, access_token)


@router.post(
    "/test/get_test_result",
    response_model=None,
)
def get_test_res(data: GetTestRes, access_token: str = Cookie(None)):
    return test_service.get_test_res(data, access_token)