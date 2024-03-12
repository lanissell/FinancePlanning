from FinancePlanning.Repositories.EarningRepository import EarningRepository
from FinancePlanning.Repositories.GoalRepository import GoalRepository
from FinancePlanning.Repositories.RevenueRepository import RevenueRepository


class User:

    def __init__(self, user_id, name, surname):
        self.user_id = user_id
        self.name = name
        self.surname = surname

    def get_user_earnings(self):
        user_earnings = list()
        earnings = EarningRepository().GetAll()

        for earning in earnings:
            if earning.user_id == self.user_id:
                user_earnings.append(earning)

        return user_earnings

    def get_user_revenues(self):
        user_revenues = list()
        revenues = RevenueRepository().GetAll()

        for revenue in revenues:
            if revenue.user_id == self.user_id:
                user_revenues.append(revenue)

        return user_revenues

    def get_user_goals(self):
        goals = GoalRepository().GetAll()
        user_goals = list()

        for goal in goals:
            if goal.user_id == self.user_id:
                user_goals.append(goal)

        return user_goals

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.user_id == other.user_id
