from abc import ABC, abstractmethod


class RepositoryBase(ABC):

    @abstractmethod
    def GetAll(self):
        pass

    @abstractmethod
    def GetById(self, id):
        pass

    @abstractmethod
    def Add(self, item):
        pass

    @abstractmethod
    def DeleteById(self, id):
        pass

    @abstractmethod
    def Update(self, item):
        pass
