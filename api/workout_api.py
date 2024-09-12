from datetime import datetime
from fastapi import APIRouter, Depends
from enums.workout_type_enum import WorkoutTypeEnum
from models.workout_model import WorkoutModel
from services.workout_service import WorkoutService


api = APIRouter(prefix = "/workouts")

@api.get("")
def get_workouts(workout_type: WorkoutTypeEnum | None = None, 
                 min_distance: float | None = None, 
                 after_time: datetime | None = None,
                 workout_service: WorkoutService = Depends()
                 ) -> list[WorkoutModel]:
    """
    Gets workouts with optional filters

    Parameters:
        workout_type: Optional query parameter for filtering by type defined by WorkoutTypeEnum
        min_distance: Optional query parameter for filtering by a minimum distance
        after_time: Optional query parameter for filtering by workouts after a datetime
        workout_service: An injected workout service instance 

    Returns:
        list[WorkoutModel]: All workouts matching the filters
    """

    return workout_service.get_workouts(workout_type, min_distance, after_time)

@api.get("/{workout_id}")
def get_by_id(workout_id: int, workout_service: WorkoutService = Depends()) -> WorkoutModel:
    """
    Gets a workout by ID

    Parameters:
        workout_id: The ID of the workout to be retrieved
        workout_service: An injected workout service instance 

    Returns:
        WorkoutModel: the workout matching the id
    """

    return workout_service.get_by_id(workout_id)


@api.post("")
def new_workout(workout: WorkoutModel, workout_service: WorkoutService = Depends()) -> WorkoutModel:
    """
    Creates a workout

    Parameters:
        workout: The workout to be created
        workout_service: An injected workout service instance 

    Returns:
        WorkoutModel: the workout that was just created
    """

    return workout_service.create(workout)

@api.put("/{workout_id}")
def update_workout(workout_id :int, workout: WorkoutModel, workout_service: WorkoutService = Depends()) -> WorkoutModel:
    """
    Updates a workout by id

    Parameters:
        workout_id: The ID of the workout to be updated
        workout: The new information to update the workout with
        workout_service: An injected workout service instance 

    Returns:
        WorkoutModel: the updated workout
    """

    return workout_service.update(workout_id, workout)

@api.delete("/{workout_id}")
def delete_workout(workout_id :int, workout_service: WorkoutService = Depends()) -> None:
    """
    Deletes a workout by id

    Parameters:
        workout_id: The ID of the workout to be deleted
        workout_service: An injected workout service instance 

    Returns:
        None
    """

    workout_service.delete(workout_id)