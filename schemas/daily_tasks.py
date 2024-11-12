import datetime
from typing import List, Optional
from typing import Union
from database.enum import FieldType
import pydantic
import uuid

class DailyTaskId(pydantic.BaseModel):
    daily_task_id: uuid.UUID