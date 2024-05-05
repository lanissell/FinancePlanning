import unittest
from datetime import datetime

from FinancePlanning.Logic.RevenuesService import RevenuesService
from FinancePlanning.Models.Revenue import Revenue
from FinancePlanning.Models.RevenueCategory import RevenueCategory
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.XMLRepository import XMLRepository
from FinancePlanning.Repositories.XMLRepositoryParented import XMLRepositoryParented
from Test.GoalServiceTest import remove_test_repo


class RevenueServiceTest(unittest.TestCase):

    PATH = "C:\\MyWindows\\Projects\\FinancePlanning\\FinancePlanning"

    def setUp(self):
        self.revenues = XMLRepositoryParented("revenue", "user", self.PATH, Revenue)
        self.earnings = XMLRepositoryParented("earning", "user", self.PATH, Revenue)
        self.revenues_categories = XMLRepository("revenuesCategoriesTest", self.PATH, RevenueCategory)

        self.users_repo = XMLRepository("user", self.PATH, User)

        user = User(1, "Denis", "Belavin")
        self.users_repo.Add(user)

        self.revenue_service = RevenuesService(self.revenues, self.revenues_categories)

    def test_create_revenue_successfully(self):

        revenues_count = len(self.revenues.GetAll())

        user = self.users_repo.GetById(0)
        self.revenue_service.create_revenue(user, 100,
                                            self.revenue_service.get_revenue_category_by_name("Shop"),
                                            datetime.now())

        isRevenueAdded = len(self.revenues.GetAll()) == revenues_count + 1

        self.assertTrue(isRevenueAdded)

    def test_create_revenue_negative_price(self):

        revenues_count = len(self.revenues.GetAll())

        user = self.users_repo.GetById(0)
        self.revenue_service.create_revenue(user, -100,
                                            self.revenue_service.get_revenue_category_by_name("Shop"),
                                            datetime.now())

        isRevenueAdded = len(self.revenues.GetAll()) == revenues_count + 1

        self.assertFalse(isRevenueAdded)

    def test_create_revenue_future_date(self):

        revenues_count = len(self.revenues.GetAll())

        date = datetime(2050, 1, 1)

        user = self.users_repo.GetById(0)
        self.revenue_service.create_revenue(user, 100,
                                            self.revenue_service.get_revenue_category_by_name("Shop"),
                                            date)

        isRevenueAdded = len(self.revenues.GetAll()) == revenues_count + 1

        self.assertFalse(isRevenueAdded)

    def tearDown(self):
        pass
        # remove_test_repo(self.revenues)
        # remove_test_repo(self.earnings)
        # remove_test_repo(self.revenues_categories)
        # remove_test_repo(self.users_repo)
