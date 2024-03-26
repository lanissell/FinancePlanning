import unittest
from datetime import datetime

from FinancePlanning.Logic.GoalService import GoalService
from FinancePlanning.Logic.RevenuesService import RevenuesService
from FinancePlanning.Models.Earning import Earning
from FinancePlanning.Models.EarningSource import EarningSource
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.EarningRepository import EarningRepository
from FinancePlanning.Repositories.GoalRepository import GoalRepository
from FinancePlanning.Repositories.RevenueCategoryRepository import RevenueCategoryRepository
from FinancePlanning.Repositories.RevenueRepository import RevenueRepository
from FinancePlanning.Repositories.UserRepository import UserRepository


class GoalServiceTest(unittest.TestCase):

    def setUp(self):
        revenues = RevenueRepository()
        earnings = EarningRepository()
        goals = GoalRepository()

        earnings.Add(Earning(0, 0, 1000000, EarningSource(0, "Salary"), datetime(2010, 1, 1)))

        self.user = User(0, "Denis", "Belavin", earnings, revenues, goals)

        self.revenue_service = RevenuesService(RevenueRepository(), RevenueCategoryRepository())

        self.user_repository = UserRepository()
        self.user_repository.AddUser(self.user)

        self.goal_service = GoalService(goals, self.user_repository, self.revenue_service)

    def test_create_goal_successfully(self):
        repository = self.goal_service.goal_repository

        goals_count = repository.GetAll().count()

        self.goal_service.create_goal(self.user, "Car", 10000)

        isGoalAdded = repository.GetAll().count() == goals_count + 1

        self.assertTrue(isGoalAdded)

    def test_create_goal_with_negative_price(self):
        result = self.goal_service.create_goal(self.user, "Car", -10000)

        self.assertFalse(result)

    def test_close_goal_successfully(self):
        self.goal_service.create_goal(self.user, "Car", 10000)
        self.goal_service.close_goal(self.user.get_user_goals()[0])

        self.assertTrue(self.user.get_user_goals()[0].closed)

    def test_close_goal_unsuccessfully(self):
        self.goal_service.create_goal(self.user, "Car", 10000000)
        self.goal_service.close_goal(self.user.get_user_goals()[0])

        self.assertFalse(self.user.get_user_goals()[0].closed)
