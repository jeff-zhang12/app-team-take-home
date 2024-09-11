from fastapi import FastAPI
from api import workout_api

app = FastAPI()

app.include_router(workout_api.api)

