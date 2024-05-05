from abc import ABC

import psycopg2

from FinancePlanning.Repositories.RepositoryBase import RepositoryBase


class TableRepository(RepositoryBase, ABC):

    def __init__(self, name):
        self.name = name
        self.conn = psycopg2.connect(
            dbname="Star", host="localhost", user="admin",
            password="123456", port="5432"
        )

    def __del__(self):
        self.conn.close()
