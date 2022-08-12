import psycopg2

from conf import *


class DataBase:
    """
    Подключение к базе данных
    получает аргументы из файла conf
    """

    def __init__(self, host, user, password, database):

        try:
            self.psycopg = psycopg2.connect(
                dbname=database,
                user=user,
                password=password,
                host=host
            )
            self.cursor = self.psycopg.cursor()
            self.connected = True
        except Exception as ex:
            self.error = ex
            self.connected = False


db = DataBase(host=host, user=user, password=password, database=database)
