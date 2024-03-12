from EarningSource import EarningSource


class Earning:

    def __init__(self, earning_id, price, earning_source: EarningSource, date):
        self.transaction_id = earning_id
        self.price = price
        self.source = earning_source
        self.date = date
