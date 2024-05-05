import dataclasses
import os

from lxml import etree as ET

from FinancePlanning.Repositories.RepositoryBase import RepositoryBase
from dicttoxml import dicttoxml
import xmltodict


class XMLRepositoryParented(RepositoryBase):

    def __init__(self, name, parentName, path, valueType):
        self.name = name
        self.valueType = valueType
        self.parentName = parentName
        self.containerName = name + "s"
        self.parentPath = f"{path}\\{parentName}"

    def GetFullPath(self):
        return self.parentPath

    def GetAll(self):
        root = self.GetXmlRoot()

        items = list()

        for child in list(root.iter(self.name)):
            item = xmltodict.parse(ET.tostring(child))
            attrs = self.GetTypedDict(item[self.name])
            items.append(self.valueType(**attrs))

        return items

    def GetById(self, id):
        items = self.GetAll()

        for item in items:
            if item.object_id == id:
                return item

    def Add(self, item):
        root = self.GetXmlRoot()

        users = root.findall(self.parentName)
        selectedUser = None

        for user in users:
            user_id = user.findtext("object_id")
            if str(user_id) == str(item.user_id):
                selectedUser = user
                break

        if selectedUser is None:
            print("Parent user not found")
            return

        itemDict = dataclasses.asdict(item)
        itemXmlString = dicttoxml(itemDict, custom_root=self.name)
        itemXml = ET.fromstring(itemXmlString)

        container = selectedUser.find(self.containerName)
        if container is None:
            container = ET.Element(self.containerName)
            selectedUser.append(container)

        container.append(itemXml)
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

        if os.path.exists(self.parentPath):
            return ET.parse(self.parentPath).getroot()

        print("Parent xml not found")

    def Save(self, root):
        path = self.parentPath

        if os.path.exists(path):
            os.remove(path)

        file = os.open(path, os.O_RDWR | os.O_CREAT)
        ET.indent(root, space="\t")
        xmlString = ET.tostring(root, xml_declaration=True, pretty_print=True, method='xml')
        os.write(file, xmlString)
        os.close(file)

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
