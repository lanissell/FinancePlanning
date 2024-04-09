from FinancePlanning.Models.User import User
from FinancePlanning.Repositories.XMLRepository import XMLRepository

if __name__ == '__main__':

    repo = XMLRepository("user", "C:\\MyWindows\\Projects\\FinancePlanning\\FinancePlanning", User)