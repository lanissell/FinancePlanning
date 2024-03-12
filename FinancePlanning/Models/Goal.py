from dataclasses import dataclass


@dataclass(frozen=True)
class Goal:

    goal_id: int
    user_id: int
    name: str
    price: float

