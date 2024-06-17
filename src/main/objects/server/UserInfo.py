from src.main.objects.server.DataBase import DataBase
from src.main.objects.server.Static import getConfigInfo
from src.main.objects.server.Result import generateResult
from src.main.objects.server.MailSender import MailSender
from src.main.objects.server.Authorization import Authorization
from src.main.objects.server.Validator import validateName, validateUsername, validateAbout, getValidString


class User:
    def __init__(self, user_id):
        self._db = DataBase()
        self.user_id = user_id

    @property
    def userInfo(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            message = self.userID
            user_id = message["data"]
            error = message["error"]
            if user_id == -1:
                return generateResult(error_type="auth", error="User is not authorized!")
            if error:
                return message

            if not self._db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                user_info = self._db.select(f"""SELECT email, username, name, access, image_id, about FROM Users WHERE user_id = {user_id};""")[0]
                user_info['user_id'] = str(user_id)
                user_info['online'] = self.online['data']
                user_info['followers_ids'] = self.followersIds['data']
                user_info['followings_ids'] = self.followingsIds['data']
            return generateResult(data=user_info)
               
    @property
    def userID(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            if self._db.select(f"""SELECT email FROM Users WHERE user_id = {self.user_id};""") == ():
                return generateResult("This account isn't found", "format")
            else:
                return generateResult(data=int(self.user_id))
    
    @property
    def email(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            message = self.userID
            user_id = message["data"]
            error = message["error"]
            if user_id == -1:
                return generateResult(error_type="auth", error="User is not authorized!")
            if error:
                return message
            
            if not self._db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                email = self._db.select(f"""SELECT email FROM Users WHERE user_id = {user_id};""")[0]['email']
            return generateResult(data=email)
    
    @property
    def username(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            message = self.userID
            user_id = message["data"]
            error = message["error"]
            if user_id == -1:
                return generateResult(error_type="auth", error="User is not authorized!")
            if error:
                return message

            if not self._db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                username = self._db.select(f"""SELECT username FROM Users WHERE user_id = {user_id};""")[0]['username']
            return generateResult(data=username)
    
    @property
    def name(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            message = self.userID
            user_id = message["data"]
            error = message["error"]
            if user_id == -1:
                return generateResult(error_type="auth", error="User is not authorized!")
            if error:
                return message

            if not self._db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                name = self._db.select(f"""SELECT name FROM Users WHERE user_id = {user_id};""")[0]['name']
            return generateResult(data=name)

    @property
    def imageID(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            message = self.userID
            user_id = message["data"]
            error = message["error"]
            if user_id == -1:
                return generateResult(error_type="auth", error="User is not authorized!")
            if error:
                return message

            if not self._db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                image_id = int(self._db.select(f"""SELECT image_id FROM Users WHERE user_id = {user_id};""")[0]['image_id'])
            return generateResult(data=image_id)
    
    @property
    def access(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            message = self.userID
            user_id = message["data"]
            error = message["error"]
            if user_id == -1:
                return generateResult(error_type="auth", error="User is not authorized!")
            if error:
                return message

            if not self._db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                access = self._db.select(f"""SELECT access FROM Users WHERE user_id = {user_id};""")[0]['access']
            return generateResult(data=access)
        
    @property
    def about(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            message = self.userID
            user_id = message["data"]
            error = message["error"]
            if user_id == -1:
                return generateResult(error_type="auth", error="User is not authorized!")
            if error:
                return message

            if not self._db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                about = self._db.select(f"""SELECT about FROM Users WHERE user_id = {user_id};""")[0]['about']
                if about == "":
                    about = None
            return generateResult(data=about)
    
    @property
    def online(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            message = self.userID
            user_id = message["data"]
            error = message["error"]
            if user_id == -1:
                return generateResult(error_type="auth", error="User is not authorized!")
            if error:
                return message

            if not self._db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                difference_seconds = int(self._db.select(f"""SELECT TIMESTAMPDIFF(SECOND, time, NOW()) AS time \
                                                             FROM Online WHERE user_id = {user_id};""")[0]['time'])
                
        if difference_seconds <= int(getConfigInfo('const', 'difference_time_online')):
            return generateResult(data=True)
        return generateResult(data=False)
    
    @property
    def followersIds(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            message = self.userID
            user_id = message["data"]
            error = message["error"]
            if user_id == -1:
                return generateResult(error_type="auth", error="User is not authorized!")
            if error:
                return message
            
            if not self._db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                follower_ids = self._db.select(f"""SELECT follower_id FROM Followers WHERE user_id = {user_id};""")
            
            ids = []
            if follower_ids != ():
                for i in follower_ids:
                    ids.append(i['follower_id'])

        return generateResult(data=ids)
    
    @property
    def followingsIds(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            message = self.userID
            user_id = message["data"]
            error = message["error"]
            if user_id == -1:
                return generateResult(error_type="auth", error="User is not authorized!")
            if error:
                return message
            
            if not self._db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                following_ids = self._db.select(f"""SELECT user_id FROM Followers WHERE follower_id = {user_id};""")
            
            ids = []
            if following_ids != ():
                for i in following_ids:
                    ids.append(i['user_id'])

        return generateResult(data=ids)
    
    @property
    def postIds(self):
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            message = self.userID
            user_id = message["data"]
            error = message["error"]
            if user_id == -1:
                return generateResult(error_type="auth", error="User is not authorized!")
            if error:
                return message
            
            if not self._db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
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
            message = self.userID
            user_id = message["data"]
            error = message["error"]
            if user_id == -1:
                return generateResult(error_type="auth", error="User is not authorized!")
            if error:
                return message

            if not self._db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
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
        self.user_id = getConfigInfo('current_user', 'user_id')
        return generateResult(data=int(self.user_id))
    
    def changeName(self, new_name: str):
        error = self.updateOnline()
        if error["error"]:
            return error

        if validateName(new_name):
            return generateResult(validateName(new_name), "format")    
        
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID['data']
            self._db.insert(f"""UPDATE Users SET name = '{getValidString(new_name)}' WHERE user_id = {user_id};""")
        
        return generateResult()

    def changeUsername(self, new_username: str):
        error = self.updateOnline()
        if error["error"]:
            return error
        
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
    
    def changeAbout(self, new_about: str):
        error = self.updateOnline()
        if error["error"]:
            return error
        
        if validateAbout(new_about):
            return generateResult(validateAbout(new_about), "format")
        
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID['data']
            self._db.insert(f"""UPDATE Users SET about = '{getValidString(new_about)}' WHERE user_id = {user_id};""")

        return generateResult()
    
    def changeImageID(self, new_image_id: int):
        error = self.updateOnline()
        if error["error"]:
            return error
        
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
    
    def followTo(self, user_id: int):
        error = self.updateOnline()
        if error["error"]:
            return error
        
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:   
            if not self._db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                current_user_id = self.userID['data']
                self._db.insert(
                    f"""INSERT INTO Followers (user_id, follower_id) \
                        VALUES  ({str(user_id)}, {str(current_user_id)});""")
        return generateResult()

    def unfollowTo(self, user_id: int):
        error = self.updateOnline()
        if error["error"]:
            return error
        
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:   
            if not self._db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                current_user_id = self.userID['data']
                self._db.insert(
                    f"""DELETE FROM Followers
                        WHERE follower_id = {str(current_user_id)} 
                        AND 
                        user_id = {user_id};""")
        return generateResult() 
    
    def updateOnline(self):
        if not Authorization().checkAuthorization()["data"]:
            return generateResult(error_type="auth", error="User is not authorized!")
        
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            user_id = self.userID['data']
            self._db.insert(
                f"""UPDATE Online SET time = NOW() \
                    WHERE user_id = {user_id};""")
        
        return generateResult()

    def makeReportTo(self, post_id: int):
        error = self.updateOnline()
        if error["error"]:
            return error
        
        user_id_1 = self.userID["data"]
        username_1 = self.username["data"]

        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            post_info = self._db.select(f"""SELECT Posts.post_id, \
                                                   Posts.user_id, \
                                                   Users.username \
                                            FROM Posts \
                                            INNER JOIN Users \
                                                ON Posts.user_id = Users.user_id 
                                            WHERE Posts.post_id = {post_id};""")
            if post_info == ():
                return generateResult("This post isn't found", "format")
            user_id_2 = post_info[0]["user_id"]
            username_2 = post_info[0]["username"]
        
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            if self._db.select(f"""SELECT report_id FROM Reports \
                                   WHERE user_id_1 = {user_id_1} AND post_id = {post_id} AND user_id_2 = {user_id_2};""") != ():
                 return generateResult("You already sent report about this post", "format")
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            self._db.insert(f"""INSERT INTO Reports (user_id_1, post_id, user_id_2) \
                                VALUES  ({user_id_1}, {post_id}, {user_id_2});""")
        
        if not self._db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            admins_list = self._db.select(f"""SELECT email FROM Users WHERE access = 'Admin';""")
            if admins_list == ():
                return generateResult(error="No active admins. Try again later", error_type="format")
        
        for email in admins_list:
            MailSender(email_to=email["email"]).sendReportEmail({"user_id": user_id_1, "username": username_1}, 
                                                                {"user_id": user_id_2, "username": username_2, 
                                                                 "post_id": post_id})
        return generateResult()
        

# EXAMPLES FOR USING

# user = User(user_id=1) -> this class is needed to get information about a user by his user_id
# cur_user = CurrentUser() -> this class is a child class of User(), in which, in addition to getting information about the current user, it will be possible to change information about him

# GET USER INFO
# user.userInfo -> for getting email, username, name, access, image_id, about, user_id, online, followers_ids, followings_ids of user
# or
# cur_user.userInfo

# GET USER ID
# user.userID
# or
# cur_user.userID

# GET EMAIL
# user.email
# or
# cur_user.email

# GET USERNAME
# user.username
# or
# cur_user.username

# GET NAME
# user.name
# or
# cur_user.name

# GET ACCESS
# user.access
# or
# cur_user.access

# GET IMAGE ID
# user.image_id
# or
# cur_user.image_id

# GET ABOUT
# user.about
# or
# cur_user.about

# GET ONLINE
# user.online -> to check the online user
# or
# cur_user.online

# GET FOLLOWERS IDS
# user.followers_ids -> to get the user_id of users who are followed to this user
# or
# cur_user.followers_ids

# GET FOLLOWINGS IDS
# user.followings_ids -> to get the user_id of the users that this user is followed to
# or
# cur_user.followings_ids

# GET POST IDS
# user.postIds -> to get the post_id of the posts that this user has made
# or
# cur_user.postIds

# GET COMMENT IDS
# user.commentIds -> to get the comment_id of the comment that this user has made
# or
# cur_user.commentIds

# CHANGE NAME
# cur_user.changeName(new_name="new name")

# CHANGE USERNAME
# cur_user.changeUsername(new_username="new username")

# CHANGE ABOUT
# cur_user.changeAbout(new_about="new about")

# CHANGE IMAGE ID
# cur_user.changeImageID(new_image_id=1)

# CHANGE IMAGE ID
# cur_user.changeImageID(new_image_id=1)

# FOLLOW
# cur_user.followTo(user_id=1) -> to follow to another user

# UNFOLLOW
# cur_user.unfollowTo(user_id=1) -> to unfollow from a user, current user have already followed to

# UPDATE ONLINE
# cur_user.updateOnline() -> to mark the user's last action

# MAKE REPORT
# cur_user.makeReportTo(post_id=1) -> to send a post complaint to all admins by email
