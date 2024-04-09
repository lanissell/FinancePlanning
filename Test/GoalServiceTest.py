import os
import unittest
from datetime import datetime

from FinancePlanning.Logic.GoalService import GoalService
from FinancePlanning.Logic.RevenuesService import RevenuesService
from FinancePlanning.Models.Earning import Earning
from FinancePlanning.Models.Goal import Goal
from FinancePlanning.Models.Revenue import Revenue
from FinancePlanning.Models.RevenueCategory import RevenueCategory
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.XMLRepository import XMLRepository
from Test.TestUtils import remove_test_repo

class GoalServiceTest(unittest.TestCase):

    PATH = "C:\\MyWindows\\Projects\\FinancePlanning\\FinancePlanning"

    def setUp(self):
        self.revenues = XMLRepository("revenuesTest", self.PATH, Revenue)
        self.earnings = XMLRepository("earningsTest", self.PATH, Earning)
        self.goals = XMLRepository("goalsTest", self.PATH, Goal)
        self.revenuesCategories = XMLRepository("revenuesCategoriesTest", self.PATH, RevenueCategory)

        self.revenuesCategories.Add(RevenueCategory(0, "Salary"))

        self.earnings.Add(Earning(0, 0, 1000000, 0, str(datetime(2010, 1, 1))))

        self.user = User(0, "Denis", "Belavin")

        self.revenue_service = RevenuesService(self.revenues, self.revenuesCategories)

        self.user_repository = XMLRepository("user", self.PATH, User)
        self.user_repository.Add(self.user)

        self.goal_service = GoalService(self.goals, self.user_repository, self.earnings, self.revenues,
                                        self.revenue_service)

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
        self.goal_service.close_goal(self.user.get_user_goals(self.goals)[0])

        self.assertTrue(self.user.get_user_goals(self.goals)[0].closed)

    def test_close_goal_unsuccessfully(self):
        self.goal_service.create_goal(self.user, "Car", 10000000)
        self.goal_service.close_goal(self.user.get_user_goals(self.goals)[0])

        self.assertFalse(self.user.get_user_goals(self.goals)[0].closed)

    def tearDown(self):
        remove_test_repo(self.goals)
        remove_test_repo(self.revenues)
        remove_test_repo(self.revenuesCategories)
        remove_test_repo(self.earnings)
        remove_test_repo(self.user_repository)

