from dataclasses import dataclass

from FinancePlanning.Models.DomainObject import DomainFrozen


@dataclass(frozen=True)
class Earning (DomainFrozen):
    user_id: int
    price: float
    source_id: int
    date: str

