import abc

from FinancePlanning.Repositories.RepositoryBase import RepositoryBase


class UnitOfWorkBase(abc.ABC):
    batches: RepositoryBase

    @abc.abstractmethod
    def __enter__(self):
        raise NotImplemented

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Rollback()

    @abc.abstractmethod
    def Commit(self):
        raise NotImplemented

    @abc.abstractmethod
    def Rollback(self):
        raise NotImplemented
