from src.main.objects.server.DataBase import DataBase
from src.main.objects.server.Authorization import Authorization
from src.main.objects.server.Static import getConfigInfo
from src.main.objects.server.Validator import validateName, validateUsername, validateInfo


class UserInfo:
    def __init__(self, user_id):
        self.__db = DataBase()
        self.__user_id = user_id
    
    @property
    def userID(self):
        return int(self.__user_id)
    
    @property
    def email(self):
        message = Authorization().checkAuthorization()
        if message:
            return message
             
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            return self.__db.select(f"""SELECT email FROM Users WHERE user_id = {self.userID};""")[0]['email']
    
    @property
    def username(self):
        message = Authorization().checkAuthorization()
        if message:
            return message
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            return self.__db.select(f"""SELECT username FROM Users WHERE user_id = {self.userID};""")[0]['username']
    
    @property
    def name(self):
        message = Authorization().checkAuthorization()
        if message:
            return message
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            return self.__db.select(f"""SELECT name FROM Users WHERE user_id = {self.userID};""")[0]['name']

    @property
    def imageID(self):
        message = Authorization().checkAuthorization()
        if message:
            return message
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            return int(self.__db.select(f"""SELECT image_id FROM Users WHERE user_id = {self.userID};""")[0]['image_id'])
    
    @property
    def access(self):
        message = Authorization().checkAuthorization()
        if message:
            return message
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            return self.__db.select(f"""SELECT access FROM Users WHERE user_id = {self.userID};""")[0]['access']
        
    @property
    def info(self):
        message = Authorization().checkAuthorization()
        if message:
            return message
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            return self.__db.select(f"""SELECT info FROM Users WHERE user_id = {self.userID};""")[0]['info']
    
    @property
    def postIds(self):
        message = Authorization().checkAuthorization()
        if message:
            return message
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            post_ids = self.__db.select(f"""SELECT post_id FROM Posts WHERE user_id = {self.userID};""")
        
        if post_ids == ():
            return 'Posts were not found'

        ids = []
        for i in post_ids:
            ids.append(i['post_id'])

        return ids
    
    @property
    def commentIds(self):
        message = Authorization().checkAuthorization()
        if message:
            return message
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            post_ids = self.__db.select(f"""SELECT comment_id FROM Comments WHERE user_id = {self.userID};""")
        
        if post_ids == ():
            return 'Comments were not found'

        ids = []
        for i in post_ids:
            ids.append(i['comment_id'])

        return ids
    

class CurrentUserInfo(UserInfo):
    def __init__(self):
        super().__init__(user_id=getConfigInfo('current_user', 'user_id'))
        self.__db = DataBase()
    
    def changeName(self, new_name: str):
        message = Authorization().checkAuthorization()
        if message:
            return message

        if validateName(new_name):
            return self.validateName(new_name)      
        
        fixed_name = new_name.replace("'", "''")
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            self.__db.insert(f"""UPDATE Users SET name = '{fixed_name}' WHERE user_id = {str(self.userID)};""")
        
        return None

    def changeUsername(self, new_username: str):
        message = Authorization().checkAuthorization()
        if message:
            return message
        
        if validateUsername(new_username):
            return self.validateUsername(new_username)  

        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            if self.__db.select(f"""SELECT * FROM Users WHERE username = '{new_username}';""") != ():
                return "This username is already occupied"   
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            self.__db.insert(f"""UPDATE Users SET username = '{new_username}' WHERE user_id = {str(self.userID)};""")

        return None
    
    def changeInfo(self, new_info: str):
        message = Authorization().checkAuthorization()
        if message:
            return message
        
        if validateInfo(new_info):
            return self.changeInfo(new_info)
        
        fixed_info = new_info.replace("'", "''")
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            self.__db.insert(f"""UPDATE Users SET info = '{fixed_info}' WHERE user_id = {str(self.userID)};""")

        return None
    
    def changeImageID(self, new_image_id: int):
        message = Authorization().checkAuthorization()
        if message:
            return message
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            image_info = self.__db.select(
                f"""SELECT * FROM Images \
                    WHERE image_id = {str(new_image_id)};""")
        
        if image_info == ():
            return "This id is not found" 
        else:
            image_info = image_info[0]

        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            self.__db.insert(
                f"""UPDATE Users SET image_id = '{str(new_image_id)}' \
                    WHERE user_id = {str(self.userID)};""")

        return None


# u = CurrentUserInfo()
# print(u.changeInfo("""i l'o'v"e abdukh'kim"""))