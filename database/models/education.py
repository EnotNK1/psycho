import enum
import uuid

from database.database import Base
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from database.enum import DiaryType
import datetime

from database.models.users import *

from typing import List

class Educational_theme(Base):
    __tablename__ = "educational_theme"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    theme: Mapped[str]
    link: Mapped[str]

    educational_material: Mapped[List["Educational_material"]] = relationship(cascade="all, delete-orphan")

class Educational_material(Base):
    __tablename__ = "educational_material"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]
    title: Mapped[str]
    type: Mapped[int]
    link_to_picture: Mapped[str] = mapped_column(nullable=True)
    educational_theme_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("educational_theme.id", ondelete="CASCADE"))

    educational_progress: Mapped[List["Educational_progress"]] = relationship(cascade="all, delete-orphan")

    # users: Mapped[List["Users"]] = relationship(back_populates="educational_material", secondary="educational_progress")

class Educational_progress(Base):
    __tablename__ = "educational_progress"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    educational_material_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("educational_material.id", ondelete="CASCADE"))