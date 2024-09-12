from sqlalchemy import Enum, Float, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from entities.base_entity import BaseEntity
from datetime import datetime
from enums.workout_type_enum import WorkoutTypeEnum
from models.workout_model import WorkoutModel

class WorkoutEntity(BaseEntity):
    """Schema for the Workout table"""

    # Table name in SQLite
    __tablename__ = "workout"

    # Columns

    # Unique workout ID
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    # Name of the workout
    name: Mapped[str] = mapped_column(String)
    # Time the workout started
    start_time: Mapped[datetime] = mapped_column(DateTime)
    # Time the workout ended
    end_time: Mapped[datetime] = mapped_column(DateTime)
    # Workout notes
    notes: Mapped[str] = mapped_column(String)
    # Distance of workout
    distance: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    # Avg Heartrate during workout
    heartrate: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    # Workout type: long, recovery, speed, interval
    workout_type: Mapped[WorkoutTypeEnum] = mapped_column(Enum(WorkoutTypeEnum), nullable=False, default = WorkoutTypeEnum.BASE)

    @classmethod
    def from_model(cls, model: WorkoutModel):
        """Takes in Pydantic model, returns SQLAlchemy Entity"""
        return cls(
            id=model.id,
            name=model.name,
            start_time=model.start_time,
            end_time=model.end_time,
            notes=model.notes,
            distance=model.distance,
            heartrate=model.heartrate,
            workout_type=model.workout_type,
        )
    
    def to_model(self):
        """Takes in SQLAlchemy Entity, Returns Pydantic Model"""
        return WorkoutModel(
            id=self.id,
            name=self.name,
            start_time=self.start_time,
            end_time=self.end_time,
            notes=self.notes,
            distance=self.distance,
            heartrate=self.heartrate,
            workout_type=self.workout_type,
        )

