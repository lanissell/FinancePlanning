from dataclasses import dataclass


@dataclass(frozen=True)
class RevenueCategory:

    revenue_category_id: int
    name: str