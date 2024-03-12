from Models import EarningSource


class EarningSourceRepository:

    def __init__(self):
        self.sources: list[EarningSource] = []

    def GetAll(self):
        return self.sources

    def GetById(self, earning_source_id):
        return next(earning_source for earning_source in self.sources
                    if earning_source["earning_source_id"] == earning_source_id)

    def AddUser(self, earning_source: EarningSource):
        self.sources.append(earning_source)

    def DeleteUserById(self, category_id):
        self.sources.remove(self.GetById(category_id))

    def Update(self, earning_source_id, new_earning_source: EarningSource):
        for source in self.sources:
            if source["earning_source_id"] == earning_source_id:
                new_earning_source.id = earning_source_id
                source.update(new_earning_source)

