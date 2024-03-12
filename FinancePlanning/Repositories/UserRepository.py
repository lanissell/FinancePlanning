from Models import User


class UserRepository:

    def __init__(self):
        self.users: list[User] = []

    def GetAll(self):
        return self.users

    def GetById(self, user_id):
        return next(user for user in self.users if user["user_id"] == user_id)

    def AddUser(self, user: User):
        self.users.append(user)

    def DeleteUserById(self, user_id):
        self.users.remove(self.GetById(user_id))

    def Update(self, user_id, new_user: User):
        for user in self.users:
            if user["user_id"] == user_id:
                new_user.id = user_id
                user.update(new_user)
