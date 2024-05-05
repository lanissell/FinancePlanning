import dataclasses
import os

from dacite import from_dict
from lxml import etree as ET
from sqlalchemy.orm import Mapped

from FinancePlanning.Repositories.RepositoryBase import RepositoryBase
from dicttoxml import dicttoxml
import xmltodict

import sqlalchemy


class XMLRepository(RepositoryBase):

    def __init__(self, name, path, valueType):
        self.name = name
        self.path = path
        self.valueType = valueType

    def GetAll(self):
        root = self.GetXmlRoot()

        items = list()

        for child in root:
            item = xmltodict.parse(ET.tostring(child))
            attr = self.GetTypedDict(item[self.name])
            items.append(self.valueType(**attr))

        return items

    def GetById(self, id):
        items = self.GetAll()

        for item in items:
            if item.object_id == id:
                return item

    def Add(self, item):

        if self.GetById(item.object_id) is not None:
            return

        root = self.GetXmlRoot()

        itemDict = dataclasses.asdict(item)
        itemXmlString = dicttoxml(itemDict, custom_root=self.name)
        itemXml = ET.fromstring(itemXmlString)

        root.append(itemXml)
        self.Save(root)

    def DeleteById(self, id):

        root = self.GetXmlRoot()

        for item in root.iter(f"{self.name}"):

            if item[0].text == f"{id}":
                root.remove(item)
                self.Save(root)
                return

    def Update(self, item):

        self.DeleteById(item.object_id)
        self.Add(item)

    def GetXmlRoot(self):

        fullPath = self.GetFullPath()

        if os.path.exists(fullPath):
            return ET.parse(fullPath).getroot()

        root = ET.XML(f"<{self.name}s>"f"</{self.name}s>")

        return root

    def Save(self, root):
        path = self.GetFullPath()

        if os.path.exists(path):
            os.remove(path)

        file = os.open(path, os.O_RDWR | os.O_CREAT)
        ET.indent(root, space="\t")
        xmlString = ET.tostring(root, xml_declaration=True, pretty_print=True, method='xml')
        os.write(file, xmlString)
        os.close(file)

    def GetFullPath(self):
        return self.path + f"\\{self.name}"

    def GetTypedDict(self, xmlDict):

        newDict = xmlDict.copy()

        for key in xmlDict.keys():
            t = xmlDict[key].get("@type")

            if t is None:
                newDict.pop(key)
                continue

            valueType = eval(t)

            if valueType is dict:
                value = xmlDict[key]
                value.pop("@type")
                value = self.GetTypedDict(value)
            else:
                value = xmlDict[key]["#text"]

            if valueType is bool:
                newDict[key] = True if value == "true" else False
            else:
                newDict[key] = valueType(value)

        return newDict