from FinancePlanning.Models.DomainObject import DomainObject
from FinancePlanning.Repositories.Redudant.EarningRepository import EarningRepository
from FinancePlanning.Repositories.Redudant.GoalRepository import GoalRepository
from FinancePlanning.Repositories.Redudant.RevenueRepository import RevenueRepository


class User(DomainObject):

    def __init__(self, object_id, name, surname, earningsRepo: EarningRepository, revenuesRepo: RevenueRepository, goalsRepo: GoalRepository):

        super().__init__(object_id)
        self.name = name
        self.surname = surname
        self.earningsRepo = earningsRepo
        self.revenuesRepo = revenuesRepo
        self.goalsRepo = goalsRepo

    def get_user_earnings(self):
        user_earnings = list()
        earnings = self.earningsRepo.GetAll()

        for earning in earnings:
            if earning.user_id == self.object_id:
                user_earnings.append(earning)

        return user_earnings

    def get_user_revenues(self):
        user_revenues = list()
        revenues = self.revenuesRepo.GetAll()

        for revenue in revenues:
            if revenue.user_id == self.object_id:
                user_revenues.append(revenue)

        return user_revenues

    def get_user_goals(self):
        goals = self.goalsRepo.GetAll()
        user_goals = list()

        for goal in goals:
            if goal.user_id == self.object_id:
                user_goals.append(goal)

        return user_goals

    def get_user_balance(self):

        balance = 0

        for earning in self.get_user_earnings():
            balance += earning.price

        for goal in self.get_user_goals():
            balance -= goal.price

        return balance

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return super().object_id == other.object_id
