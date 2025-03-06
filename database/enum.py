import enum

class DiaryType(enum.Enum):
    FREE = 1
    THOUGHTS = 2

class FieldType(enum.Enum):
    TEXT = 1
    SLIDER = 2
    CHOICE = 3
    SELECTION = 4


class DailyTaskType(enum.Enum):
    THEORY = 1
    MOOD_TRACKER_AND_FREE_DIARY = 2
    TEST = 3
    OTHER = 4