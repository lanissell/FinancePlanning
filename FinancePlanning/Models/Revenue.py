from dataclasses import dataclass
from datetime import datetime

from FinancePlanning.Models.RevenueCategory import RevenueCategory


@dataclass(frozen=True)
class Revenue:
    earning_id: int
    price: float
    category: RevenueCategory
    date: datetime
