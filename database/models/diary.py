import enum
import uuid

from database.database import Base
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from database.enum import DiaryType
import datetime

from database.models.mood_tracker import *

from typing import List

class FreeDiary(Base):
    __tablename__ = "free_diary"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    text: Mapped[str]
    created_at: Mapped[datetime.date]

    mood_tracker: Mapped[List["Mood_tracker"]] = relationship(cascade="all, delete-orphan")

class Diary_record(Base):
    __tablename__ = "diary_record"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    situation: Mapped[str]
    mood: Mapped[str]
    level: Mapped[int]
    auto_thought: Mapped[str]
    proofs: Mapped[str]
    refutations: Mapped[str]
    new_mood: Mapped[str]
    alternative_thought: Mapped[str]
    new_level: Mapped[int]
    behavioral: Mapped[str]
    created_at: Mapped[datetime.datetime]

    mood_tracker: Mapped[List["Mood_tracker"]] = relationship(cascade="all, delete-orphan")