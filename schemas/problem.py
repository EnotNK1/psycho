import datetime
from typing import List

import pydantic
import uuid


class AddProblem(pydantic.BaseModel):
    description: str
    goal: str


class ProblemAnalysisCreate(pydantic.BaseModel):
    problem_id: str
    type: int


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
