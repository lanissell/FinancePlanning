from dataclasses import dataclass

from FinancePlanning.Models.DomainObject import DomainParented


@dataclass(frozen=True)
class Earning (DomainParented):
    price: float
    source_id: int
    date: str

