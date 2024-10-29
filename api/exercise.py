import uuid

from fastapi import APIRouter, Cookie, Depends
from schemas.exercise import SaveExerciseResult, ResponseGetExerciseResult, ResponseGetDetailExerciseResult, EditExerciseResult
from services.exercise import exercise_service
from database.models.exercise import Filled_field
from services.review import review_service
from starlette.responses import JSONResponse, Response
from typing import List, Optional

router = APIRouter()

@router.get(
    "/exercise/get_all_exercises",
    tags=["Exercise"],
    response_model=None,
)
def get_all_exercises(access_token: str = Cookie(None)):
    return exercise_service.get_all_exercises(access_token)

@router.get(
    "/exercise/get_exercise",
    tags=["Exercise"],
    response_model=None,
)
def get_exercise(exercise_id: uuid.UUID, access_token: str = Cookie(None)):
    return exercise_service.get_exercise(exercise_id, access_token)

@router.post(
    "/exercise/save_exercise_result",
    tags=["Exercise"],
    response_model=None,
)
def save_test_result(data: SaveExerciseResult, access_token: str = Cookie(None)):
    exercise_service.save_exercise_result(data, access_token)

@router.get(
    "/exercise/get_exercise_results/{exercise_id}",
    tags=["Exercise"],
    response_model=List[ResponseGetExerciseResult],
)
def get_exercise_results(exercise_id: str, access_token: str = Cookie(None)):
    return exercise_service.get_exercise_res(exercise_id, access_token)

@router.get(
    "/exercise/get_exercise_result/{completed_exercise_id}",
    tags=["Exercise"],
    response_model=ResponseGetDetailExerciseResult,
)
def get_exercise_results(completed_exercise_id: str, access_token: str = Cookie(None)):
    return exercise_service.get_completed_exercise_res(completed_exercise_id, access_token)

@router.delete(
    "/exercise/delete_exercise_result/{completed_exercise_id}",
    tags=["Exercise"],
    response_model=None,
)
def delete_exercise_result(completed_exercise_id: str, access_token: str = Cookie(None)):
    return exercise_service.delete_exercise_result(completed_exercise_id, access_token)

@router.patch(
    "/exercise/edit_exercise_result",
    tags=["Exercise"],
    response_model=None,
)
def edit_exercise_result(data: EditExerciseResult, access_token: str = Cookie(None)):
    return exercise_service.edit_exercise_result(data, access_token)




# @router.patch(
#     "/review/read/{review_id}",
#     tags=["Review"],
#     response_model=str,
# )
# def mark_review_as_read(review_id: uuid.UUID, access_token: str = Cookie(None)):
#     return review_service.mark_review_as_read(review_id, access_token)
#
#
# @router.delete(
#     "/review/delete/{review_id}",
#     tags=["Review"],
#     response_model=str,
# )
# def delete_review(review_id: uuid.UUID, access_token: str = Cookie(None)):
#     return review_service.delete_review(review_id, access_token)