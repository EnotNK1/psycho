from sqlalchemy import Table, Column, UUID, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    verified: Mapped[bool]
    gender: Mapped[bool]
    description: Mapped[str]
    active: Mapped[bool]
    role_id: Mapped[int]