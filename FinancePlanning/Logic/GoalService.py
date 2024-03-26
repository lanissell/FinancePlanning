from datetime import datetime

from FinancePlanning.Logic.RevenuesService import RevenuesService
from FinancePlanning.Models.Goal import Goal
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.GoalRepository import GoalRepository
from FinancePlanning.Repositories.UserRepository import UserRepository


class GoalService:

    def __init__(self, goal_repository: GoalRepository, user_repository: UserRepository,
                 revenues_service: RevenuesService):
        self.goal_repository = goal_repository
        self.user_repository = user_repository
        self.revenues_service = revenues_service

    def create_goal(self, user: User, name, price: float):

        if price <= 0:
            return False

        goals = self.goal_repository.GetAll()

        if len(goals) > 0:
            last_id = goals[-1].goal_id + 1
        else:
            last_id = 0

        self.goal_repository.Add(Goal(last_id, user.user_id, name, price, False))

        return True

    def close_goal(self, goal: Goal):
        user = self.user_repository.GetById(goal.user_id)

        if user.get_user_balance() < goal.price:
            return False

        new_goal = Goal(goal.goal_id, goal.user_id, goal.name, goal.price, True)
        self.goal_repository.Update(goal.goal_id, new_goal)

        self.revenues_service.create_revenue(user, goal.goal_id,
                                             self.revenues_service.get_revenue_category_by_name("Goal"), datetime.now())

        return True
