import uuid

from schemas.test import SaveTestRes, CreateTest, GetTestInfo, ResponseGetPassedTests, ResponseGetTestResult, \
    SaveTestResult
from services.test import test_service
from fastapi import Cookie, APIRouter, Query
from typing import List, Optional

router = APIRouter()

@router.post(
    "/test/save_test_result",
    tags=["Test"],
    response_model=SaveTestResult,
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
    "/test/get_test_results/{test_id}",
    tags=["Test"],
    response_model=List[ResponseGetTestResult],
)
def get_test_results(test_id: str, access_token: str = Cookie(None), user_id: Optional[str] = Query(None)):
    return test_service.get_test_res(test_id, access_token, user_id)


@router.get(
    "/test/get_test_result/{test_result_id}",
    tags=["Test"],
    response_model=ResponseGetTestResult,
)
def get_test_result(test_result_id: str, access_token: str = Cookie(None)):
    return test_service.get_test_result(test_result_id, access_token)

@router.get(
    "/test/get_passed_tests/{user_id}",
    tags=["Test"],
    response_model=List[ResponseGetPassedTests],
)
def get_passed_tests(user_id: str, access_token: str = Cookie(None)):
    return test_service.get_passed_tests(user_id, access_token)

@router.get(
    "/test/get_passed_tests",
    tags=["Test"],
    response_model=List[ResponseGetPassedTests],
)
def get_passed_tests(access_token: str = Cookie(None)):
    return test_service.get_your_passed_tests(access_token)

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

@router.get(
    "/test/get_test_questions/{test_id}",
    tags=["Test"],
    response_model=None,
)
def get_test_questions(test_id: uuid.UUID, access_token: str = Cookie(None)):
    return test_service.get_test_questions(test_id, access_token)

@router.delete(
    "/test/delete_test",
    tags=["Test"],
    response_model=None,
)
def delete_test(test_id: uuid.UUID, access_token: str = Cookie(None)):
    return test_service.delete_test(test_id, access_token)

@router.post(
    "/test/auto_create",
    tags=["Test"],
    response_model=None,
)
def auto_create(access_token: str = Cookie(None)):
    return test_service.auto_create(access_token)

