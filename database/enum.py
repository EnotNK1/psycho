import enum

class DiaryType(enum.Enum):
    FREE = 1
    THOUGHTS = 2

class FieldType(enum.Enum):
    TEXT = 1
    SLIDER = 2