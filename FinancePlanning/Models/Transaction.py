class Transaction:

    def __init__(self, transaction_id, price, category, date):
        self.transaction_id = transaction_id
        self.price = price
        self.category = category
        self.date = date


class Earning(Transaction):
    pass


class Revenue(Transaction):
    pass
