import datetime
from typing import List

import pydantic
import uuid


class Creds(pydantic.BaseModel):
    email: str
    password: str


class Reg(pydantic.BaseModel):
    email: str
    username: str
    password: str
    confirm_password: str


class ResetPassword(pydantic.BaseModel):
    email: str


class AddProblem(pydantic.BaseModel):
    description: str
    goal: str


class UpdateUser(pydantic.BaseModel):
    birth_date: datetime.date
    gender: str
    username: str
    request: List[int]
    city: str
    description: str
    type: int


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


class Psychologist(pydantic.BaseModel):
    username: str
    title: str
    document: str
    description: str
    city: str
    online: bool
    face_to_face: bool
    gender: str
    birth_date: datetime.date
    request: List[int]


class GetClient(pydantic.BaseModel):
    user_id: str


class SendАpplication(pydantic.BaseModel):
    user_id: str
    text: str

class ConfirmApplication(pydantic.BaseModel):
    user_id: str
    status: bool

class ProblemAnalysisCreate(pydantic.BaseModel):
    problem_id: str
    type: int

class ProblemAnalysisGet(pydantic.BaseModel):
    problem_id: uuid.UUID

class CreateDeepConviction(pydantic.BaseModel):
    disadaptive: str
    adaptive: str
    problem_id: str

class BeliefAnalysis(pydantic.BaseModel):
    text: str
    feeling_and_actions: str
    motivation: str
    hindrances: str
    incorrect_victims: str
    results: str
    intermediate_conviction_id: str

class CheckBelief(pydantic.BaseModel):
    truthfulness: str
    consistency: str
    usefulness: str
    intermediate_conviction_id: str

class GetBeliefAnalysis(pydantic.BaseModel):
    intermediate_conviction_id: str

class WritingFreeDiary(pydantic.BaseModel):
    text: str

class WatchApplication(pydantic.BaseModel):
    app_id: str

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