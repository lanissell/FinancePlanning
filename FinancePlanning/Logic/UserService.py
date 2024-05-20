from FinancePlanning.Models.User import User
from FinancePlanning.UOF.UnityOfWorkBase import UnitOfWorkBase


class UserService:

    def __init__(self, user_uof: UnitOfWorkBase):
        self.uof = user_uof

    def add_user(self, name, surname):

        with self.uof:
            users = self.uof.batches.GetAll()
            if len(users) > 0:
                last_id = users[-1].object_id + 1
            else:
                last_id = 0

            user = User(
                object_id=last_id,
                name=name,
                surname=surname
            )

            self.uof.batches.Add(user)
            self.uof.Commit()

            return user
