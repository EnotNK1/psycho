from schemas.test import WritingFreeDiary, WritingThinkDiary, ReadThinkDiary, ReadRIDialog
from services.diary import diary_service

from fastapi import Cookie, APIRouter

router = APIRouter()

@router.post(
    "/diary/writing_free_diary",
    response_model=None,
)
def writing_free_diary(data: WritingFreeDiary, access_token: str = Cookie(None)):
    return diary_service.writing_free_diary(data, access_token)

@router.get(
    "/diary/reading_free_diary",
    response_model=None,
)
def reading_free_diary(access_token: str = Cookie(None)):
    return diary_service.reading_free_diary(access_token)

@router.post(
    "/diary/writing_think_diary",
    response_model=None,
)
def writing_think_diary(data: WritingThinkDiary, access_token: str = Cookie(None)):
    return diary_service.writing_think_diary(data, access_token)

@router.post(
    "/diary/reading_think_diary",
    response_model=None,
)
def reading_think_diary(data: ReadThinkDiary, access_token: str = Cookie(None)):
    return diary_service.reading_think_diary(data, access_token)

@router.post(
    "/diary/reading_r_i_dialog",
    response_model=None,
)
def reading_r_i_dialog(data: ReadRIDialog, access_token: str = Cookie(None)):
    return diary_service.reading_r_i_dialog(data, access_token)