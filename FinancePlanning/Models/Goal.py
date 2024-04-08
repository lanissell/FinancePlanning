from dataclasses import dataclass

from FinancePlanning.Models.DomainObject import DomainDataClass


@dataclass(frozen=True)
class Goal(DomainDataClass):
    user_id: int
    name: str
    price: float
    closed: bool

