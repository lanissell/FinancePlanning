from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from FinancePlanning.Models.DomainObject import DomainObject
from FinancePlanning.Repositories.RepositoryBase import RepositoryBase


class TableRepository(RepositoryBase):

    def __init__(self, itemType: DomainObject):
        self.itemType = itemType
        self.engine = create_engine(f"sqlite:///database.db", echo=True)

    def GetAll(self):
        with Session(autoflush=False, bind=self.engine) as session:
            items = session.query(self.itemType).all()
            return items

    def GetById(self, object_id):
        with Session(autoflush=False, bind=self.engine) as session:
            item = session.query(self.itemType).filter(self.itemType.object_id == object_id).first()
            return item

    def Add(self, item):
        with Session(autoflush=False, bind=self.engine) as session:
            session.add(item)
            session.commit()

    def Update(self, item):
        self.DeleteById(item.object_id)
        self.Add(item)

    def DeleteById(self, object_id):
        with Session(autoflush=False, bind=self.engine) as session:
            item = session.query(self.itemType).filter(self.itemType.object_id == object_id).first()
            session.delete(item)
            session.commit()
