from schemas.test import SaveTestRes, CreateTest, GetTestInfo, ResponseGetPassedTests, ResponseGetTestResult
from services.test import test_service
from fastapi import Cookie, APIRouter
from typing import List

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

@router.get(
    "/test/get_test_result/{test_id}",
    tags=["Test"],
    response_model=List[ResponseGetTestResult],
)
def get_test_res(test_id: str, access_token: str = Cookie(None)):
    return test_service.get_test_res(test_id, access_token)

@router.get(
    "/test/get_passed_tests/{user_id}",
    tags=["Test"],
    response_model=List[ResponseGetPassedTests],
)
def get_passed_tests(user_id: str, access_token: str = Cookie(None)):
    return test_service.get_passed_tests(user_id, access_token)

@router.get(
    "/test/get_all_tests",
    tags=["Test"],
    response_model=None,
)
def get_all_tests():
    return test_service.get_all_tests()

@router.get(
    "/test/get_test_info/{id}",
    tags=["Test"],
    response_model=GetTestInfo,
)
def get_test_info(id: str):
    return test_service.get_test_info(id)

