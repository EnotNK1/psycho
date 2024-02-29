import uuid

from fastapi import APIRouter
from schemas.users import Creds, Reg
from services.users import user_service

router = APIRouter()

@router.post(
    "/users",
    response_model=None,
)
def register_user(data: Reg):
    return user_service.register(data)

@router.get(
    "/users",
    status_code=200,
    response_model=list,
)
def get_users():
    return user_service.get_users()