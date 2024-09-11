"""Superclass for all entities, allows changing of all the application's entities"""
from sqlalchemy.orm import DeclarativeBase

class BaseEntity(DeclarativeBase):
    pass