import uuid

from schemas.problem import CreateDeepConviction
from services.mood_tracker import mood_tracker_service
from schemas.mood_tracker import SaveMoodTracker, ResponseSaveTracker, ResponseGetTracker
from typing import List, Optional

from fastapi import Cookie, APIRouter

router = APIRouter()

@router.post(
    "/mood_tracker/save_mood_tracker",
    tags=["Mood_tracker"],
    response_model=ResponseSaveTracker,
)
def save_mood_tracker(data: SaveMoodTracker, access_token: str = Cookie(None)):
    return mood_tracker_service.save_mood_tracker(data, access_token)

@router.get(
    "/mood_tracker/get_all_mood_tracker",
    tags=["Mood_tracker"],
    response_model=List[ResponseGetTracker],
)
def get_all_mood_tracker(date: Optional[str] = None, access_token: str = Cookie(None)):
    return mood_tracker_service.get_all_mood_tracker(date, access_token)

# @router.get(
#     "/mood_tracker/get_all_mood_tracker_with_date",
#     tags=["Mood_tracker"],
#     response_model=List[ResponseGetTracker],
# )
# def get_all_mood_tracker_with_date(date, access_token: str = Cookie(None)):
#     return mood_tracker_service.get_all_mood_tracker_with_date(date, access_token)

@router.get(
    "/mood_tracker/get_mood_tracker/{mood_tracker_id}",
    tags=["Mood_tracker"],
    response_model=ResponseGetTracker,
)
def get_mood_tracker(mood_tracker_id: uuid.UUID, access_token: str = Cookie(None)):
    return mood_tracker_service.get_mood_tracker(mood_tracker_id, access_token)