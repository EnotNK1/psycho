from schemas.test import WritingRIDialog, ReadRIDialog
from services.dialog import dialog_service
from fastapi import Cookie, APIRouter

router = APIRouter()

@router.post(
    "/dialog/writing_r_i_dialog",
    tags=["Dialog"],
    response_model=None,
)
def writing_r_i_dialog(data: WritingRIDialog, access_token: str = Cookie(None)):
    return dialog_service.writing_r_i_dialog(data, access_token)

@router.post(
    "/dialog/reading_r_i_dialog",
    tags=["Dialog"],
    response_model=None,
)
def reading_r_i_dialog(data: ReadRIDialog, access_token: str = Cookie(None)):
    return dialog_service.reading_r_i_dialog(data, access_token)