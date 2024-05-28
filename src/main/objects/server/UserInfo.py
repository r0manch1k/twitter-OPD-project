from src.main.objects.server.DataBase import DataBase
from src.main.objects.server.Static import getConfigInfo, setConfigInfo


class UserInfo:
    def __init__(self):
        self.__db = DataBase()

    def updateConfig(self):
        login = self.login
        if login == "-1":
            return
        
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            user_info = self.__db.select(f"""SELECT * FROM Users WHERE login = '{login}';""")[0]
        
        setConfigInfo('current_user', 'user_id', str(user_info['user_id']))
        setConfigInfo('current_user', 'name', str(user_info['name']))
        setConfigInfo('current_user', 'access', str(user_info['access']))
        setConfigInfo('current_user', 'image_id', str(user_info['image_id']))
        setConfigInfo('current_user', 'info', str(user_info['info']))

    def getOtherInfo(self, login):
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            user_info = self.__db.select(f"""SELECT * FROM Users WHERE login = '{login}';""")[0]
        
        return user_info
    
    @property
    def userID(self):
        return int(getConfigInfo('current_user', 'user_id'))
    
    @property
    def login(self):
        return getConfigInfo('current_user', 'login')
    
    @property
    def name(self):
        return getConfigInfo('current_user', 'name')

    @property
    def imageID(self):
        return int(getConfigInfo('current_user', 'image_id'))
    
    @property
    def access(self):
        return getConfigInfo('current_user', 'access')
    
    @property
    def info(self):
        return getConfigInfo('current_user', 'info')
    
    def changeName(self, new_name: str):
        if len(new_name) < 4 or len(new_name) > 20:
            return 'NAME_ERROR: ' + "Name must be between 4 and 20 characters long"       
        
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            self.__db.insert(f"""UPDATE Users SET name = '{new_name}' WHERE user_id = {str(self.userID)};""")
        setConfigInfo('current_user', 'name', new_name)
        return None
    
    def changeInfo(self, new_info: str):
        if len(new_info) > 30:
            return 'INFO_ERROR: ' + "Info must be less than 30 characters long"
        
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            self.__db.insert(f"""UPDATE Users SET info = '{new_info}' WHERE user_id = {str(self.userID)};""")
        setConfigInfo('current_user', 'info', new_info)
        return None
    
    def changeImageID(self, new_image_id: int):
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            image_info = self.db.select(
                f"""SELECT * FROM Images \
                    WHERE image_id = {str(new_image_id)};""")
        
        if image_info == ():
            return 'IMAGE_ID_ERROR: ' + "This id is not found" 
        else:
            image_info = image_info[0]

        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            self.__db.insert(
                f"""UPDATE Users SET image_id = '{str(new_image_id)}' \
                    WHERE user_id = {str(self.userID)};""")
        setConfigInfo('current_user', 'image_id', str(new_image_id))
        return None