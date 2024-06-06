import pymysql
from .Static import getConfigInfo


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

        self.identity_ids = {'Users': 'user_id',
                             'Verifications': 'verification_id',
                             'Reactions': 'reaction_id',
                             'Posts': 'post_id',
                             'Chats': 'chat_id',
                             'Comments': 'comment_id',
                             'Friends': 'friends_id',
                             'Images': 'image_id',
                             'Messages': 'message_id',
                             'Videos': 'video_id'}

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
        except:
            return False

    def select(self, query):
        self.cursor.execute(query)
        info = self.cursor.fetchall()

        if info == ():
            return ()
        else:
            return info

    def insert(self, query):
        self.__update_id(query)

        self.cursor.execute(query)
        self.connection.commit()

    def __update_id(self, query):
        if query.startswith("INSERT INTO"):
            table_name = query.split(" ")[2]
            if table_name != "Online":
                table_primary_ids = self.select(f"""SELECT {self.identity_ids[table_name]} FROM {table_name};""")

                new_id = 0
                if table_primary_ids != ():
                    ids = []
                    for i in table_primary_ids:
                        ids.append(i[self.identity_ids[table_name]])
                    ids.sort()
                    new_id = max(ids)
                    for i in range(1, len(ids)):
                        if ids[i - 1] + 1 != ids[i]:
                            new_id = ids[i - 1]

                self.cursor.execute(f"""ALTER TABLE {table_name} AUTO_INCREMENT = {new_id};""")
                self.connection.commit()
        return
