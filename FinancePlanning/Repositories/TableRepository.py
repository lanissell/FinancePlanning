from FinancePlanning.Models.DomainObject import DomainObject
from FinancePlanning.Repositories.RepositoryBase import RepositoryBase


class TableRepository(RepositoryBase):

    def __init__(self, itemType: DomainObject, session):
        self.itemType = itemType
        self.session = session

    def GetAll(self):
        with self.session as session:
            items = session.query(self.itemType).all()
            return items

    def GetById(self, object_id):
        item = self.session.query(self.itemType).filter(self.itemType.object_id == object_id).first()
        return item

    def Add(self, item):
        self.session.add(item)

    def Update(self, item):
        self.DeleteById(item.object_id)
        self.Add(item)

    def DeleteById(self, object_id):
        item = self.session.query(self.itemType).filter(self.itemType.object_id == object_id).first()
        self.session.delete(item)
