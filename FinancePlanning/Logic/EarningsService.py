from datetime import datetime

from FinancePlanning.Models.Earning import Earning
from FinancePlanning.Models.EarningSource import EarningSource
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.RepositoryBase import RepositoryBase


class EarningsService:

    def __init__(self, earning_repository: RepositoryBase, earning_category_repository: RepositoryBase):
        self.earning_repository = earning_repository
        self.earning_category_repository = earning_category_repository

    def create_earning(self, user: User, price: float, category: EarningSource, date: datetime):

        if price <= 0 or date > datetime.now():
            return False

        revenues = self.earning_repository.GetAll()

        if len(revenues) > 0:
            last_id = revenues[-1].object_id + 1
        else:
            last_id = 0

        self.earning_repository.Add(Earning(last_id, user.object_id, price, category.object_id, str(date)))

        return True

    def get_earning_category_by_name(self, name):

        categories = self.earning_category_repository.GetAll()

        for revenue_category in categories:
            if revenue_category.name == name:
                return revenue_category

        if len(categories) > 0:
            last_id = categories[-1].object_id + 1
        else:
            last_id = 0

        new_revenue = EarningSource(last_id, name)
        self.earning_category_repository.Add(new_revenue)

        return new_revenue

