from dataclasses import dataclass

from FinancePlanning.Models.DomainObject import DomainFrozen


@dataclass(frozen=True)
class Goal(DomainFrozen):
    user_id: int
    name: str
    price: float
    closed: bool

