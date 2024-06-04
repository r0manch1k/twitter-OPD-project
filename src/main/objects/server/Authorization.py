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

    def signUp(self, in_email: str, in_username: str, in_password: str, in_name: str):
        self.logOut()

        if in_email == "":
            return "Enter email!"
        if in_username == "":
            return "Enter username!"
        if in_password == "":
            return "Enter password!"
        if in_name == "":
            return "Enter name!"
        
        if validateName(in_name):
            return validateName(in_name)
        if validateUsername(in_username):
            return validateUsername(in_username)
        if validateEmail(in_email):
            return validateEmail(in_email)
        if validatePassword(in_password):
            return validatePassword(in_password)
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            if self.__db.select(f"""SELECT * FROM Users WHERE email = '{in_email}';""") != ():
                return "Account with this email already exists"
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            if self.__db.select(f"""SELECT * FROM Users WHERE username = '{in_username}';""") != ():
                return "This username is already occupied"
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            if self.__db.select(f"""SELECT verification_id FROM Verifications WHERE email = '{in_email}';""") != ():
                if self.checkRelevance(in_email) == 'Check your internet connection':
                    return 'Check your internet connection'
                if self.checkRelevance(in_email):
                    return "You are sending request too often"
                
        self.makeVerificationSession(in_email, in_username, in_name, in_password)

        return None

    def resetPassword(self, in_email: str):
        self.logOut()

        if in_email == "":
            return "Enter email!"
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            user_id = self.__db.select(f"""SELECT user_id FROM Users WHERE email = '{in_email}';""")
            if user_id == ():
                return "Account with this email isn't found"
            else:
                user_id = user_id[0]['user_id']
                
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            if self.__db.select(f"""SELECT verification_id FROM Verifications WHERE email = '{in_email}';""") != ():
                if self.checkRelevance(in_email) == 'Check your internet connection':
                    return 'Check your internet connection'
                if self.checkRelevance(in_email):
                    return "You are sending request too often"
        
        self.makeVerificationSession(in_email)

        return None
    
    def setNewPassword(self, in_password: str):
        if in_password == "":
            return "Enter password!"
        if validatePassword(in_password):
            return validatePassword(in_password)
        
        salt = getConfigInfo('salt', 'salt')
        hashed_password = hashlib.md5((in_password + salt).encode()).hexdigest()
        user_id = getConfigInfo('current_user', 'user_id')

        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            self.__db.insert(
                f"""UPDATE Users SET password = '{str(hashed_password)}' \
                    WHERE user_id = '{user_id}';""")
        setConfigInfo('current_user', 'password', str(in_password))

        return None
        
    def logIn(self, in_email: str, in_password: str):
        if in_email == "":
            return "Enter email!"
        if in_password == "":
            return "Enter password!"
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            user_info = self.__db.select(f"""SELECT user_id, password FROM Users WHERE email = '{in_email}';""")
            if user_info == ():
                return "Account with this email isn't found"
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
        setConfigInfo('current_user', 'password', '-1')
    
    def makeVerificationSession(self, email: str, username="", name="", password=""):
        fixed_name = name.replace("'", "''")
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            utc_time = datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S")
            code = MailSender(email).sendEmailVerification()
            self.__db.insert(
                f"""INSERT INTO Verifications (email, username, name, password, code, time) \
                    VALUES  ('{email}', '{username}', '{fixed_name}', '{password}', {code}, '{utc_time}');""")
            verification_id = self.__db.select(f"""SELECT verification_id FROM Verifications WHERE code = {code} AND time = '{utc_time}';""")[0]['verification_id']
            setConfigInfo('verification_session', 'verification_id', str(verification_id))
        
        return None

    def verificationSession(self, in_code: int, session_type: str):
        if in_code == "":
            return "Enter your personal code!"
        
        verification_id = getConfigInfo('verification_session', 'verification_id')
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            server_verification_info = self.__db.select(f"""SELECT * FROM Verifications WHERE verification_id = {verification_id};""")[0]
            if in_code != int(server_verification_info['code']):
                return 'Invalid personal code'
        
        user_id = -1
        email = server_verification_info['email']
        username = server_verification_info['username']
        name = server_verification_info['name']
        password = server_verification_info['password']
        hashed_password = hashlib.md5((password + getConfigInfo('salt', 'salt')).encode()).hexdigest()
        
        if self.checkRelevance(email) == 'Check your internet connection':
            return 'Check your internet connection'
        elif not self.checkRelevance(email):
            return 'Code has expired. Try again!'

        if session_type == "signUp": 
            if not self.__db.connect():
                return 'Check your internet connection'
            else:
                self.__db.insert(
                f"""INSERT INTO Users (email, username, password, name, access, image_id) \
                    VALUES  ('{email}', '{username}', '{hashed_password}', '{name}', 'user', 1);""")
            setConfigInfo('current_user', 'password', str(password))
        elif session_type == "resetPassword":
            pass

        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            user_id = self.__db.select(f"""SELECT user_id FROM Users WHERE email = '{email}';""")[0]['user_id']
            
        utc_time = datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S")
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            if self.__db.select(f"""SELECT * FROM Online WHERE user_id = '{str(user_id)}';""") != ():
                if not self.__db.connect():
                    return 'Check your internet connection'
                else:
                    self.__db.insert(
                    f"""UPDATE Online SET time = '{str(utc_time)}' \
                        WHERE user_id = {str(user_id)};""")
            else:
                if not self.__db.connect():
                    return 'Check your internet connection'
                else:
                    self.__db.insert(
                    f"""INSERT INTO Online (user_id, time) \
                        VALUES  ({str(user_id)}, '{str(utc_time)}');""")
                
        setConfigInfo('current_user', 'user_id', str(user_id))
        self.closeVerificationSession(verification_id)

        return None
    
    def closeVerificationSession(self, verification_id):
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            self.__db.insert(
            f"""DELETE FROM Verifications WHERE verification_id = {verification_id};""")

        return None

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
    
    def checkRelevance(self, email):
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            verification_id = self.__db.select(f"""SELECT verification_id FROM Verifications WHERE email = '{email}';""")

        if verification_id == ():
            return False
        verification_id = verification_id[0]['verification_id']
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            server_verification_time = self.__db.select(f"""SELECT time FROM Verifications WHERE verification_id = {verification_id};""")[0]['time']
            
        time1 = datetime.strptime(server_verification_time, "%Y-%m-%d %H:%M:%S")
        time2 = datetime.strptime(datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        difference = time2 - time1
        difference_seconds = difference.total_seconds()
        if difference_seconds > 90:
            self.closeVerificationSession(verification_id)
            return False
        else:
            return True

# EXAMPLES FOR USING

# auth = Authorization()

# SIGN UP
# 1st step - > auth.signUp("kutorgin2002@gmail.com", "GunDon", "1234WaSd@@@@@@", "rUsIk")
# 2nd step - > auth.verificationSession(383102, "signUp")

# RESET PASSWORD
# 1st step - > auth.resetPassword("kutorgin2002@gmail.com")
# 2nd step - > auth.verificationSession(606074, "resetPassword")
# 3rd step - > auth.setNewPassword("0000WaSd@@@@@@")

# LOG IN
# auth.logIn("kutorgin2002@gmail.com", "1234WaSd@@@@@@")

# LOG OUT
# auth.logOut()
