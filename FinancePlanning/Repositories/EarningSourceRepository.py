from FinancePlanning.Models.EarningSource import EarningSource


class EarningSourceRepository:

    def __init__(self):
        self.sources: list[EarningSource] = []

    def GetAll(self):
        return self.sources

    def GetById(self, earning_source_id):
        return next(earning_source for earning_source in self.sources
                    if earning_source.earning_source_id == earning_source_id)

    def AddSource(self, earning_source: EarningSource):
        self.sources.append(earning_source)

    def DeleteSourceById(self, category_id):
        self.sources.remove(self.GetById(category_id))

    def Update(self, earning_source_id, new_name):
        index = 0
        for source in self.sources:
            if source.earning_source_id == earning_source_id:
                self.sources[index] = EarningSource(source.earning_source_id, new_name)
                pass
            index += 1


