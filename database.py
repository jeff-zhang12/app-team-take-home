from sqlalchemy import create_engine
from sqlalchemy.orm import Session

DATABASE_URL = "sqlite///./workout.db"

engine = create_engine(DATABASE_URL, echo = True )

def db_session():
    """Passes session to service methods"""
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()