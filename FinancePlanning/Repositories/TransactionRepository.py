from Models import Earning


class TransactionRepository:

    def __init__(self):
        self.transactions: list[Transaction] = []

    def GetAll(self):
        return self.transactions

    def GetById(self, transaction_id):
        return next(transaction for transaction in self.transactions if transaction["transaction_id"] == transaction_id)

    def AddUser(self, transaction: Transaction):
        self.transactions.append(transaction)

    def DeleteUserById(self, transaction_id):
        self.transactions.remove(self.GetById(transaction_id))

    def Update(self, transaction_id, new_transaction: Transaction):
        for transaction in self.transactions:
            if transaction["transaction_id"] == transaction_id:
                new_transaction.id = transaction_id
                transaction.update(new_transaction)
