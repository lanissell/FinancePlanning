from FinancePlanning.Models.Revenue import Revenue


class RevenueRepository:

    def __init__(self):
        self.revenues: list[Revenue] = []

    def GetAll(self):
        return self.revenues

    def GetById(self, revenue_id):
        return next(revenue for revenue in self.revenues
                    if revenue.earning_id == revenue_id)

    def Add(self, revenue: Revenue):
        self.revenues.append(revenue)

    def DeleteById(self, revenue_id):
        self.revenues.remove(self.GetById(revenue_id))
