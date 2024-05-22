import datetime
from typing import List

import pydantic
import uuid


class SaveTestRes(pydantic.BaseModel):
    title: str
    score: int
    test_id: str
    date: datetime.datetime


class CreateTest(pydantic.BaseModel):
    title: str
    description: str
    short_desc: str


class GetTestRes(pydantic.BaseModel):
    test_id: str


class SendАpplication(pydantic.BaseModel):
    user_id: str
    text: str


class ConfirmApplication(pydantic.BaseModel):
    user_id: str
    status: bool


class WatchApplication(pydantic.BaseModel):
    app_id: str


class WritingFreeDiary(pydantic.BaseModel):
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
