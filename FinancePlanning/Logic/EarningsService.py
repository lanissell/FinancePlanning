from datetime import datetime

from FinancePlanning.Models.Earning import Earning
from FinancePlanning.Models.EarningSource import EarningSource
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.Redudant.EarningRepository import EarningRepository


class EarningsService:

    def __init__(self, earnings_repository: EarningRepository):
        self.earnings_repository = earnings_repository

    def create_earning(self, user: User, price: float, source: EarningSource, date: datetime):

        if price <= 0:
            return False

        if date > datetime.now():
            return False

        earnings = self.earnings_repository.GetAll()

        if len(earnings) > 0:
            last_id = earnings[-1].revenue_category_id + 1
        else:
            last_id = 0

        self.earnings_repository.Add(Earning(last_id, user.user_id, price, source, date))

