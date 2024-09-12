from database import engine
from entities.base_entity import BaseEntity
from entities.workout_entity import WorkoutEntity

BaseEntity.metadata.drop_all(engine)
BaseEntity.metadata.create_all(engine)


print("Demo Reset!")


