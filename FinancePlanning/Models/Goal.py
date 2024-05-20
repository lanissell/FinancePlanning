from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, declared_attr, relationship

from FinancePlanning.Models.DomainObject import DomainObject
from FinancePlanning.Models.User import User


class Goal(DomainObject):
    __tablename__ = "goal"
    user_id: Mapped[int] = mapped_column(ForeignKey("user.object_id"))

    @declared_attr
    def user(self) -> Mapped["User"]:
        return relationship("User")

    name: Mapped[str] = mapped_column(String(30))
    price: Mapped[float] = mapped_column(Float())
    closed: bool

