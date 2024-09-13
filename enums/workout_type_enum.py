from enum import Enum

class WorkoutTypeEnum(str, Enum):
    RECOVERY = "recovery"
    LONG = "long"
    SPEED = "speed"
    INTERVAL = "interval"
    BASE = "base"
    