from dataclasses import dataclass

from FinancePlanning.Models.DomainObject import DomainParented
from FinancePlanning.Models.RevenueCategory import RevenueCategory


@dataclass(frozen=True)
class Revenue(DomainParented):
    price: float
    category: RevenueCategory
    date: str
