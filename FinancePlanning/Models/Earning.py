from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped, declared_attr

from FinancePlanning.Models.DomainObject import DomainObject
from FinancePlanning.Models.EarningSource import EarningSource
from FinancePlanning.Models.User import User


class Earning(DomainObject):
    __tablename__ = "earning"

    price: Mapped[float] = mapped_column(Float())

    date: Mapped[str]

    user_id: Mapped[int] = mapped_column(ForeignKey("user.object_id"))

    @declared_attr
    def user(self) -> Mapped["User"]:
        return relationship("User")

    source_id: Mapped[int] = mapped_column(ForeignKey("earning_source.object_id"))

    @declared_attr
    def source(self) -> Mapped["EarningSource"]:
        return relationship("EarningSource")
