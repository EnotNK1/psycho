import enum
import uuid

from database.database import Base
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from database.models.problem import *
from database.models.users import *

from typing import List

class Test(Base):
    __tablename__ = "test"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    short_desc: Mapped[str]

    test_result: Mapped[List["Test_result"]] = relationship(cascade="all, delete-orphan")
    question: Mapped[List["Question"]] = relationship(cascade="all, delete-orphan")
    scale: Mapped[List["Scale"]] = relationship(cascade="all, delete-orphan")

class Test_result(Base):
    __tablename__ = "test_result"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    test_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("test.id", ondelete="CASCADE"))
    date: Mapped[datetime.datetime]

    scale_result: Mapped[List["Scale_result"]] = relationship(cascade="all, delete-orphan")

class Scale(Base):
    __tablename__ = "scale"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    title: Mapped[str]
    min: Mapped[int]
    max: Mapped[int]
    test_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("test.id", ondelete="CASCADE"))

    scale_result: Mapped[List["Scale_result"]] = relationship(cascade="all, delete-orphan")
    borders: Mapped[List["Borders"]] = relationship(cascade="all, delete-orphan")

class Scale_result(Base):
    __tablename__ = "scale_result"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    score: Mapped[float]
    scale_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("scale.id", ondelete="CASCADE"))
    test_result_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("test_result.id", ondelete="CASCADE"))

class Borders(Base):
    __tablename__ = "borders"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    left_border: Mapped[float]
    right_border: Mapped[float]
    color: Mapped[str]
    title: Mapped[str]
    user_recommendation: Mapped[str] = mapped_column(nullable=True)
    scale_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("scale.id", ondelete="CASCADE"))

class Question(Base):
    __tablename__ = "question"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]
    number: Mapped[int]
    test_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("test.id", ondelete="CASCADE"))

    answer_choice: Mapped[List["Answer_choice"]] = relationship(cascade="all, delete-orphan")

class Answer_choice(Base):
    __tablename__ = "answer_choice"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]
    question_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("question.id", ondelete="CASCADE"))
    score: Mapped[int]