from datetime import datetime

from FinancePlanning.Models.Earning import Earning
from FinancePlanning.Models.EarningSource import EarningSource
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.EarningRepository import EarningRepository


class EarningsService:

    @staticmethod
    def create_earning(user: User, price: float, source: EarningSource, date: datetime):

        if price <= 0:
            pass

        if date > datetime.now():
            pass

        repository = EarningRepository()
        last_earning_id = repository.GetAll()[-1].earning_id

        repository.Add(Earning(last_earning_id + 1, user.user_id, price, source, date))

