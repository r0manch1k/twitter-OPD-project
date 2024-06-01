import tzlocal
from datetime import datetime
from pytz import timezone, utc
from src.main.objects.server.DataBase import DataBase
from src.main.objects.server.Validator import validateText
from src.main.objects.server.UserInfo import CurrentUserInfo
from src.main.objects.server.Authorization import Authorization


class PostTools:
    def __init__(self):
        self.__db = DataBase()

    def createPost(self, post_text: str, image_id: int, video_id: int):
        message = Authorization().checkAuthorization()
        if message:
            return message

        if validateText(post_text):
            return self.validateText(post_text)  
        
        utc_time = datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S")
        fixed_post_text = post_text.replace("'", "''")
        user_id = CurrentUserInfo().userID

        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            self.__db.insert(
                f"""INSERT INTO Posts (user_id, image_id, video_id, post_text, likes, dislikes, post_time) \
                    VALUES  ({user_id}, {image_id}, {video_id}, '{fixed_post_text}', 0, 0, '{utc_time}');""")
        return None
    
    def deletePost(self, post_id):
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            self.__db.insert(
            f"""DELETE FROM Posts WHERE post_id = {post_id};""")
        
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            self.__db.insert(
            f"""DELETE FROM Comments WHERE post_id = {post_id};""")
        
        return None

    def createComment(self, comment_text: str, post_id: int):
        message = Authorization().checkAuthorization()
        if message:
            return message
        
        if validateText(comment_text):
            return self.validateText(comment_text) 
        
        utc_time = datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S")
        fixed_comment_text = comment_text.replace("'", "''")
        user_id = CurrentUserInfo().userID

        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            self.__db.insert(
                f"""INSERT INTO Comments (post_id, user_id, comment_time, comment_text, likes, dislikes) \
                    VALUES  ({post_id}, {user_id}, '{utc_time}', '{fixed_comment_text}', 0, 0);""")
        return None
    
    def deleteComment(self, comment_id):
        if not self.__db.connect():
            return 'Check your internet connection'
        else:
            self.__db.insert(
            f"""DELETE FROM Comments WHERE comment_id = {comment_id};""")
        
        return None

    def getPostIds(self, sort_by_time=False, sort_by_likes=False, search_by_key=None):
        if sort_by_time:
            if not self.__db.connect():
                return 'Check your internet connection'
            else:
                post_ids = self.__db.select("""SELECT post_id FROM Posts ORDER BY (post_time) DESC;""")
        elif sort_by_likes:
            if not self.__db.connect():
                return 'Check your internet connection'
            else:
                post_ids = self.__db.select("""SELECT post_id FROM Posts ORDER BY (likes) DESC;""")
        elif search_by_key is not None:
            if not self.__db.connect():
                return 'Check your internet connection'
            else:
                post_ids = self.__db.select(f"""SELECT post_id FROM Posts WHERE post_text LIKE '%{search_by_key}%';""")
        else:
            if not self.__db.connect():
                return 'Check your internet connection'
            else:
                post_ids = self.__db.select("""SELECT post_id FROM Posts;""")

        if post_ids == ():
            return 'Posts were not found'

        ids = []
        for i in post_ids:
            ids.append(i['post_id'])

        return ids

    def getPostInfo(self, post_ids: list):
        if not self.__db.connect():
            return 'Check your internet connection'
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
            return 'Check your internet connection'
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
                comments_info[i]['comment_time'] = server_datetime.astimezone(timezone(str(tzlocal.get_localzone()))).strftime("%I:%M %p - %d %b %Y")
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
# print(p.createComment("zov", 4))
