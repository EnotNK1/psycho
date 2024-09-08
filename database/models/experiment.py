from database.models.diary import *
from database.models.problem import *
from database.models.test import *

from typing import List

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