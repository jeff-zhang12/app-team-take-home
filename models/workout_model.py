from pydantic import BaseModel
from datetime import datetime
from enums.workout_type_enum import WorkoutTypeEnum

class Workout(BaseModel):
    """Pydantic model to represent workout. Mirrors the WorkoutEntity"""
    id: int
    name: str
    start_time: datetime
    end_time: datetime
    notes: str
    distance: float
    heartrate: int
    workout_type: WorkoutTypeEnum 