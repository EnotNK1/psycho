from schemas.test import WritingRIDialog
from services.dialog import dialog_service
from fastapi import Cookie, APIRouter

router = APIRouter()

@router.post(
    "/dialog/writing_r_i_dialog",
    response_model=None,
)
def writing_r_i_dialog(data: WritingRIDialog, access_token: str = Cookie(None)):
    return dialog_service.writing_r_i_dialog(data, access_token)