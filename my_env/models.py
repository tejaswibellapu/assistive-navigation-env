from pydantic import BaseModel
from typing import Optional, List


class Observation(BaseModel):
    description: str
    step_count: int
    history: List[str]


class Action(BaseModel):
    action: str


class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: Optional[dict] = {}