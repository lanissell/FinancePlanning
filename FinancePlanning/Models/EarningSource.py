from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from FinancePlanning.Models.DomainObject import DomainObject


class EarningSource(DomainObject):
    __tablename__ = "earning_source"

    name: Mapped[str] = mapped_column(String(30))
