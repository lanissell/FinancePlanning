from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from FinancePlanning.Models.DomainObject import DomainObject


class RevenueCategory(DomainObject):
    __tablename__ = "revenue_category"

    name: Mapped[str] = mapped_column(String(30))
