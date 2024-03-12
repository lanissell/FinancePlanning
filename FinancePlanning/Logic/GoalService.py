from datetime import datetime

from FinancePlanning.Logic.RevenuesService import RevenuesService
from FinancePlanning.Models.Goal import Goal
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.GoalRepository import GoalRepository
from FinancePlanning.Repositories.UserRepository import UserRepository


class GoalService:

    @staticmethod
    def create_goal(user: User, name, price: float):

        if price <= 0:
            pass

        repository = GoalRepository()
        last_goal_id = repository.GetAll()[-1].earning_id

        repository.Add(Goal(last_goal_id + 1, user.user_id, name, price, False))

    @staticmethod
    def close_goal(goal: Goal):

        user_repository = UserRepository()
        goal_repository = GoalRepository()

        user = user_repository.GetById(goal.user_id)

        if user.get_user_balance() < goal.price:
            pass

        new_goal = Goal(goal.goal_id, goal.user_id, goal.name, goal.price, True)
        goal_repository.Update(goal.goal_id, new_goal)

        revenue_service = RevenuesService()

        revenue_service.create_revenue(user, goal.goal_id, RevenuesService.get_revenue_category_by_name("Goal"),
                                       datetime.now())



