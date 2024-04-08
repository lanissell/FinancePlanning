from dataclasses import dataclass
from datetime import datetime

from FinancePlanning.Models import EarningSource
from FinancePlanning.Models.DomainObject import DomainDataClass


@dataclass(frozen=True)
class Earning (DomainDataClass):
    user_id: int
    price: float
    source: EarningSource
    date: datetime

