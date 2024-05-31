import tzlocal
from pytz import timezone, utc
from datetime import datetime
from src.main.objects.server.DataBase import DataBase
from src.main.objects.server.UserInfo import UserInfo
from src.main.objects.server.Validator import validateText


class PostTools:
    def __init__(self):
        self.__db = DataBase()

    def createPost(self, text: str, image_id: int, video_id: int):
        if validateText(text):
            return 'TEXT_ERROR: ' + self.validateText(text)  

        user_id = str(UserInfo().userID)
        if user_id == "-1":
            return 'AUTHORIZATION_ERROR: Authorization is required'
        
        utc_time = datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S")

        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            self.__db.insert(
                f"""INSERT INTO Posts (user_id, image_id, video_id, post_text, likes, dislikes, post_time) \
                    VALUES  ({user_id}, {image_id}, {video_id}, '{text}', 0, 0, '{utc_time}');""")
        return None

    def createComment(self, comment_text: str, post_id: int):
        if validateText(comment_text):
            return 'TEXT_ERROR: ' + self.validateText(comment_text) 
        
        user_id = str(UserInfo().userID)
        if user_id == "-1":
            return 'AUTHORIZATION_ERROR: Authorization is required'
        
        utc_time = datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S")

        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            self.__db.insert(
                f"""INSERT INTO Comments (post_id, user_id, comment_time, comment_text, likes, dislikes) \
                    VALUES  ({post_id}, {user_id}, '{utc_time}', '{comment_text}', 0, 0);""")
        return None

    def getPostIds(self, sort_by_time=False, sort_by_likes=False, search_by_key=None):
        if sort_by_time:
            if not self.__db.connect():
                return 'CONNECTION_ERROR: Check your internet connection'
            else:
                post_info = self.__db.select("""SELECT post_id FROM Posts ORDER BY (post_time) DESC;""")
        elif sort_by_likes:
            if not self.__db.connect():
                return 'CONNECTION_ERROR: Check your internet connection'
            else:
                post_info = self.__db.select("""SELECT post_id FROM Posts ORDER BY (likes) DESC;""")
        elif search_by_key is not None:
            if not self.__db.connect():
                return 'CONNECTION_ERROR: Check your internet connection'
            else:
                post_info = self.__db.select(f"""SELECT post_id FROM Posts WHERE post_text LIKE '%{search_by_key}%';""")
        else:
            if not self.__db.connect():
                return 'CONNECTION_ERROR: Check your internet connection'
            else:
                post_info = self.__db.select("""SELECT post_id FROM Posts;""")

        if post_info == ():
            return 'SEARCH_ERROR: Posts were not found'

        ids = []
        for i in post_info:
            ids.append(i['post_id'])

        return ids

    def getPostInfo(self, post_ids: list):
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            posts_info = self.__db.select(
                f"""SELECT Posts.post_id, \
                           Posts.image_id, \
                           Posts.video_id, \
                           Posts.post_text, \
                           Posts.likes, \
                           Posts.dislikes, \
                           Posts.post_time, \
                           Users.username, \
                           Users.name, \
                           Users.image_id \
                    FROM Posts \
                    INNER JOIN Users \
                        ON Posts.user_id = Users.user_id \
                    WHERE Posts.post_id IN ({', '.join([str(i) for i in post_ids])});""")
        
        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            comments_info = self.__db.select(
                f"""SELECT Comments.post_id, \
                           Comments.user_id, \
                           Comments.comment_text, \
                           Comments.comment_time, \
                           Comments.likes, \
                           Comments.dislikes, \
                           Users.username, \
                           Users.name, \
                           Users.image_id \
                    FROM Comments \
                    INNER JOIN Users \
                        ON Comments.user_id = Users.user_id \
                    WHERE Comments.post_id IN ({', '.join([str(i) for i in post_ids])});""")
            
        dict_posts_info = dict()    
        for i in range(len(posts_info)):
            server_datetime = utc.localize(datetime.strptime(posts_info[i]['post_time'], "%Y-%m-%d %H:%M:%S"))
            posts_info[i]['post_time'] = server_datetime.astimezone(timezone(str(tzlocal.get_localzone()))).strftime(
                "%I:%M %p - %d %b %Y")
            dict_posts_info[posts_info[i]['post_id']] = posts_info[i]
            dict_posts_info[posts_info[i]['post_id']].pop('post_id')
        
        dict_comments_info = dict()
        if comments_info == ():
            for i in list(dict_posts_info.keys()):
                dict_posts_info[i]['comments'] = None
        else:
            for i in range(len(comments_info)): 
                server_datetime = utc.localize(datetime.strptime(comments_info[i]['comment_time'], "%Y-%m-%d %H:%M:%S"))
                comments_info[i]['comment_time'] = server_datetime.astimezone(timezone(str(tzlocal.get_localzone()))).strftime(
                "%I:%M %p - %d %b %Y")
                dict_comments_info[comments_info[i]['post_id']] = comments_info[i]
                dict_comments_info[comments_info[i]['post_id']].pop('post_id')
            for i in list(dict_posts_info.keys()):
                if i in list(dict_comments_info.keys()):
                    dict_posts_info[i]['comments'] = dict_comments_info[i]
                else:
                    dict_posts_info[i]['comments'] = None

        return dict_posts_info
    

# Example to using
# p = PostTools()
# print(p.createPost("форум кусок хуйни", 666, 69))
# ids = p.getPostIds(sort_by_time=True)
# print(p.getPostInfo(ids))
# print(p.createComment("че сказал?????", 4))
