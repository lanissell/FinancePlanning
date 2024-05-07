import dataclasses
import os

from FinancePlanning.Repositories.RepositoryBase import RepositoryBase
from pathlib import Path
import json


class JSONRepository(RepositoryBase):
    def __init__(self, name, path, valueType):
        self.name = name
        self.path = path
        self.valueType = valueType
        self.key = f"{self.name}s"

    def GetAll(self):
        items = list()

        data = self.LoadData()

        for args in data:

            cleaned_args = args.copy()

            for key in args.keys():
                if type(cleaned_args[key]) is list:
                    cleaned_args.pop(key)
            items.append(self.valueType(**cleaned_args))

        return items

    def GetById(self, id):
        items = self.GetAll()

        for item in items:
            if item.object_id == id:
                return item

    def Add(self, item):

        if self.GetById(item.object_id) is not None:
            return

        data = self.LoadData()
        itemDict = dataclasses.asdict(item)
        data.append(itemDict)

        self.Save(data)

    def DeleteById(self, id):
        data = self.LoadData()
        for item in data:

            if item["object_id"] == id:
                data.remove(item)
                self.Save(data)
                return

    def Update(self, item):

        self.DeleteById(item.object_id)
        self.Add(item)

    def LoadData(self):
        path = Path(self.GetFullPath())

        if not path.exists():
            with open(path, "w") as f:
                f.write("{" + f'"{self.key}":[]' + "}")

        data = json.loads(path.read_text(encoding='utf-8'))

        return data[self.key]

    def Save(self, data):

        data = {self.key: data}

        path = Path(self.GetFullPath())
        path.write_text(json.dumps(data, indent=4), encoding='utf-8')

    def GetFullPath(self):
        return self.path + f"\\{self.name}.json"
