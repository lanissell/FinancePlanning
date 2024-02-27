from Models import Category


class CategoryRepository:

    def __init__(self):
        self.categories: list[Category] = []

    def GetAll(self):
        return self.categories

    def GetById(self, category_id):
        return next(category for category in self.categories if category["category_id"] == category_id)

    def AddUser(self, category: Category):
        self.categories.append(category)

    def DeleteUserById(self, category_id):
        self.categories.remove(self.GetById(category_id))

    def Update(self, category_id, new_category: Category):
        for category in self.categories:
            if category["category_id"] == category_id:
                new_category.id = category_id
                category.update(new_category)


