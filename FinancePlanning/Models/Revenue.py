from dataclasses import dataclass

from FinancePlanning.Models.DomainObject import DomainFrozen


@dataclass(frozen=True)
class Revenue(DomainFrozen):
    user_id: int
    price: float
    category_id: int
    date: str
