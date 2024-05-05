from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, declared_attr

from FinancePlanning.Models.DomainObject import DomainObject
from FinancePlanning.Models.RevenueCategory import RevenueCategory
from FinancePlanning.Models.User import User


class Revenue(DomainObject):
    __tablename__ = "revenue"

    price: Mapped[float] = mapped_column(Float())
    date: Mapped[str] = mapped_column(String(30))

    user_id: Mapped[int] = mapped_column(ForeignKey("user.object_id"))

    @declared_attr
    def user(self) -> Mapped["User"]:
        return relationship("User")

    category_id: Mapped[int] = mapped_column(ForeignKey("revenue_category.object_id"))

    @declared_attr
    def category(self) -> Mapped["RevenueCategory"]:
        return relationship("RevenueCategory")
