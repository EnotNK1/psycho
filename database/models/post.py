import enum
import uuid

from database.database import Base
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from database.enum import DiaryType
import datetime

from typing import List

class Post_in_feed(Base):
    __tablename__ = "post_in_feed"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    like_score: Mapped[int]
    date: Mapped[datetime.datetime]

class Like(Base):
    __tablename__ = "like"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    post_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("post_in_feed.id", ondelete="CASCADE"))