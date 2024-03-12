from FinancePlanning.Models.Earning import Earning


class EarningRepository:

    def __init__(self):
        self.earnings: list[Earning] = []

    def GetAll(self):
        return self.earnings

    def GetById(self, earning_source_id):
        return next(earning for earning in self.earnings
                    if earning.earning_id == earning_source_id)

    def Add(self, earning: Earning):
        self.earnings.append(earning)

    def DeleteById(self, earning_id):
        self.earnings.remove(self.GetById(earning_id))