import hashlib
from src.main.objects.server.UserInfo import UserInfo
from src.main.objects.server.DataBase import DataBase
from src.main.objects.server.Static import getConfigInfo, setConfigInfo
from src.main.objects.server.Validator import validateEmail, validateName, validateUsername, validatePassword


class Authorization:
    def __init__(self):
        self.__db = DataBase()

    def signIn(self, in_email: str, in_username: str, in_password: str, in_name: str):
        if validateEmail(in_email):
            return 'EMAIL_ERROR: ' + validateEmail(in_email)
        
        if validatePassword(in_password):
            return 'PASSWORD_ERROR: ' + validatePassword(in_password)
        
        if validateUsername(in_username):
            return 'USERNAME_ERROR: ' + validateUsername(in_username)
        
        if validateName(in_name):
            return 'NAME_ERROR: ' + validateName(in_name)
        
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            if self.__db.select(f"""SELECT * FROM Users WHERE email = '{in_email}';""") != ():
                return 'EMAIL_ERROR: ' + "Account with such an email already exists"
            
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            if self.__db.select(f"""SELECT * FROM Users WHERE username = '{in_username}';""") != ():
                return 'USERNAME_ERROR: ' + "Account with such an username already exists"

        salt = getConfigInfo('salt', 'salt')
        password = hashlib.md5((in_password + salt).encode()).hexdigest()
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            self.__db.insert(
            f"""INSERT INTO Users (email, username, password, name, access, image_id) \
                VALUES  ('{in_email}', '{in_username}', '{password}', '{in_name}', 'user', 1);""")

        setConfigInfo('current_user', 'email', in_email)
        UserInfo().updateConfig()

        return None

    def logIn(self, in_email: str, in_password: str):
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            user_info = self.__db.select(f"""SELECT password FROM Users WHERE email = '{in_email}';""")
            if user_info == ():
                return 'EMAIL_ERROR: ' + "Email is not found"
            else:
                user_info = user_info[0]

        salt = getConfigInfo('salt', 'salt')
        hashed_in_password = hashlib.md5((in_password + salt).encode()).hexdigest()
        if user_info['password'] != hashed_in_password:
            return 'PASSWORD_ERROR: ' + "Wrong password"

        setConfigInfo('current_user', 'email', in_email)
        UserInfo().updateConfig()

        return None

    @staticmethod
    def logOut():
        setConfigInfo('current_user', 'user_id', '-1')
        setConfigInfo('current_user', 'email', '-1')
        setConfigInfo('current_user', 'username', '-1')
        setConfigInfo('current_user', 'name', '-1')
        setConfigInfo('current_user', 'image_id', '-1')
        setConfigInfo('current_user', 'access', '-1')
        setConfigInfo('current_user', 'info', '-1')


# testing connection

# auth = Authorization()
# print(auth.signIn("kutorgin2002@gmail.com", "GunDon", "1234WaSd@@@@@@", "rUsIk"))
# auth.logOut()
# "GunDon", "1234WaSd@@@@@@"