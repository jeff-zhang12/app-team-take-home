from datetime import datetime
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import db_session
from enums.workout_type_enum import WorkoutTypeEnum
from models.workout_model import WorkoutModel
from entities.workout_entity import WorkoutEntity

class WorkoutService:
    """Performs all CRUD operations on workout table"""
    def __init__(self, session: Session = Depends(db_session)) -> None:
        self.db = session

    def get_workouts(self, workout_type: WorkoutTypeEnum | None = None, 
                     min_distance: float | None = None,
                     after_time: datetime | None = None
                     ) -> list[WorkoutModel]:
        """
        Gets workouts with optional filters

        Arguments:
            workout_type: Optional parameter for filtering query by type defined by WorkoutTypeEnum
            min_distance: Optional parameter for filtering query by a minimum distance
            after_time: Optional query parameter for filtering by workouts after a datetime
        Returns:
            list[WorkoutModel]: a list of workouts matching the filters
        """

        query = self.db.query(WorkoutEntity)

        if workout_type:
            query = query.filter(WorkoutEntity.workout_type == workout_type)
        if min_distance:
            if min_distance < 0:
                raise HTTPException(status_code=400, detail="Negative minimum distance")
            
            query = query.filter(WorkoutEntity.distance >= min_distance)
        if after_time:
            query = query.filter(WorkoutEntity.start_time > after_time)

        entity_list = query.all()
        

        return [entity.to_model() for entity in entity_list]

    def get_by_id(self, id: int) -> WorkoutEntity:
        """
        Gets a workout by id.

        Args:
            id: ID of the workout to retrieve.
        Returns:
            WorkoutEntity: the workout with matching id
        """
        workout_entity = self.db.query(WorkoutEntity).filter(WorkoutEntity.id == id).one_or_none()

        if workout_entity == None:
            raise HTTPException(status_code=404, detail="Workout not found")

       
        return workout_entity.to_model()

    def create(self, workout : WorkoutModel) -> WorkoutModel:
        """
        Create a workout

        Arguments: 
            workout: Pydantic workout to be added
        Returns:
            WorkoutModel: The workout just added to database
        """
        if workout.distance < 0:
            raise HTTPException(status_code=400, detail="Negative distance")
        if workout.heartrate < 0:
            raise HTTPException(status_code=400, detail="Negative heartrate")
        if workout.end_time < workout.start_time:
            raise HTTPException(status_code=400, detail="End time precedes start time")
        
        workout_ent = WorkoutEntity.from_model(workout)

        self.db.add(workout_ent)
        self.db.commit()

        return workout_ent.to_model()
    
    def update(self, id : int, workout : WorkoutEntity) -> WorkoutEntity:
        """
        Update a workout

        Arguments: 
            id: id of workout being updated for clarity
            workout: Pydantic workout with the updated details
        Returns:
            WorkoutModel: The edited workout
        """
        if workout.distance < 0:
            raise HTTPException(status_code=400, detail="Negative distance")
        if workout.heartrate < 0:
            raise HTTPException(status_code=400, detail="Negative heartrate")
        if workout.end_time < workout.start_time:
            raise HTTPException(status_code=400, detail="End time precedes start time")
        
        workout_entity = self.db.get(WorkoutEntity, id)

        if workout_entity == None:
            raise HTTPException(status_code=404, detail="Workout not found")

        workout_entity.name = workout.name
        workout_entity.start_time = workout.start_time
        workout_entity.end_time = workout.end_time
        workout_entity.notes = workout.notes
        workout_entity.distance = workout.distance
        workout_entity.heartrate = workout.heartrate
        workout_entity.workout_type = workout.workout_type

        self.db.commit()

        return workout_entity.to_model()
    
    def delete(self, id: int) -> None:
        """Deletes a room.

        Args:
            subject: a valid User model representing the currently logged in User
            id: ID of room to delete
        """


        workout_entity = self.db.get(WorkoutEntity, id)

        if workout_entity == None:
            raise HTTPException(status_code=404, detail="Workout not found")

        self.db.delete(workout_entity)
        self.db.commit()