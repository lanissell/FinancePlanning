from FinancePlanning.Models.RevenueCategory import RevenueCategory


class RevenueCategoryRepository:

    def __init__(self):
        self.categories: list[RevenueCategory] = []

    def GetAll(self):
        return self.categories

    def GetById(self, revenue_category_id):
        return next(category for category in self.categories if category["revenue_category_id"] == revenue_category_id)

    def AddUser(self, category: RevenueCategory):
        self.categories.append(category)

    def DeleteUserById(self, category_id):
        self.categories.remove(self.GetById(category_id))

    def Update(self, revenue_category_id, new_category: RevenueCategory):
        for category in self.categories:
            if category["revenue_category_id"] == revenue_category_id:
                new_category.id = revenue_category_id
                category.update(new_category)

