from datetime import datetime

from FinancePlanning.Models.Revenue import Revenue
from FinancePlanning.Models.RevenueCategory import RevenueCategory
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.Redudant.RevenueCategoryRepository import RevenueCategoryRepository
from FinancePlanning.Repositories.Redudant.RevenueRepository import RevenueRepository


class RevenuesService:

    def __init__(self, revenue_repository: RevenueRepository, revenue_category_repository: RevenueCategoryRepository):
        self.revenue_repository = revenue_repository
        self.revenue_category_repository = revenue_category_repository

    def create_revenue(self, user: User, price: float, category: RevenueCategory, date: datetime):

        if price <= 0 or date > datetime.now():
            return False

        revenues = self.revenue_repository.GetAll()

        if len(revenues) > 0:
            last_id = revenues[-1].revenue_category_id + 1
        else:
            last_id = 0

        self.revenue_repository.Add(Revenue(last_id, user.user_id, price, category, date))

        return True

    def get_revenue_category_by_name(self, name):

        categories = self.revenue_category_repository.GetAll()

        for revenue_category in categories:
            if revenue_category.name == name:
                return revenue_category

        if len(categories) > 0:
            last_id = categories[-1].revenue_category_id
        else:
            last_id = 0

        new_revenue = RevenueCategory(last_id, name)
        self.revenue_category_repository.Add(new_revenue)

        return new_revenue

