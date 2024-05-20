import dataclasses
import os

from FinancePlanning.Repositories.RepositoryBase import RepositoryBase
from pathlib import Path
import json


class JSONRepositoryParented(RepositoryBase):
    def __init__(self, name, path, valueType):
        self.name = name
        self.parentName = "user"
        self.path = path
        self.valueType = valueType
        self.key = f"{self.name}s"
        self.parentKey = f"{self.parentName}s"

    def GetAll(self):
        items = list()

        data = self._LoadData()

        for user in data:

            itemsDicts = user.get(self.key)
            if itemsDicts is None:
                continue

            for args in itemsDicts:
                items.append(self.valueType(**args))

        return items

    def GetById(self, id):
        items = self.GetAll()

        for item in items:
            if item.object_id == id:
                return item

    def Add(self, item):

        if self.GetById(item.object_id) is not None:
            return

        data = self._LoadData()
        itemDict = dataclasses.asdict(item)

        for user in data:
            if user["object_id"] != item.user_id:
                continue
            data[data.index(user)] = self._AddInParent(user, itemDict)
            break

        self._Save(data)

    def DeleteById(self, id):
        data = self._LoadData()
        for user in data:
            if self.key not in user:
                continue

            items = list(user[self.key])
            for item in user[self.key]:
                if item["object_id"] != id:
                    continue
                items.remove(item)
            user[self.key] = items
            break

        self._Save(data)

    def Update(self, item):

        self.DeleteById(item.object_id)
        self.Add(item)

    def _LoadData(self):
        path = Path(self._GetFullPath())

        if not path.exists():
            print("Parent not found!")
            return

        data = json.loads(path.read_text(encoding='utf-8'))

        return data[self.parentKey]

    def _AddInParent(self, parentDict, itemDict):

        if self.key not in parentDict:
            parentDict[self.key] = []

        parentDict[self.key].append(itemDict)

        return parentDict

    def _Save(self, data):

        data = {self.parentKey: data}

        path = Path(self._GetFullPath())
        path.write_text(json.dumps(data, indent=4), encoding='utf-8')

    def _GetFullPath(self):
        return self.path + f"\\{self.parentName}.json"
