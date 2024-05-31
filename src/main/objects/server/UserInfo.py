from src.main.objects.server.DataBase import DataBase
from src.main.objects.server.Static import getConfigInfo, setConfigInfo
from src.main.objects.server.Validator import validateName, validateUsername, validateInfo


class UserInfo:
    def __init__(self):
        self.__db = DataBase()

    def updateConfig(self):
        email = self.email
        if email == "-1":
            return
        
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            user_info = self.__db.select(f"""SELECT * FROM Users WHERE email = '{email}';""")[0]
        
        setConfigInfo('current_user', 'user_id', str(user_info['user_id']))
        setConfigInfo('current_user', 'username', str(user_info['username']))
        setConfigInfo('current_user', 'name', str(user_info['name']))
        setConfigInfo('current_user', 'access', str(user_info['access']))
        setConfigInfo('current_user', 'image_id', str(user_info['image_id']))
        setConfigInfo('current_user', 'info', str(user_info['info']))

    def getOtherInfo(self, username):
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            user_info = self.__db.select(f"""SELECT username, name, image_id, info FROM Users WHERE username = '{username}';""")[0]
        
        return user_info
    
    @property
    def userID(self):
        return int(getConfigInfo('current_user', 'user_id'))
    
    @property
    def email(self):
        return getConfigInfo('current_user', 'email')
    
    @property
    def username(self):
        return getConfigInfo('current_user', 'username')
    
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
        if validateName(new_name):
            return 'NAME_ERROR: ' + self.validateName(new_name)      
        
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            self.__db.insert(f"""UPDATE Users SET name = '{new_name}' WHERE user_id = {str(self.userID)};""")
        setConfigInfo('current_user', 'name', new_name)
        
        return None

    def changeUsername(self, new_username: str):
        if validateUsername(new_username):
            return 'USERNAME_ERROR: ' + self.validateUsername(new_username)  

        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            if self.__db.select(f"""SELECT * FROM Users WHERE username = '{new_username}';""") != ():
                return 'USERNAME_ERROR: ' + "Account with such an username already exists"   
        
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            self.__db.insert(f"""UPDATE Users SET username = '{new_username}' WHERE user_id = {str(self.userID)};""")
        setConfigInfo('current_user', 'username', new_username)

        return None
    
    def changeInfo(self, new_info: str):
        if validateInfo(new_info):
            return 'INFO_ERROR: ' + self.changeInfo(new_info)
        
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
            image_info = self.__db.select(
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
