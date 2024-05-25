import hashlib
from src.main.objects.server.UserInfo import UserInfo
from src.main.objects.server.DataBase import DataBase
from src.main.objects.server.Static import getConfigInfo, setConfigInfo


class Authorization:
    def __init__(self):
        self.__db = DataBase()

    def signIn(self, in_login: str, in_password: str, in_name: str):
        if self.validateLogin(in_login):
            return 'LOGIN_ERROR: ' + self.validateLogin(in_login)
        
        if self.validatePassword(in_password):
            return 'PASSWORD_ERROR: ' + self.validatePassword(in_password)
        
        if len(in_name) < 4 or len(in_name) > 20:
            return 'NAME_ERROR: ' + "Name must be between 4 and 20 characters long"
        
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            if self.__db.select(f"""SELECT * FROM Users WHERE login = '{in_login}';""") != ():
                return 'LOGIN_ERROR: ' + "This login is already taken"

        salt = getConfigInfo('salt', 'salt')
        password = hashlib.md5((in_password + salt).encode()).hexdigest()
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            self.__db.insert(
            f"""INSERT INTO Users (login, password, name, access) \
                VALUES  ('{in_login}', '{password}', '{in_name}', 'user');""")

        setConfigInfo('current_user', 'login', in_login)
        UserInfo().updateConfig()

        return None

    def logIn(self, in_login: str, in_password: str):
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            user_info = self.__db.select(f"""SELECT * FROM Users WHERE login = '{in_login}';""")
            if user_info == ():
                return 'LOGIN_ERROR: ' + "Login is not found"
            else:
                user_info = user_info[0]

        salt = getConfigInfo('salt', 'salt')
        hashed_in_password = hashlib.md5((in_password + salt).encode()).hexdigest()
        if user_info['password'] != hashed_in_password:
            return 'PASSWORD_ERROR: ' + "Wrong password"

        setConfigInfo('current_user', 'login', in_login)
        UserInfo().updateConfig()

        return None

    @staticmethod
    def logOut():
        setConfigInfo('current_user', 'user_id', '-1')
        setConfigInfo('current_user', 'login', '-1')
        setConfigInfo('current_user', 'name', '-1')
        setConfigInfo('current_user', 'access', '-1')
        setConfigInfo('current_user', 'info', '-1')

    @staticmethod
    def validateLogin(login):
        lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        digits = [str(i) for i in range(10)]
        other_symbols = ['_', '$']

        if len(login) < 2 or len(login) > 16:
            return "Login must be between 2 and 16 characters long"

        for i in login:
            if (i not in lowercase_letters and i not in uppercase_letters
                    and i not in digits and i not in other_symbols):
                return "Password contains an invalid character -> " + i

        return ""

    @staticmethod
    def validatePassword(password):
        if len(password) < 8 or len(password) > 16:
            return "Password must be between 8 and 16 characters long"

        flag = False
        for i in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
            if password.find(i) > 0:
                flag = True
                break
        if not flag:
            return "Password must contain Latin lowercase letters"

        flag = False
        for i in [chr(i) for i in range(ord('A'), ord('Z') + 1)]:
            if password.find(i) > 0:
                flag = True
                break
        if not flag:
            return "Password must contain Latin uppercase letters"

        flag = False
        for i in [str(i) for i in range(0, 10)]:
            if password.find(i) > 0:
                flag = True
                break
        if not flag:
            return "Password must contain digits"

        flag = False
        for i in "[_@$]":
            if password.find(i) > 0:
                flag = True
                break
        if not flag:
            return "Password must contain special characters -> []_@$"

        for i in r"-+={}<>!#£%^&*()~` '?/|\:;":
            if password.find(i) > 0:
                return "Password contains an invalid character -> " + i

        return ""


# testing connection

# auth = Authorization()
# print(auth.logIn("GunDon", "1234WaSd@@@@@@"))
# auth.logOut()