import uuid

from starlette.responses import FileResponse

from schemas.education_material import CompleteEducation, ResponceGetAllTheme, ResponceGetAllMaterial
from services.education import education_service
from fastapi import Cookie, APIRouter, Query
from typing import List, Optional

router = APIRouter()


@router.get(
    "/education/get_all_theme",
    tags=["Education_material"],
    response_model=List[ResponceGetAllTheme],
)
def get_all_theme(access_token: str = Cookie(None)):
    return education_service.get_all_theme(access_token)


@router.get(
    "/education/get_all_education_material/{education_theme_id}",
    tags=["Education_material"],
    response_model=ResponceGetAllMaterial,
)
def get_all_education_material(education_theme_id, access_token: str = Cookie(None)):
    return education_service.get_all_education_material(education_theme_id, access_token)


@router.post(
    "/education/complete_education_material",
    tags=["Education_material"],
    response_model=None,
)
def complete_education_material(data: CompleteEducation, access_token: str = Cookie(None)):
    return education_service.complete_education_material(data, access_token)


@router.get(
    "/education/images/{filename}",
    tags=["Education_material"],
    response_model=None,
)
def get_images(filename: str, access_token: str = Cookie(None)):
    return FileResponse(f"database/images/{filename}")
