class Transaction:

    def __init__(self, date, price, category):
        self.date = date
        self.price = price
        self.category = category


class Earning(Transaction):
    pass


class Revenue(Transaction):
    pass
