from Goal import Goal
from Earning import Earning
from Revenue import Revenue


class User:

    def __init__(self, user_id, name, surname, earnings: list[Earning], revenues: list[Revenue], goals: list[Goal]):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.earnings = earnings
        self.revenues = revenues
        self.goals = goals

    def add_earning(self, earning_id, price, earning_source, date):
        self.earnings.append(Earning(earning_id, price, earning_source, date))

    def add_revenue(self, revenue_id, price, revenue_category, date):
        self.revenues.append(Revenue(revenue_id, price, revenue_category, date))

    def add_goal(self, goal_id, name, price):
        self.goals.append(Goal(goal_id, name, price))
