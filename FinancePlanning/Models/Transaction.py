class Transaction:

    def __init__(self, price, category, date):
        self.price = price
        self.category = category
        self.date = date


class Earning(Transaction):
    pass


class Revenue(Transaction):
    pass
