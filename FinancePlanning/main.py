from datetime import datetime

from sqlalchemy import create_engine

from FinancePlanning.Logic.EarningsService import EarningsService
from FinancePlanning.Logic.RevenuesService import RevenuesService
from FinancePlanning.Models.DomainObject import DomainObject
from FinancePlanning.Models.Earning import Earning
from FinancePlanning.Models.EarningSource import EarningSource
from FinancePlanning.Models.Revenue import Revenue
from FinancePlanning.Models.RevenueCategory import RevenueCategory
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.JSONRepository import JSONRepository
from FinancePlanning.Repositories.JSONRepositoryParented import JSONRepositoryParented
from FinancePlanning.Repositories.TableRepository import TableRepository
from FinancePlanning.Repositories.XMLRepository import XMLRepository
from FinancePlanning.Repositories.XMLRepositoryParented import XMLRepositoryParented
from FinancePlanning.UOF.FileUnitOfWork import FileUnitOfWork
from FinancePlanning.UOF.TableUnitOfWork import TableUnitOfWork

xml_repo_path = "C:\\MyWindows\\Projects\\FinancePlanning\\FinancePlanning\\xml"
json_repo_path = "C:\\MyWindows\\Projects\\FinancePlanning\\FinancePlanning\\JSON"


if __name__ == '__main__':
    pass