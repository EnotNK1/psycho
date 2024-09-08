import enum
import uuid

from database.database import Base
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from database.enum import DiaryType
import datetime

from database.models.client import *
from database.models.diary import *
from database.models.education import *
from database.models.experiment import *
from database.models.inquiry import *
from database.models.mood_tracker import *
from database.models.post import *
from database.models.problem import *
from database.models.test import *

from typing import List

class Users(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    city: Mapped[str]
    company: Mapped[str] = mapped_column(nullable=True)
    online: Mapped[bool]
    face_to_face: Mapped[bool]
    gender: Mapped[str]
    birth_date: Mapped[datetime.date] = mapped_column(nullable=True)
    description: Mapped[str]
    role_id: Mapped[int]
    is_active: Mapped[bool]

    problem: Mapped[List["Problem"]] = relationship(cascade="all, delete-orphan")
    test_result: Mapped[List["Test_result"]] = relationship(cascade="all, delete-orphan")
    behavioral_experiment: Mapped[List["Behavioral_experiment"]] = relationship(cascade="all, delete-orphan")
    educational_progress: Mapped[List["Educational_progress"]] = relationship(cascade="all, delete-orphan")
    record: Mapped[List["Record"]] = relationship(cascade="all, delete-orphan")
    education: Mapped[List["Education"]] = relationship(cascade="all, delete-orphan")
    task: Mapped[List["Task"]] = relationship(cascade="all, delete-orphan")
    message: Mapped[List["Message"]] = relationship(cascade="all, delete-orphan")
    job_application: Mapped[List["Job_application"]] = relationship(cascade="all, delete-orphan")
    inquiry: Mapped[List["Inquiry"]] = relationship(back_populates="users", secondary="user_inquiries")
    post_in_feed: Mapped[List["Post_in_feed"]] = relationship(cascade="all, delete-orphan")
    like: Mapped[List["Like"]] = relationship(cascade="all, delete-orphan")
    token: Mapped["Token"] = relationship(cascade="all, delete-orphan")
    free_diary: Mapped[List["FreeDiary"]] = relationship(cascade="all, delete-orphan")
    think_diary: Mapped[List["Diary_record"]] = relationship(cascade="all, delete-orphan")
    mood_tracker: Mapped[List["Mood_tracker"]] = relationship(cascade="all, delete-orphan")

class Token(Base):
    __tablename__ = "token"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    token: Mapped[str]
    exp_date: Mapped[datetime.datetime]
    type: Mapped[str]

class Education(Base):
    __tablename__ = "education"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    title: Mapped[str]
    document: Mapped[str]
    psychologist_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

class Job_application(Base):
    __tablename__ = "job_application"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]
    psychologist_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    client_id: Mapped[uuid.UUID]
    status: Mapped[str]

class Message(Base):
    __tablename__ = "message"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]
    psychologist_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    client_id: Mapped[uuid.UUID]

#????????????
class Record(Base):
    __tablename__ = "record"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]
    date: Mapped[datetime.datetime]
    type: Mapped[str]
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))