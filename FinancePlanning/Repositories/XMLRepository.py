import os
from lxml import etree as ET

from FinancePlanning.Repositories.RepositoryBase import RepositoryBase
from dicttoxml import dicttoxml
import xmltodict


class XMLRepository(RepositoryBase):

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def GetAll(self):
        root = self.GetXmlRoot()

        items = list()

        for child in root:
            items.append(xmltodict.parse(ET.tostring(child)))

        return items

    def GetById(self, id):
        items = self.GetAll()

        for item in items:
            if item[f"{self.name}"]['object_id']['#text'] == f"{id}":
                return item

    def Add(self, item):
        root = self.GetXmlRoot()

        itemDict = vars(item)
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

        self.DeleteById(item.id)
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
