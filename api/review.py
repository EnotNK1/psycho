import uuid

from fastapi import APIRouter, Cookie, Depends
from schemas.review import ReviewCreate, ReviewRead
from services.review import review_service
from starlette.responses import JSONResponse, Response

router = APIRouter()


@router.post(
    "/review/create",
    tags=["Review"],
    response_model=str,
)
def create_review(data: ReviewCreate, access_token: str = Cookie(None)):
    return review_service.create_review(data, access_token)


@router.get(
    "/review/get",
    tags=["Review"],
    response_model=list[ReviewRead],
)
def get_reviews(access_token: str = Cookie(None)):
    return review_service.get_reviews(access_token)


@router.patch(
    "/review/read/{review_id}",
    tags=["Review"],
    response_model=str,
)
def mark_review_as_read(review_id: uuid.UUID, access_token: str = Cookie(None)):
    return review_service.mark_review_as_read(review_id, access_token)


@router.delete(
    "/review/delete/{review_id}",
    tags=["Review"],
    response_model=str,
)
def delete_review(review_id: uuid.UUID, access_token: str = Cookie(None)):
    return review_service.delete_review(review_id, access_token)