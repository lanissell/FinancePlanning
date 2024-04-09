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

        repository = self.revenue_service.revenue_repository
        revenues_count = repository.GetAll().count()

        self.revenue_service.create_revenue(self.user, 100,
                                            self.revenue_service.get_revenue_category_by_name("Shop"), datetime.now())

        isRevenueAdded = repository.GetAll().count() == revenues_count + 1

        self.assertTrue(isRevenueAdded)

    def test_create_revenue_negative_price(self):

        repository = self.revenue_service.revenue_repository
        revenues_count = repository.GetAll().count()

        self.revenue_service.create_revenue(self.user, -100,
                                            self.revenue_service.get_revenue_category_by_name("Shop"), datetime.now())

        isRevenueAdded = repository.GetAll().count() == revenues_count + 1

        self.assertFalse(isRevenueAdded)

    def test_create_revenue_future_date(self):

        repository = self.revenue_service.revenue_repository
        revenues_count = repository.GetAll().count()

        date = datetime(2050, 1, 1)

        self.revenue_service.create_revenue(self.user, 100,
                                            self.revenue_service.get_revenue_category_by_name("Shop"), date)

        isRevenueAdded = repository.GetAll().count() == revenues_count + 1

        self.assertFalse(isRevenueAdded)
