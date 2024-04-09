from dataclasses import dataclass

from FinancePlanning.Models.DomainObject import DomainFrozen


@dataclass(frozen=True)
class RevenueCategory(DomainFrozen):
    name: str