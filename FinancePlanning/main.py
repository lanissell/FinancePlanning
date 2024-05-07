from datetime import datetime

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

xml_repo_path = "C:\\MyWindows\\Projects\\FinancePlanning\\FinancePlanning\\xml"
json_repo_path = "C:\\MyWindows\\Projects\\FinancePlanning\\FinancePlanning\\JSON"


def TestRepositoryRun(users_repo, revenues_repo, revenues_categories_repo,
                      earnings_repo, earnings_categories_repo):

    users_repo.Add(User(
        object_id=0,
        name="A",
        surname="B"
    ))

    revenue_service = RevenuesService(revenues_repo, revenues_categories_repo)
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


if __name__ == '__main__':

    repoType = "json"

    if repoType == "xml":
        # region XML
        users_repo = XMLRepository("user", xml_repo_path, User)

        revenues_repo = XMLRepositoryParented("revenue", "user", xml_repo_path, Revenue)
        revenues_categories_repo = XMLRepository("revenueCategory", xml_repo_path, RevenueCategory)

        earnings_repo = XMLRepositoryParented("earning", "user", xml_repo_path, Earning)
        earnings_categories_repo = XMLRepository("earningSource", xml_repo_path, EarningSource)
        # endregion
    elif repoType == "json":
        # region XML
        users_repo = JSONRepository("user", json_repo_path, User)

        revenues_repo = JSONRepositoryParented("revenue", json_repo_path, Revenue)
        revenues_categories_repo = JSONRepository("revenueCategory", json_repo_path, RevenueCategory)

        earnings_repo = JSONRepositoryParented("earning", json_repo_path, Earning)
        earnings_categories_repo = JSONRepository("earningSource", json_repo_path, EarningSource)
        # endregion
    else:
        # region Table
        users_repo = TableRepository(User)

        revenues_repo = TableRepository(Revenue)
        revenues_categories_repo = TableRepository(RevenueCategory)

        earnings_repo = TableRepository(Earning)
        earnings_categories_repo = TableRepository(EarningSource)
        # endregion

    TestRepositoryRun(users_repo, revenues_repo, revenues_categories_repo, earnings_repo, earnings_categories_repo)
