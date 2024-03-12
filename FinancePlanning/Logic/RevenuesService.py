from datetime import datetime

from FinancePlanning.Models.Revenue import Revenue
from FinancePlanning.Models.RevenueCategory import RevenueCategory
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.RevenueCategoryRepository import RevenueCategoryRepository
from FinancePlanning.Repositories.RevenueRepository import RevenueRepository


class RevenueCategoryService:
    pass


class RevenuesService:

    @staticmethod
    def create_revenue(user: User, price: float, category: RevenueCategory, date: datetime):

        if price <= 0:
            pass

        if date > datetime.now():
            pass

        repository = RevenueRepository()
        last_revenue_id = repository.GetAll()[-1].earning_id

        repository.Add(Revenue(last_revenue_id + 1, user.user_id, price, category, date))

    @staticmethod
    def get_revenue_category_by_name(name):

        repository = RevenueCategoryRepository()
        categories = repository.GetAll()

        for revenue_category in categories:
            if revenue_category.name == name:
                return revenue_category

        last_id = categories[-1].revenue_category_id

        new_revenue = RevenueCategory(last_id, name)
        repository.Add(new_revenue)

        return new_revenue

