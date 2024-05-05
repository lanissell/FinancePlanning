from datetime import datetime

from FinancePlanning.Logic.EarningsService import EarningsService
from FinancePlanning.Logic.RevenuesService import RevenuesService
from FinancePlanning.Models.DomainObject import DomainObject
from FinancePlanning.Models.Earning import Earning
from FinancePlanning.Models.EarningSource import EarningSource
from FinancePlanning.Models.Revenue import Revenue
from FinancePlanning.Models.RevenueCategory import RevenueCategory
from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.TableRepository import TableRepository
from FinancePlanning.Repositories.XMLRepository import XMLRepositorys
from FinancePlanning.Repositories.XMLRepositoryParented import XMLRepositoryParented

PATH = "C:\\MyWindows\\Projects\\FinancePlanning\\FinancePlanning\\xml"

if __name__ == '__main__':
    # User
    #users_repo = XMLRepository("user", PATH, User)
    users_repo = TableRepository(User)

    users_repo.Add(User(
        object_id=0,
        name="A",
        surname="B"
    ))

    # Revenue
    #revenues_repo = XMLRepositoryParented("revenue", "user", PATH, Revenue)
    revenues_repo = TableRepository(Revenue)

    #revenues_categories_repo = XMLRepository("revenueCategory", PATH, RevenueCategory)
    revenues_categories_repo = TableRepository(RevenueCategory)

    revenue_service = RevenuesService(revenues_repo, revenues_categories_repo)

    # Earning
    #earnings_repo = XMLRepositoryParented("earning", "user", PATH, Earning)
    earnings_repo = TableRepository(Earning)

    #earnings_categories_repo = XMLRepository("earningSource", PATH, EarningSource)
    earnings_categories_repo = TableRepository(EarningSource)

    earning_service = EarningsService(earnings_repo, earnings_categories_repo)

    # Add revenues
    revenue_service.create_revenue(users_repo.GetById(0), 1000,
                                   revenue_service.get_revenue_category_by_name("Shop"),
                                   datetime.now())

    revenue_service.create_revenue(users_repo.GetById(0), 500,
                                   revenue_service.get_revenue_category_by_name("Taxi"),
                                   datetime.now())
    # Add earnings

    earning_service.create_earning(users_repo.GetById(0), 1000,
                                   earning_service.get_earning_category_by_name("Work"),
                                   datetime.now())

    earning_service.create_earning(users_repo.GetById(0), 500,
                                   earning_service.get_earning_category_by_name("Present"),
                                   datetime.now())
