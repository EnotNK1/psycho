import enum
import uuid

from database.database import Base
from sqlalchemy import ForeignKey, Enum, Column, String, Boolean, Text, TIMESTAMP, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from database.enum import DiaryType
import datetime


class Review(Base):
    __tablename__ = 'review'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]
    email: Mapped[str]
    is_read: Mapped[bool]
    created_at: Mapped[datetime.datetime]