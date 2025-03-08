from database.database import Base
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime
import uuid
from database.enum import DiaryType


class Mood_tracker(Base):
    __tablename__ = "mood_tracker"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    score: Mapped[int]
    date: Mapped[datetime.datetime]
    free_diary_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("free_diary.id", ondelete="CASCADE"), nullable=True)
    think_diary_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("diary_record.id", ondelete="CASCADE"), nullable=True)
    diary_type: Mapped[DiaryType] = mapped_column(Enum(DiaryType), nullable=True)