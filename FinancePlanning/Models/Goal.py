from dataclasses import dataclass

from FinancePlanning.Models.DomainObject import DomainParented


@dataclass(frozen=True)
class Goal(DomainParented):
    name: str
    price: float
    closed: bool

