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
        self.update_id(query)
            
        self.cursor.execute(query)
        self.connection.commit()
    
    def update_id(self, query):
        if query[:11] == "INSERT INTO":
            begin = 12
            end = -1
            for i in range(begin, len(query)):
                if query[i] == " ":
                    end = i
                    break
            table_name = query[begin : end]
            identity_ids = {'Users': 'user_id', 
                            'Verifications': 'verification_id', 
                            'Reactions': 'reaction_id', 
                            'Posts': 'post_id', 
                            'Online': 'user_id', 
                            'Chats': 'chat_id',
                            'Comments': 'comment_id',
                            'Friends': 'friends_id', 
                            'Images': 'image_id',
                            'Messages': 'message_id',
                            'Videos': 'video_id'}
            max_id = self.select(f"""SELECT MAX({identity_ids[table_name]}) FROM {table_name};""")[0][f"""MAX({identity_ids[table_name]})"""]
            if max_id is None:
                max_id = 0
    
            self.cursor.execute(f"""ALTER TABLE {table_name} AUTO_INCREMENT = {max_id};""")
            self.connection.commit()
        return 
