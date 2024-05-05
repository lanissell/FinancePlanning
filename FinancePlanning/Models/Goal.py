from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column

from FinancePlanning.Models.DomainObject import DomainObject


class Goal(DomainObject):
    name: Mapped[str] = mapped_column(String(30))
    price: Mapped[float] = mapped_column(Float())
    closed: bool

