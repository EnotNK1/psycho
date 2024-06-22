import datetime
from typing import List, Optional

import pydantic
import uuid


class ResScale(pydantic.BaseModel):
    scale_id: str
    score: int


class SaveTestRes(pydantic.BaseModel):
    test_id: str
    date: datetime.datetime
    results: List[ResScale]


class ReqBorder(pydantic.BaseModel):
    left_border: int
    right_border: int
    color: str
    title: str


class ReqScale(pydantic.BaseModel):
    title: str
    min: int
    max: int
    borders: List[ReqBorder]


class CreateTest(pydantic.BaseModel):
    title: str
    description: str
    short_desc: str
    scales: List[ReqScale]


class ResponseScale(pydantic.BaseModel):
    scale_id: uuid.UUID
    title: str
    min: int
    max: int
    borders: List[ReqBorder]


class GetTestInfo(pydantic.BaseModel):
    test_id: uuid.UUID
    title: str
    description: str
    short_desc: str
    scales: List[ResponseScale]


class GetTestRes(pydantic.BaseModel):
    test_id: str


class SendАpplication(pydantic.BaseModel):
    user_id: str
    text: str


class ResponseSendАpplication(pydantic.BaseModel):
    app_id: uuid.UUID
    client_id: uuid.UUID
    username: str
    text: str
    online: bool
    problem_id: None
    problem: None


class ConfirmApplication(pydantic.BaseModel):
    user_id: str
    status: bool

class ResponseGetClient(pydantic.BaseModel):
    username: str
    client_id: uuid.UUID
    birth_date: Optional[datetime.date] = None
    gender: str
    request: List[str]


class ResponseGetListClient(pydantic.BaseModel):
    username: str
    is_active: bool
    client_id: uuid.UUID
    request: List[str]

class WatchApplication(pydantic.BaseModel):
    app_id: str


class ResponseWatchApplication(pydantic.BaseModel):
    app_id: uuid.UUID
    client_id: uuid.UUID
    is_active: bool
    username: str
    birth_date: Optional[datetime.date] = None
    gender: str
    text: str


class WritingFreeDiary(pydantic.BaseModel):
    text: str


class ResponseReadingFreeDiary(pydantic.BaseModel):
    free_diary_id: uuid.UUID
    text: str

class WritingThinkDiary(pydantic.BaseModel):
    deep_conviction_id: str
    situation: str
    mood: str
    level: int
    auto_thought: str
    proofs: str
    refutations: str
    new_mood: str
    new_level: int
    behaviour: str


class ReadThinkDiary(pydantic.BaseModel):
    think_diary_id: str


class WritingRIDialog(pydantic.BaseModel):
    problem_id: uuid.UUID
    text: str
    type: bool


class ReadRIDialog(pydantic.BaseModel):
    problem_id: uuid.UUID

class GetPassTest(pydantic.BaseModel):
    user_id: uuid.UUID