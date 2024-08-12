import enum
import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime

from typing import List


class Base(DeclarativeBase):
    pass

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
    educational_material: Mapped[List["Educational_material"]] = relationship(back_populates="users", secondary="educational_progress")
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

class Token(Base):
    __tablename__ = "token"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    token: Mapped[str]
    exp_date: Mapped[datetime.datetime]
    type: Mapped[str]

class Problem(Base):
    __tablename__ = "problem"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    description: Mapped[str]
    goal: Mapped[str]
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    plan_point: Mapped[List["Plan_point"]] = relationship(cascade="all, delete-orphan")
    ladder_of_fear_rung: Mapped[List["Ladder_of_fear_rung"]] = relationship(cascade="all, delete-orphan")
    message_r_i_dialog: Mapped[List["Message_r_i_dialog"]] = relationship(cascade="all, delete-orphan")
    intermediate_belief: Mapped[List["Intermediate_belief"]] = relationship(cascade="all, delete-orphan")

class Deep_conviction(Base):
    __tablename__ = "deep_conviction"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    disadaptive: Mapped[str]
    adaptive: Mapped[str]
    problem_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("problem.id", ondelete="CASCADE"))

    intermediate_belief: Mapped[List["Intermediate_belief"]] = relationship(cascade="all, delete-orphan")


class Message_r_i_dialog(Base):
    __tablename__ = "message_r_i_dialog"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    is_rational: Mapped[bool]
    text: Mapped[str]
    date: Mapped[datetime.datetime]
    problem_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("problem.id", ondelete="CASCADE"))

class Intermediate_belief(Base):
    __tablename__ = "intermediate_belief"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(nullable=True)
    truthfulness: Mapped[str] = mapped_column(nullable=True)
    consistency: Mapped[str] = mapped_column(nullable=True)
    usefulness: Mapped[str] = mapped_column(nullable=True)
    feelings_and_actions: Mapped[str] = mapped_column(nullable=True)
    motivation: Mapped[str] = mapped_column(nullable=True)
    hindrances: Mapped[str] = mapped_column(nullable=True)
    incorrect_victims: Mapped[str] = mapped_column(nullable=True)
    results: Mapped[str] = mapped_column(nullable=True)
    problem_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("problem.id", ondelete="CASCADE"))
    deep_conviction: Mapped[uuid.UUID] = mapped_column(ForeignKey("deep_conviction.id", ondelete="CASCADE"), nullable=True)
    type: Mapped[int] = mapped_column(ForeignKey("type_analysis.id", ondelete="CASCADE"))

class Test_result(Base):
    __tablename__ = "test_result"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    test_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("test.id", ondelete="CASCADE"))
    date: Mapped[datetime.datetime]

    scale_result: Mapped[List["Scale_result"]] = relationship(cascade="all, delete-orphan")

class Scale(Base):
    __tablename__ = "scale"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    title: Mapped[str]
    min: Mapped[int]
    max: Mapped[int]
    test_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("test.id", ondelete="CASCADE"))

    scale_result: Mapped[List["Scale_result"]] = relationship(cascade="all, delete-orphan")
    borders: Mapped[List["Borders"]] = relationship(cascade="all, delete-orphan")

class Borders(Base):
    __tablename__ = "borders"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    left_border: Mapped[float]
    right_border: Mapped[float]
    color: Mapped[str]
    title: Mapped[str]
    scale_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("scale.id", ondelete="CASCADE"))

class Scale_result(Base):
    __tablename__ = "scale_result"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    score: Mapped[int]
    scale_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("scale.id", ondelete="CASCADE"))
    test_result_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("test_result.id", ondelete="CASCADE"))


class Test(Base):
    __tablename__ = "test"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    short_desc: Mapped[str]

    test_result: Mapped[List["Test_result"]] = relationship(cascade="all, delete-orphan")
    question: Mapped[List["Question"]] = relationship(cascade="all, delete-orphan")
    scale: Mapped[List["Scale"]] = relationship(cascade="all, delete-orphan")

class Question(Base):
    __tablename__ = "question"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]
    number: Mapped[int]
    test_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("test.id", ondelete="CASCADE"))

    answer_choice: Mapped[List["Answer_choice"]] = relationship(cascade="all, delete-orphan")

class Answer_choice(Base):
    __tablename__ = "answer_choice"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]
    question_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("question.id", ondelete="CASCADE"))
    score: Mapped[int]

class Behavioral_experiment(Base):
    __tablename__ = "behavioral_experiment"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    belief: Mapped[str]
    description: Mapped[str]
    difficulties: Mapped[str]
    strategies: Mapped[str]
    best_scenario: Mapped[str]
    best_scenario_probability: Mapped[str]
    worst_scenario: Mapped[str]
    worst_scenario_probability: Mapped[str]
    real_scenario: Mapped[str]
    real_scenario_probability: Mapped[str]
    alternative_belief: Mapped[str]
    alternative_belief_confidence: Mapped[str]
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    result_experiment: Mapped[List["Result_experiment"]] = relationship(cascade="all, delete-orphan")

class Result_experiment(Base):
    __tablename__ = "result_experiment"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    behavioral_experiment_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("behavioral_experiment.id", ondelete="CASCADE"))
    text: Mapped[str]
    emotion_before: Mapped[str]
    emotion_level_before: Mapped[int]
    emotion_after: Mapped[str]
    emotion_level_after: Mapped[int]

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

# class Goal(Base):
#     __tablename__ = "goal"
#
#     id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
#     description: Mapped[str]
#     user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
#
#     plan_point: Mapped[List["Plan_point"]] = relationship()
#     ladder_of_fear_rung: Mapped[List["Ladder_of_fear_rung"]] = relationship()

class Plan_point(Base):
    __tablename__ = "plan_point"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    problem_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("problem.id", ondelete="CASCADE"))
    description: Mapped[str]
    number: Mapped[int]
    term: Mapped[datetime.datetime]

    trouble: Mapped[List["Trouble"]] = relationship(cascade="all, delete-orphan")

class Ladder_of_fear_rung(Base):
    __tablename__ = "ladder_of_fear_rung"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    problem_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("problem.id", ondelete="CASCADE"))
    number: Mapped[int]
    description: Mapped[str]

class Trouble(Base):
    __tablename__ = "trouble"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    plan_point_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("plan_point.id", ondelete="CASCADE"))
    description: Mapped[str]
    strategy: Mapped[str]

class Educational_material(Base):
    __tablename__ = "educational_material"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]
    title: Mapped[str]
    theme: Mapped[str]
    type: Mapped[int]
    link: Mapped[str]

    users: Mapped[List["Users"]] = relationship(back_populates="educational_material", secondary="educational_progress")

class Educational_progress(Base):
    __tablename__ = "educational_progress"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    educational_material_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("educational_material.id", ondelete="CASCADE"), primary_key=True)

class Record(Base):
    __tablename__ = "record"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]
    date: Mapped[datetime.datetime]
    type: Mapped[str]
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

class Education(Base):
    __tablename__ = "education"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    title: Mapped[str]
    document: Mapped[str]
    psychologist_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

class Task(Base):
    __tablename__ = "task"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]
    test_title: Mapped[str] = mapped_column(nullable=True)
    test_id: Mapped[uuid.UUID] = mapped_column(nullable=True)
    psychologist_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    client_id: Mapped[uuid.UUID]
    is_complete: Mapped[bool]

class Message(Base):
    __tablename__ = "message"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]
    psychologist_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    client_id: Mapped[uuid.UUID]

class Job_application(Base):
    __tablename__ = "job_application"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    text: Mapped[str]
    psychologist_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    client_id: Mapped[uuid.UUID]
    status: Mapped[str]

class Inquiry(Base):
    __tablename__ = "inquiry"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]

    users: Mapped[List["Users"]] = relationship(back_populates="inquiry", secondary="user_inquiries")
    book: Mapped[List["Book"]] = relationship(back_populates="inquiry", secondary="inquiry_to_book")

class Type_analysis(Base):
    __tablename__ = "type_analysis"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]

    intermediate_belief: Mapped[List["Intermediate_belief"]] = relationship(cascade="all, delete-orphan")

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


class Clients(Base):
    __tablename__ = "clients"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    client_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    psychologist_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    text: Mapped[str]
    status: Mapped[bool]


class FreeDiary(Base):
    __tablename__ = "free_diary"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    text: Mapped[str]