from dataclasses import dataclass

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, registry

from FinancePlanning.Models.DomainObject import DomainObject
from FinancePlanning.Repositories.RepositoryBase import RepositoryBase

reg = registry()


class User(DomainObject):
    __tablename__ = "user"

    name: Mapped[str] = mapped_column(String(30))
    surname: Mapped[str] = mapped_column(String(30))

    def get_user_earnings(self, earningsRepo: RepositoryBase):
        user_earnings = list()
        earnings = earningsRepo.GetAll()

        for earning in earnings:
            if earning.user_id == self.object_id:
                user_earnings.append(earning)

        return user_earnings

    def get_user_revenues(self, revenuesRepo: RepositoryBase):
        user_revenues = list()
        revenues = revenuesRepo.GetAll()

        for revenue in revenues:
            if revenue.user_id == self.object_id:
                user_revenues.append(revenue)

        return user_revenues

    def get_user_goals(self, goalsRepo: RepositoryBase):
        goals = goalsRepo.GetAll()
        user_goals = list()

        for goal in goals:
            if goal.user_id == self.object_id:
                user_goals.append(goal)

        return user_goals

    def get_user_balance(self, earningsRepo: RepositoryBase,
                         revenuesRepo: RepositoryBase):

        balance = 0

        for earning in self.get_user_earnings(earningsRepo):
            balance += earning.price

        for revenue in self.get_user_revenues(revenuesRepo):
            balance -= revenue.price

        return balance

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return super().object_id == other.object_id
