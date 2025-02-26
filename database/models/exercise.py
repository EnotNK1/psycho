import enum
import uuid
from typing import List

from database.database import Base
from sqlalchemy import ForeignKey, Enum, Column, String, Boolean, Text, TIMESTAMP, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from database.enum import FieldType
import datetime


class Exercise_structure(Base):
    __tablename__ = 'exercise_structure'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    picture_link: Mapped[str]
    linked_exercise_id: Mapped[uuid.UUID]
    closed: Mapped[bool]

    completed_exercise: Mapped[List["Сompleted_exercise"]] = relationship(
        cascade="all, delete-orphan")
    field: Mapped[List["Field"]] = relationship(cascade="all, delete-orphan")


class Сompleted_exercise(Base):
    __tablename__ = 'completed_exercise'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    date: Mapped[datetime.datetime]
    exercise_structure_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("exercise_structure.id",
                                                                        ondelete="CASCADE"))
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"))

    filled_field: Mapped[List["Filled_field"]] = relationship(
        cascade="all, delete-orphan")


class Field(Base):
    __tablename__ = 'field'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    title: Mapped[str]
    hint: Mapped[str]
    description: Mapped[str]
    type: Mapped[FieldType] = mapped_column(Enum(FieldType), nullable=True)
    major: Mapped[bool]
    exercise_structure_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("exercise_structure.id",
                                                                        ondelete="CASCADE"))

    variants: Mapped[List["Variant"]] = relationship(
        cascade="all, delete-orphan", back_populates="field"
    )

    filled_field: Mapped[List["Filled_field"]] = relationship(
        cascade="all, delete-orphan")


class Variant(Base):
    __tablename__ = 'variants'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    field_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("field.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)

    # Связь с таблицей field
    field: Mapped["Field"] = relationship(back_populates="variants")


class Filled_field(Base):
    __tablename__ = 'filled_field'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]

    field_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("field.id", ondelete="CASCADE"))
    completed_exercise_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("completed_exercise.id",
                                                                        ondelete="CASCADE"))
