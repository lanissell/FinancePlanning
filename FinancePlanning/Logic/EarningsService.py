from datetime import datetime

from FinancePlanning.Models.Earning import Earning
from FinancePlanning.Models.EarningSource import EarningSource
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.EarningRepository import EarningRepository


class EarningsService:

    def __init__(self, earnings_repository: EarningRepository):
        self.earnings_repository = earnings_repository

    def create_earning(self, user: User, price: float, source: EarningSource, date: datetime):

        if price <= 0:
            pass

        if date > datetime.now():
            pass

        last_earning_id = self.earnings_repository.GetAll()[-1].earning_id

        self.earnings_repository.Add(Earning(last_earning_id + 1, user.user_id, price, source, date))

