import enum
import uuid

from database.database import Base
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from database.enum import DiaryType
import datetime

from database.models.users import *

from typing import List

class Problem(Base):
    __tablename__ = "problem"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    description: Mapped[str]
    goal: Mapped[str]
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    plan_point: Mapped[List["Plan_point"]] = relationship(cascade="all, delete-orphan")
    ladder_of_fear_rung: Mapped[List["Ladder_of_fear_rung"]] = relationship(cascade="all, delete-orphan")
    message_r_i_dialog: Mapped[List["Message_r_i_dialog"]] = relationship(cascade="all, delete-orphan")
    intermediate_belief: Mapped[List["Intermediate_belief"]] = relationship(cascade="all, delete-orphan")

class Deep_conviction(Base):
    __tablename__ = "deep_conviction"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    disadaptive: Mapped[str]
    adaptive: Mapped[str]
    problem_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("problem.id", ondelete="CASCADE"))

    intermediate_belief: Mapped[List["Intermediate_belief"]] = relationship(cascade="all, delete-orphan")

class Message_r_i_dialog(Base):
    __tablename__ = "message_r_i_dialog"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    is_rational: Mapped[bool]
    text: Mapped[str]
    date: Mapped[datetime.datetime]
    problem_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("problem.id", ondelete="CASCADE"))

class Intermediate_belief(Base):
    __tablename__ = "intermediate_belief"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(nullable=True)
    truthfulness: Mapped[str] = mapped_column(nullable=True)
    consistency: Mapped[str] = mapped_column(nullable=True)
    usefulness: Mapped[str] = mapped_column(nullable=True)
    feelings_and_actions: Mapped[str] = mapped_column(nullable=True)
    motivation: Mapped[str] = mapped_column(nullable=True)
    hindrances: Mapped[str] = mapped_column(nullable=True)
    incorrect_victims: Mapped[str] = mapped_column(nullable=True)
    results: Mapped[str] = mapped_column(nullable=True)
    problem_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("problem.id", ondelete="CASCADE"))
    deep_conviction: Mapped[uuid.UUID] = mapped_column(ForeignKey("deep_conviction.id", ondelete="CASCADE"), nullable=True)
    type: Mapped[int] = mapped_column(ForeignKey("type_analysis.id", ondelete="CASCADE"))

class Ladder_of_fear_rung(Base):
    __tablename__ = "ladder_of_fear_rung"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    problem_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("problem.id", ondelete="CASCADE"))
    number: Mapped[int]
    description: Mapped[str]

class Plan_point(Base):
    __tablename__ = "plan_point"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    problem_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("problem.id", ondelete="CASCADE"))
    description: Mapped[str]
    number: Mapped[int]
    term: Mapped[datetime.datetime]

    trouble: Mapped[List["Trouble"]] = relationship(cascade="all, delete-orphan")

class Trouble(Base):
    __tablename__ = "trouble"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    plan_point_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("plan_point.id", ondelete="CASCADE"))
    description: Mapped[str]
    strategy: Mapped[str]

class Type_analysis(Base):
    __tablename__ = "type_analysis"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]

    intermediate_belief: Mapped[List["Intermediate_belief"]] = relationship(cascade="all, delete-orphan")