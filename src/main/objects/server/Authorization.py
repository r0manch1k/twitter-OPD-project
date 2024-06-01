import hashlib
from pytz import utc
from datetime import datetime
from src.main.objects.server.DataBase import DataBase
from src.main.objects.server.MailSender import MailSender
from src.main.objects.server.Static import getConfigInfo, setConfigInfo
from src.main.objects.server.Validator import validateEmail, validateName, validateUsername, validatePassword


class Authorization:
    def __init__(self):
        self.__db = DataBase()

    def signIn(self, in_email: str, in_username: str, in_password: str, in_name: str):
        if validateEmail(in_email):
            return validateEmail(in_email)
        
        if validatePassword(in_password):
            return validatePassword(in_password)
        
        if validateUsername(in_username):
            return validateUsername(in_username)
        
        if validateName(in_name):
            return validateName(in_name)
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            if self.__db.select(f"""SELECT * FROM Users WHERE email = '{in_email}';""") != ():
                return "Account with such an email already exists"
            
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            if self.__db.select(f"""SELECT * FROM Users WHERE username = '{in_username}';""") != ():
                return "Account with such an username already exists"

        salt = getConfigInfo('salt', 'salt')
        hashed_in_password = hashlib.md5((in_password + salt).encode()).hexdigest()
        fixed_name = in_name.replace("'", "/'")

        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            utc_time = datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S")
            code = MailSender(in_email).sendEmailVerification()
            self.__db.insert(f"""INSERT INTO Verifications (code, time) \
                VALUES  ({code}, '{utc_time}');""")
            verification_id = self.__db.select(f"""SELECT id FROM Verifications WHERE code = {code} AND time = '{utc_time}';""")[0]['id']
        
        setConfigInfo('verification_session', 'verification_id', str(verification_id))
        setConfigInfo('verification_session', 'email', str(in_email))
        setConfigInfo('verification_session', 'username', str(in_username))
        setConfigInfo('verification_session', 'password', str(hashed_in_password))
        setConfigInfo('verification_session', 'name', str(fixed_name))

        return None

    def verificationSession(self, in_code: int):
        verification_id = getConfigInfo('verification_session', 'verification_id')

        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            server_verification_info = self.__db.select(f"""SELECT code, time FROM Verifications WHERE id = {verification_id};""")[0]
        
        if in_code != int(server_verification_info['code']):
            return 'Invalid personal code'
        
        time1 = datetime.strptime(server_verification_info['time'], "%Y-%m-%d %H:%M:%S")
        time2 = datetime.strptime(datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        difference = time2 - time1
        difference_seconds = difference.total_seconds()
        if difference_seconds > 180:
            self.closeVerificationSession()
            return 'Code has expired. Try again'
                
        email = getConfigInfo('verification_session', 'email')
        username = getConfigInfo('verification_session', 'username')
        password = getConfigInfo('verification_session', 'password')
        name = getConfigInfo('verification_session', 'name') 

        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            self.__db.insert(
            f"""INSERT INTO Users (email, username, password, name, access, image_id) \
                VALUES  ('{email}', '{username}', '{password}', '{name}', 'user', 1);""")
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            user_id = self.__db.select(f"""SELECT user_id FROM Users WHERE email = '{email}';""")[0]['user_id']
        
        setConfigInfo('current_user', 'user_id', str(user_id))
        setConfigInfo('current_user', 'password', str(password))
        self.closeVerificationSession()

        return None
    
    def closeVerificationSession(self):
        verification_id = getConfigInfo('verification_session', 'verification_id')
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            self.__db.insert(
            f"""DELETE FROM Verifications WHERE id = {verification_id};""")

        setConfigInfo('verification_session', 'verification_id', "-1")
        setConfigInfo('verification_session', 'email', "-1")
        setConfigInfo('verification_session', 'username', "-1")
        setConfigInfo('verification_session', 'password', "-1")
        setConfigInfo('verification_session', 'name', "-1")

        return None

    def logIn(self, in_email: str, in_password: str):
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            user_info = self.__db.select(f"""SELECT user_id, password FROM Users WHERE email = '{in_email}';""")
            if user_info == ():
                return "Email is not found"
            else:
                user_info = user_info[0]

        salt = getConfigInfo('salt', 'salt')
        hashed_in_password = hashlib.md5((in_password + salt).encode()).hexdigest()
        if user_info['password'] != hashed_in_password:
            return "Invalid password"

        setConfigInfo('current_user', 'user_id', str(user_info['user_id']))
        setConfigInfo('current_user', 'password', str(in_password))

        return None

    @staticmethod
    def logOut():
        setConfigInfo('current_user', 'user_id', '-1')

    def checkAuthorization(self):
        user_id = getConfigInfo('current_user', 'user_id')
        password = getConfigInfo('current_user', 'password')

        if user_id == "-1":
            return 'Authorization is required'
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            email = self.__db.select(f"""SELECT email FROM Users WHERE user_id = {user_id};""")[0]['email']
        
        if self.logIn(email, password):
            return 'Authorization is required'
        
        return None


# testing connection

# auth = Authorization()
# print(auth.signIn("kutorgin2002@gmail.com", "GunDon", "1234WaSd@@@@@@", "rUsIk"))
# print(auth.verificationSession(363897))
# print(auth.logIn("kutorgin2002@gmail.com", "1234WaSd@@@@@@"))
# auth.logOut()