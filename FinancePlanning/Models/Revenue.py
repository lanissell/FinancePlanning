from dataclasses import dataclass
from datetime import datetime

from FinancePlanning.Models.DomainObject import DomainDataClass
from FinancePlanning.Models.RevenueCategory import RevenueCategory


@dataclass(frozen=True)
class Revenue(DomainDataClass):
    earning_id: int
    user_id: int
    price: float
    category: RevenueCategory
    date: datetime
