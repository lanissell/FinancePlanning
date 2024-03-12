import unittest
from datetime import datetime

from FinancePlanning.Logic.RevenuesService import RevenuesService
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.EarningRepository import EarningRepository
from FinancePlanning.Repositories.RevenueCategoryRepository import RevenueCategoryRepository
from FinancePlanning.Repositories.RevenueRepository import RevenueRepository


class RevenueServiceTest(unittest.TestCase):

    def setUp(self):
        revenues = RevenueRepository()
        earnings = EarningRepository()

        self.user = User(0, "Denis", "Belavin", earnings, revenues)

        self.revenue_service = RevenuesService(revenues, RevenueCategoryRepository())

    def test_create_revenue_successfully(self):

        result = self.revenue_service.create_revenue(self.user, 100,
                                            self.revenue_service.get_revenue_category_by_name("Shop"), datetime.now())

        self.assertTrue(result)

    def test_create_revenue_negative_price(self):

        result = self.revenue_service.create_revenue(self.user, -100,
                                            self.revenue_service.get_revenue_category_by_name("Shop"), datetime.now())

        self.assertFalse(result)

    def test_create_revenue_future_date(self):

        date = datetime(2050, 1, 1)

        result = self.revenue_service.create_revenue(self.user, 100,
                                            self.revenue_service.get_revenue_category_by_name("Shop"), date)

        self.assertFalse(result)
