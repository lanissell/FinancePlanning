from FinancePlanning.Repositories.EarningRepository import EarningRepository
from FinancePlanning.Repositories.GoalRepository import GoalRepository
from FinancePlanning.Repositories.RevenueRepository import RevenueRepository


class User:

    def __init__(self, user_id, name, surname, earnings: EarningRepository, revenues: RevenueRepository, goals: GoalRepository):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.earnings = earnings
        self.revenues = revenues
        self.goals = goals

    def get_user_earnings(self):
        user_earnings = list()
        earnings = self.earnings.GetAll()

        for earning in earnings:
            if earning.user_id == self.user_id:
                user_earnings.append(earning)

        return user_earnings

    def get_user_revenues(self):
        user_revenues = list()
        revenues = self.revenues.GetAll()

        for revenue in revenues:
            if revenue.user_id == self.user_id:
                user_revenues.append(revenue)

        return user_revenues

    def get_user_goals(self):
        goals = self.goals.GetAll()
        user_goals = list()

        for goal in goals:
            if goal.user_id == self.user_id:
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
            return self.user_id == other.user_id
