import datetime

from schemas.test import WritingFreeDiary, WritingThinkDiary, ReadThinkDiary, ReadRIDialog, ResponseReadingFreeDiary, WritingFreeDiaryWithDate, ResponseDay
from services.diary import diary_service

from fastapi import Cookie, APIRouter
from typing import List


router = APIRouter()


@router.post(
    "/diary/writing_free_diary",
    tags=["Diary"],
    response_model=None,
)
def writing_free_diary(data: WritingFreeDiary, access_token: str = Cookie(None)):
    return diary_service.writing_free_diary(data, access_token)


@router.get(
    "/diary/reading_free_diary",
    tags=["Diary"],
    response_model=List[ResponseReadingFreeDiary],
)
def reading_free_diary(access_token: str = Cookie(None)):
    try:
        return diary_service.reading_free_diary(access_token)
    except:
        print("x")


@router.post(
    "/diary/writing_free_diary_with_date",
    tags=["Diary"],
    response_model=None,
)
def writing_free_diary_with_date(data: WritingFreeDiaryWithDate, access_token: str = Cookie(None)):
    return diary_service.writing_free_diary_with_date(data, access_token)


@router.get(
    "/diary/reading_free_diary_with_date",
    tags=["Diary"],
    response_model=List[ResponseReadingFreeDiary],
)
def reading_free_diary_with_date(date: datetime.date, access_token: str = Cookie(None)):
    return diary_service.reading_free_diary_with_date(access_token, date)


@router.get(
    "/diary/reading_free_diary_by_month",
    tags=["Diary"],
    response_model=List[ResponseDay],
)
def reading_free_diary_by_month(date: int, access_token: str = Cookie(None)):
    return diary_service.reading_free_diary_by_month(access_token, date)


@router.post(
    "/diary/writing_think_diary",
    tags=["Diary"],
    response_model=None,
)
def writing_think_diary(data: WritingThinkDiary, access_token: str = Cookie(None)):
    return diary_service.writing_think_diary(data, access_token)


@router.post(
    "/diary/reading_think_diary",
    tags=["Diary"],
    response_model=None,
)
def reading_think_diary(data: ReadThinkDiary, access_token: str = Cookie(None)):
    return diary_service.reading_think_diary(data, access_token)


@router.get(
    "/problem/get_all_think_diary/{user_id}",
    tags=["Diary"],
    response_model=None,
)
def get_all_think_diary(user_id: str, access_token: str = Cookie(None)):
    return diary_service.get_all_think_diary(user_id, access_token)
