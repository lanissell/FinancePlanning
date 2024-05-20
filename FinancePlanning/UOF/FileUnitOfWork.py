import os.path
import shutil

from FinancePlanning.Repositories.RepositoryBase import RepositoryBase
from FinancePlanning.UOF.UnityOfWorkBase import UnitOfWorkBase


class FileUnitOfWork(UnitOfWorkBase):

    def __init__(self, repository: RepositoryBase, filePath):
        self.batches = repository
        self.filePath = filePath
        self.copyPath = filePath + "Copy"
        self.fileExist = False

    def __enter__(self):
        if os.path.exists(self.filePath):
            shutil.copy(self.filePath, self.copyPath)

    def Commit(self):
        shutil.copy(self.filePath, self.copyPath)

    def Rollback(self):
        if os.path.exists(self.copyPath):
            shutil.copy(self.copyPath, self.filePath)
        else:
            os.remove(self.filePath)

    def __exit__(self, *args):
        super().__exit__(*args)

        if os.path.exists(self.copyPath):
            os.remove(self.copyPath)
