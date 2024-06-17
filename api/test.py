from schemas.test import SaveTestRes, CreateTest, GetTestRes, GetPassTest
from services.test import test_service
from fastapi import Cookie, APIRouter

router = APIRouter()

@router.post(
    "/test/save_test_result",
    tags=["Test"],
    response_model=None,
)
def save_test_result(data: SaveTestRes, access_token: str = Cookie(None)):
    return test_service.save_test_result(data, access_token)


@router.post(
    "/test/create_test",
    tags=["Test"],
    response_model=None,
)
def create_test(data: CreateTest, access_token: str = Cookie(None)):
    return test_service.create_test(data, access_token)


@router.post(
    "/test/get_test_result",
    tags=["Test"],
    response_model=None,
)
def get_test_res(data: GetTestRes, access_token: str = Cookie(None)):
    return test_service.get_test_res(data, access_token)

@router.post(
    "/test/get_passed_tests",
    tags=["Test"],
    response_model=None,
)
def get_passed_tests(data: GetPassTest, access_token: str = Cookie(None)):
    return test_service.get_passed_tests(data, access_token)

@router.get(
    "/test/get_all_tests",
    tags=["Test"],
    response_model=None,
)
def get_all_tests():
    return test_service.get_all_tests()