from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from FinancePlanning.Models.DomainObject import DomainObject
from FinancePlanning.Repositories.TableRepository import TableRepository
from FinancePlanning.UOF.UnityOfWorkBase import UnitOfWorkBase


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(f"sqlite:///database.db", echo=True)
)


class TableUnitOfWork(UnitOfWorkBase):

    def __init__(self, itemType: DomainObject,
                 session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory
        self.itemType = itemType

    def __enter__(self):
        self.session = self.session_factory()
        self.batches = TableRepository(self.itemType, self.session)

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def Commit(self):
        self.session.commit()

    def Rollback(self):
        self.session.rollback()
