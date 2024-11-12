import enum
import uuid

from database.database import Base
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from database.models.problem import *
from database.models.users import *

from typing import List

# class Daily_task(Base):
#     __tablename__ = "daily_task"
#
#     id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
#     title: Mapped[str]
#     short_desc: Mapped[str]
#     destination_id: Mapped[uuid.UUID]
#     number: Mapped[int]
#     is_complete: Mapped[bool]
#     user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

