from dataclasses import dataclass
from datetime import datetime

from FinancePlanning.Models import EarningSource


@dataclass(frozen=True)
class Earning:
    earning_id: int
    user_id: int
    price: float
    source: EarningSource
    date: datetime

