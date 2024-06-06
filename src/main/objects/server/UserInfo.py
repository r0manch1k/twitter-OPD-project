from pytz import utc
from datetime import datetime
from src.main.objects.server.DataBase import DataBase
from src.main.objects.server.Static import getConfigInfo
from src.main.objects.server.Result import generateResult
from src.main.objects.server.Authorization import Authorization
from src.main.objects.server.Validator import validateName, validateUsername, validateInfo


class User:
    def __init__(self, user_id):
        self._db = DataBase()
        self.user_id = user_id

    @property
    def userInfo(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID
            if user_id['data'] is None:
                return user_id
            else:
                user_id = user_id["data"]

            user_info = self._db.select(f"""SELECT email, username, name, access, image_id, about FROM Users WHERE user_id = {user_id};""")[0]
            user_info['user_id'] = str(user_id)
            return generateResult(data=user_info)
               
    @property
    def userID(self):
        return generateResult(data=int(self.user_id))
    
    @property
    def email(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID
            if user_id['data'] is None:
                return user_id
            else:
                user_id = user_id["data"]

            email = self._db.select(f"""SELECT email FROM Users WHERE user_id = {user_id};""")[0]['email']
            return generateResult(data=email)
    
    @property
    def username(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID
            if user_id['data'] is None:
                return user_id
            else:
                user_id = user_id["data"]

            username = self._db.select(f"""SELECT username FROM Users WHERE user_id = {user_id};""")[0]['username']
            return generateResult(data=username)
    
    @property
    def name(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID
            if user_id['data'] is None:
                return user_id
            else:
                user_id = user_id["data"]

            name = self._db.select(f"""SELECT name FROM Users WHERE user_id = {user_id};""")[0]['name']
            return generateResult(data=name)

    @property
    def imageID(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID
            if user_id['data'] is None:
                return user_id
            else:
                user_id = user_id["data"]

            image_id = int(self._db.select(f"""SELECT image_id FROM Users WHERE user_id = {user_id};""")[0]['image_id'])
            return generateResult(data=image_id)
    
    @property
    def access(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID
            if user_id['data'] is None:
                return user_id
            else:
                user_id = user_id["data"]

            access = self._db.select(f"""SELECT access FROM Users WHERE user_id = {user_id};""")[0]['access']
            return generateResult(data=access)
        
    @property
    def about(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID
            if user_id['data'] is None:
                return user_id
            else:
                user_id = user_id["data"]

            about = self._db.select(f"""SELECT about FROM Users WHERE user_id = {user_id};""")[0]['about']
            if about == "":
                about = None
            return generateResult(data=about)
    
    @property
    def online(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID
            if user_id['data'] is None:
                return user_id
            else:
                user_id = user_id["data"]

            recent_activity = self._db.select(f"""SELECT time FROM Online WHERE user_id = {user_id};""")[0]['time']

        time1 = datetime.strptime(recent_activity, "%Y-%m-%d %H:%M:%S")
        time2 = datetime.strptime(datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        difference = time2 - time1
        difference_seconds = difference.total_seconds()
        if difference_seconds <= int(getConfigInfo('const', 'difference_time_online')):
            return generateResult(data=True)
        return generateResult(data=False)
    
    @property
    def postIds(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID
            if user_id['data'] is None:
                return user_id
            else:
                user_id = user_id["data"]

            post_ids = self._db.select(f"""SELECT post_id FROM Posts WHERE user_id = {user_id};""")
        
        if post_ids == ():
            return generateResult("Posts were not found", "format")
        ids = []
        for i in post_ids:
            ids.append(i['post_id'])

        return generateResult(data=ids)
    
    @property
    def commentIds(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:   
            user_id = self.userID
            if user_id['data'] is None:
                return user_id
            else:
                user_id = user_id["data"]

            post_ids = self._db.select(f"""SELECT comment_id FROM Comments WHERE user_id = {user_id};""")
        
        if post_ids == ():
            return generateResult("Comments were not found", "format")

        ids = []
        for i in post_ids:
            ids.append(i['comment_id'])

        return generateResult(data=ids)
    

class CurrentUser(User):
    def __init__(self):
        super().__init__(user_id=getConfigInfo('current_user', 'user_id'))

    @property
    def userID(self):
        message = Authorization().checkAuthorization()
        if message['error'] is not None:
            return message

        self.user_id = getConfigInfo('current_user', 'user_id')
        return generateResult(data=int(self.user_id))
    
    def changeName(self, new_name: str):
        message = Authorization().checkAuthorization()
        if message['error']:
            return message

        if validateName(new_name):
            return generateResult(validateName(new_name), "format")    
        
        fixed_name = new_name.replace("'", "''")
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID['data']
            self._db.insert(f"""UPDATE Users SET name = '{fixed_name}' WHERE user_id = {user_id};""")
        
        return generateResult()

    def changeUsername(self, new_username: str):
        message = Authorization().checkAuthorization()
        if message['error']:
            return message
        
        if validateUsername(new_username):
            return generateResult(validateUsername(new_username), "format")

        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            if self._db.select(f"""SELECT * FROM Users WHERE username = '{new_username}';""") != ():
                return generateResult("This username is already occupied", "format") 
        
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID['data']
            self._db.insert(f"""UPDATE Users SET username = '{new_username}' WHERE user_id = {user_id};""")

        return generateResult()
    
    def changeInfo(self, new_info: str):
        message = Authorization().checkAuthorization()
        if message['error']:
            return message
        
        if validateInfo(new_info):
            return generateResult(validateInfo(new_info), "format")
        
        fixed_info = new_info.replace("'", "''")
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID['data']
            self._db.insert(f"""UPDATE Users SET info = '{fixed_info}' WHERE user_id = {user_id};""")

        return generateResult()
    
    def changeImageID(self, new_image_id: int):
        message = Authorization().checkAuthorization()
        if message["error"]:
            return message
        
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            image_info = self._db.select(
                f"""SELECT * FROM Images \
                    WHERE image_id = {str(new_image_id)};""")
        
        if image_info == ():
            return generateResult("This id is not found", "format")
        else:
            image_info = image_info[0]
        
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID['data']
            self._db.insert(
                f"""UPDATE Users SET image_id = '{str(new_image_id)}' \
                    WHERE user_id = {user_id};""")

        return generateResult()
    
    def updateOnline(self):
        message = Authorization().checkAuthorization()
        if message["error"]:
            return message
        
        utc_time = datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S")
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID['data']
            self._db.insert(
                f"""UPDATE Online SET time = '{str(utc_time)}' \
                    WHERE user_id = {user_id};""")
        
        return generateResult()
