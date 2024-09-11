
from fastapi import APIRouter


api = APIRouter(prefix = "/workouts")

@api.get("/")
def read_root():
    return {"Hello" : "world"}