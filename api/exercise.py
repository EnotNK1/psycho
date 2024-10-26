import uuid

from fastapi import APIRouter, Cookie, Depends
from schemas.review import ReviewCreate, ReviewRead
from services.exercise import exercise_service
from services.review import review_service
from starlette.responses import JSONResponse, Response

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