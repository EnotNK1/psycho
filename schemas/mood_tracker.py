import datetime
import enum
from database.enum import DiaryType
from typing import List, Optional

import pydantic
import uuid

class SaveMoodTracker(pydantic.BaseModel):
    score: int
    free_diary_id: Optional[uuid.UUID] = None
    think_diary_id: Optional[uuid.UUID] = None
    diary_type: Optional[DiaryType] = None
    class Config:
        use_enum_values = True

class ResponseSaveTracker(pydantic.BaseModel):
    mood_tracker_id: uuid.UUID

class ResponseGetTracker(pydantic.BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    score: int
    date: datetime.datetime
    free_diary_id: Optional[uuid.UUID] = None
    think_diary_id: Optional[uuid.UUID] = None
    diary_type: Optional[DiaryType] = None
    class Config:
        use_enum_values = True