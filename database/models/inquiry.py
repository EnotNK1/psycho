from database.models.diary import *
from database.models.problem import *

from typing import List

class Inquiry(Base):
    __tablename__ = "inquiry"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]

    users: Mapped[List["Users"]] = relationship(back_populates="inquiry", secondary="user_inquiries")
    book: Mapped[List["Book"]] = relationship(back_populates="inquiry", secondary="inquiry_to_book")

class User_inquiries(Base):
    __tablename__ = "user_inquiries"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    inquiry_id: Mapped[int] = mapped_column(ForeignKey("inquiry.id", ondelete="CASCADE"), primary_key=True)
    type: Mapped[int]

class Book(Base):
    __tablename__ = "book"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    description: Mapped[str]
    link: Mapped[str]

    inquiry: Mapped[List["Inquiry"]] = relationship(back_populates="book", secondary="inquiry_to_book")

class Inquiry_to_book(Base):
    __tablename__ = "inquiry_to_book"

    book_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("book.id", ondelete="CASCADE"), primary_key=True)
    inquiry_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("inquiry.id", ondelete="CASCADE"), primary_key=True)