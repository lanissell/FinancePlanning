from datetime import datetime

from FinancePlanning.Logic.RevenuesService import RevenuesService
from FinancePlanning.Models.Goal import Goal
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.Redudant.UserRepository import UserRepository
from FinancePlanning.Repositories.RepositoryBase import RepositoryBase


class GoalService:

    def __init__(self, goal_repository: RepositoryBase, user_repository: RepositoryBase,
                 earnings_repository: RepositoryBase, revenues_repository: RepositoryBase,
                 revenues_service: RevenuesService):
        self.goal_repository = goal_repository
        self.user_repository = user_repository
        self.revenues_repository = revenues_repository
        self.earnings_repository = earnings_repository
        self.revenues_service = revenues_service

    def create_goal(self, user: User, name, price: float):

        if price <= 0:
            return False

        goals = self.goal_repository.GetAll()

        if len(goals) > 0:
            last_id = goals[-1].object_id + 1
        else:
            last_id = 0

        new_goal = Goal(last_id, user.object_id, name, price, False)
        self.goal_repository.Add(new_goal)

        return True

    def close_goal(self, goal: Goal):
        user = self.user_repository.GetById(goal.user_id)

        if user.get_user_balance(self.earnings_repository, self.revenues_repository) < goal.price:
            return False

        new_goal = Goal(goal.object_id, goal.user_id, goal.name, goal.price, True)
        self.goal_repository.Update(new_goal)

        self.revenues_service.create_revenue(user, goal.object_id,
                                             self.revenues_service.get_revenue_category_by_name("Goal"), datetime.now())

        return True
