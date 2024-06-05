import hashlib
from pytz import utc
from datetime import datetime
from src.main.objects.server.DataBase import DataBase
from src.main.objects.server.MailSender import MailSender
from src.main.objects.server.Result import generateResult
from src.main.objects.server.Static import getConfigInfo, setConfigInfo
from src.main.objects.server.Validator import validateEmail, validateName, validateUsername, validatePassword


class Authorization:
    def __init__(self):
        self.__db = DataBase()

    def signUp(self, in_email: str, in_username: str, in_password: str, in_name: str):
        self.logOut()

        if in_name == "":
            return generateResult("Enter name!", "format")
        if in_username == "":
            return generateResult("Enter username!", "format")
        if in_email == "":
            return generateResult("Enter email!", "format")
        if in_password == "":
            return generateResult("Enter password!", "format")
        
        if validateName(in_name):
            return generateResult(validateName(in_name), "format")
        if validateUsername(in_username):
            return generateResult(validateUsername(in_username), "format")
        if validateEmail(in_email):
            return generateResult(validateEmail(in_email), "format")
        if validatePassword(in_password):
            return generateResult(validatePassword(in_password), "format")
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            if self.__db.select(f"""SELECT * FROM Users WHERE email = '{in_email}';""") != ():
                return generateResult("Account with this email already exists", "format")
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            if self.__db.select(f"""SELECT * FROM Users WHERE username = '{in_username}';""") != ():
                return generateResult("This username is already occupied", "format")
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            if self.__db.select(f"""SELECT verification_id FROM Verifications WHERE email = '{in_email}';""") != ():
                if self.checkRelevance(in_email) == "Check your internet connection":
                    return generateResult("Check your internet connection", "connection")
                if self.checkRelevance(in_email):
                    return generateResult("You are sending request too often", "format")
        self.makeVerificationSession(in_email, in_username, in_name, in_password)

        return generateResult()
    
    def createNewAccount(self):
        if getConfigInfo("verification_session", "status") == "not_confirmed":
            return generateResult("Verification session not confirmed", "format")
        
        verification_id = getConfigInfo('verification_session', 'verification_id')
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            server_verification_info = self.__db.select(f"""SELECT * FROM Verifications WHERE verification_id = {verification_id};""")[0]
            user_id = -1
            email = server_verification_info['email']
            username = server_verification_info['username']
            name = server_verification_info['name']
            password = server_verification_info['password']
            hashed_password = hashlib.md5((password + getConfigInfo('const', 'salt')).encode()).hexdigest()          

        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            self.__db.insert(
            f"""INSERT INTO Users (email, username, password, name, access, image_id) \
                VALUES  ('{email}', '{username}', '{hashed_password}', '{name}', 'user', 1);""")
            setConfigInfo('current_user', 'user_id', str(user_id))
            setConfigInfo('current_user', 'password', str(password))
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.__db.select(f"""SELECT user_id FROM Users WHERE email = '{email}';""")[0]['user_id']

        utc_time = datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S")
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            self.__db.insert(
            f"""INSERT INTO Online (user_id, time) \
                VALUES  ({str(user_id)}, '{str(utc_time)}');""") 
        
        return self.closeVerificationSession(verification_id)

    def resetPassword(self, in_email: str):
        self.logOut()

        if in_email == "":
            return generateResult("Enter email!", "format")
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.__db.select(f"""SELECT user_id FROM Users WHERE email = '{in_email}';""")
            if user_id == ():
                return generateResult("Account with this email isn't found", "format")
            else:
                user_id = user_id[0]['user_id']
                
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            if self.__db.select(f"""SELECT verification_id FROM Verifications WHERE email = '{in_email}';""") != ():
                if self.checkRelevance(in_email) == 'Check your internet connection':
                    return generateResult("Check your internet connection", "connection")
                if self.checkRelevance(in_email):
                    return generateResult("You are sending request too often", "format")
        self.makeVerificationSession(in_email)
        setConfigInfo("verification_session", "status", "not_confirmed")
        return generateResult()
    
    def setNewPassword(self, in_password: str):
        if in_password == "":
            return generateResult("Enter password!", "format")
        if validatePassword(in_password):
            return generateResult(validatePassword(in_password), "format")
        if getConfigInfo("verification_session", "status") == "not_confirmed":
            return generateResult("Verification session not confirmed", "format")
        
        verification_id = getConfigInfo('verification_session', 'verification_id')
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            server_verification_info = self.__db.select(f"""SELECT * FROM Verifications WHERE verification_id = {verification_id};""")[0]
            user_id = -1
            email = server_verification_info['email']
            password = server_verification_info['password']
            hashed_password = hashlib.md5((password + getConfigInfo('const', 'salt')).encode()).hexdigest()
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.__db.select(f"""SELECT user_id FROM Users WHERE email = '{email}';""")[0]['user_id']
            
        utc_time = datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S")
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            self.__db.insert(
            f"""UPDATE Online SET time = '{str(utc_time)}' \
                WHERE user_id = {str(user_id)};""")           

        if not self.__db.connect():
            generateResult("Check your internet connection", "connection")
        else:
            self.__db.insert(
                f"""UPDATE Users SET password = '{str(hashed_password)}' \
                    WHERE user_id = '{user_id}';""")
            setConfigInfo('current_user', 'user_id', str(user_id))
            setConfigInfo('current_user', 'password', str(in_password))
            setConfigInfo("verification_session", "status", "not_confirmed")

        return self.closeVerificationSession(verification_id)
        
    def logIn(self, in_email: str, in_password: str):
        if in_email == "":
            return generateResult("Enter email!", "format")
        if in_password == "":
            return generateResult("Enter password!", "format")
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_info = self.__db.select(f"""SELECT user_id, password FROM Users WHERE email = '{in_email}';""")
            if user_info == ():
                return generateResult("Account with this email isn't found", "format")
            else:
                user_info = user_info[0]

        hashed_in_password = hashlib.md5((in_password + getConfigInfo('const', 'salt')).encode()).hexdigest()
        if user_info['password'] != hashed_in_password:
            return generateResult("Invalid password", "format")

        setConfigInfo('current_user', 'user_id', str(user_info['user_id']))
        setConfigInfo('current_user', 'password', str(in_password))

        return generateResult()

    @staticmethod
    def logOut():
        setConfigInfo("verification_session", "status", "not_confirmed")
        setConfigInfo("verification_session", "verification_id", "-1")
        
        setConfigInfo('current_user', 'user_id', '-1')
        setConfigInfo('current_user', 'password', '-1')

        return generateResult()
    
    def makeVerificationSession(self, email: str, username="", name="", password=""):
        fixed_name = name.replace("'", "''")
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection") 
        else:
            utc_time = datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S")
            code = MailSender(email).sendEmailVerification()
            self.__db.insert(
                f"""INSERT INTO Verifications (email, username, name, password, code, time) \
                    VALUES  ('{email}', '{username}', '{fixed_name}', '{password}', {code}, '{utc_time}');""")
            
            verification_id = self.__db.select(f"""SELECT verification_id FROM Verifications WHERE code = {code} AND time = '{utc_time}';""")[0]['verification_id']
            setConfigInfo('verification_session', 'verification_id', str(verification_id))
            setConfigInfo('verification_session', 'status', 'not_confirmed')

        return generateResult()

    def verificationSession(self, in_code: int):
        if in_code == "":
            return generateResult("Enter your personal code!", "format")

        verification_id = getConfigInfo('verification_session', 'verification_id')
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            server_verification_info = self.__db.select(f"""SELECT * FROM Verifications WHERE verification_id = {verification_id};""")
            if server_verification_info == ():
                return generateResult("This session doesn't exist", "foramt")
            else:
                server_verification_info = server_verification_info[0]
        
        if self.checkRelevance(server_verification_info['email']) == 'Check your internet connection':
            return generateResult("Check your internet connection", "connection")
        elif not self.checkRelevance(server_verification_info['email']):
            return generateResult("Code has expired. Try again!", "format") 
        
        if in_code != int(server_verification_info['code']):
            return generateResult("Enter your personal code!", "format")
        setConfigInfo("verification_session", "status", "confirmed")
        return generateResult()
    
    def closeVerificationSession(self, verification_id):
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            self.__db.insert(
            f"""DELETE FROM Verifications WHERE verification_id = {verification_id};""")

        return generateResult()

    def checkAuthorization(self):
        user_id = getConfigInfo('current_user', 'user_id')
        password = getConfigInfo('current_user', 'password')

        if user_id == "-1":
            return generateResult("Authorization is required", "format")
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            email = self.__db.select(f"""SELECT email FROM Users WHERE user_id = {user_id};""")[0]['email']

        if self.logIn(email, password)['errors']:
            return generateResult("Authorization is required", "format")
        
        return generateResult()
    
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
        if difference_seconds > int(getConfigInfo("const", "difference_time_code")):
            self.closeVerificationSession(verification_id)
            return False
        else:
            return True


# EXAMPLES FOR USING

# auth = Authorization()

# SIGN UP
# 1st step - > auth.signUp("kutorgin2002@gmail.com", "GunDon", "1234WaSd@@@@@@", "rUsIk")
# 2nd step - > auth.verificationSession(383102)
# 3rd step - > auth.createNewAccount()

# RESET PASSWORD
# 1st step - > auth.resetPassword("kutorgin2002@gmail.com")
# 2nd step - > auth.verificationSession(606074)
# 3rd step - > auth.setNewPassword("0000WaSd@@@@@@")

# LOG IN
# auth.logIn("kutorgin2002@gmail.com", "************")

# LOG OUT
# auth.logOut()
