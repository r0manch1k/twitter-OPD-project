import pymysql
from src.main.objects.server.Static import getConfigInfo


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance


class DataBase(Singleton):
    def __init__(self):
        self.__host = getConfigInfo('server', 'host')
        self.__port = int(getConfigInfo('server', 'port'))
        self.__user = getConfigInfo('server', 'user')
        self.__password = getConfigInfo('server', 'password')
        self.__database = getConfigInfo('server', 'database')

        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            if self.connection is None:
                self.connection = pymysql.connect(
                    host=self.__host,
                    port=self.__port,
                    user=self.__user,
                    password=self.__password,
                    database=self.__database,
                    cursorclass=pymysql.cursors.DictCursor)
                self.cursor = self.connection.cursor()
            return True
        except Exception:
            return False

    def select(self, query):
        self.cursor.execute(query)
        info = self.cursor.fetchall()

        if info == ():
            return ()
        else:
            return info

    def insert(self, query):
        self.cursor.execute(query)
        self.connection.commit()
