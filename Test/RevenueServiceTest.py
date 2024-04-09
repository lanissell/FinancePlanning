import unittest
from datetime import datetime

from FinancePlanning.Logic.RevenuesService import RevenuesService
from FinancePlanning.Models.Earning import Earning
from FinancePlanning.Models.Revenue import Revenue
from FinancePlanning.Models.RevenueCategory import RevenueCategory
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.XMLRepository import XMLRepository
from Test.GoalServiceTest import remove_test_repo


class RevenueServiceTest(unittest.TestCase):

    PATH = "C:\\MyWindows\\Projects\\FinancePlanning\\FinancePlanning"

    def setUp(self):
        self.revenues = XMLRepository("revenuesTest", self.PATH, Revenue)
        self.earnings = XMLRepository("earningsTest", self.PATH, Earning)
        self.revenues_categories = XMLRepository("revenuesCategoriesTest", self.PATH, RevenueCategory)

        self.user = User(0, "Denis", "Belavin")

        self.revenue_service = RevenuesService(self.revenues, self.revenues_categories)

    def test_create_revenue_successfully(self):

        revenues_count = len(self.revenues.GetAll())

        self.revenue_service.create_revenue(self.user, 100,
                                            self.revenue_service.get_revenue_category_by_name("Shop").object_id,
                                            datetime.now())

        isRevenueAdded = len(self.revenues.GetAll()) == revenues_count + 1

        self.assertTrue(isRevenueAdded)

    def test_create_revenue_negative_price(self):

        revenues_count = len(self.revenues.GetAll())

        self.revenue_service.create_revenue(self.user, -100,
                                            self.revenue_service.get_revenue_category_by_name("Shop").object_id,
                                            datetime.now())

        isRevenueAdded = len(self.revenues.GetAll()) == revenues_count + 1

        self.assertFalse(isRevenueAdded)

    def test_create_revenue_future_date(self):

        revenues_count = len(self.revenues.GetAll())

        date = datetime(2050, 1, 1)

        self.revenue_service.create_revenue(self.user, 100,
                                            self.revenue_service.get_revenue_category_by_name("Shop").object_id,
                                            date)

        isRevenueAdded = len(self.revenues.GetAll()) == revenues_count + 1

        self.assertFalse(isRevenueAdded)

    def tearDown(self):
        remove_test_repo(self.revenues)
        remove_test_repo(self.earnings)
        remove_test_repo(self.revenues_categories)