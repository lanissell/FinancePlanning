from dataclasses import dataclass

from FinancePlanning.Models.DomainObject import DomainDataClass


@dataclass(frozen=True)
class RevenueCategory(DomainDataClass):

    name: str