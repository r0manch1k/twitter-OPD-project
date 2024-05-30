import tzlocal
from pytz import timezone, utc
from datetime import datetime
from src.main.objects.server.DataBase import DataBase
from src.main.objects.server.UserInfo import UserInfo


class PostTools:
    def __init__(self):
        self.__db = DataBase()

    def createPost(self, text: str, image_id: int, video_id: int):
        vl_time = datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S")
        user_id = str(UserInfo().userID)
        if user_id == "-1":
            return 'AUTHORIZATION_ERROR: Authorization is required'

        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            self.__db.insert(
                f"""INSERT INTO Posts (user_id, image_id, video_id, post_text, likes, dislikes, post_time) \
                    VALUES  ({user_id}, {image_id}, {video_id}, '{text}', 0, 0, '{vl_time}');""")
        return None

    def getPostIds(self, sort_by_time=False, sort_by_likes=False, search_by_key=None):
        if sort_by_time:
            if not self.__db.connect():
                return 'CONNECTION_ERROR: Check your internet connection'
            else:
                post_info = self.__db.select(f"""SELECT post_id FROM Posts ORDER BY (post_time) DESC;""")
        elif sort_by_likes:
            if not self.__db.connect():
                return 'CONNECTION_ERROR: Check your internet connection'
            else:
                post_info = self.__db.select(f"""SELECT post_id FROM Posts ORDER BY (likes) DESC;""")
        elif search_by_key is not None:
            if not self.__db.connect():
                return 'CONNECTION_ERROR: Check your internet connection'
            else:
                post_info = self.__db.select(f"""SELECT post_id FROM Posts WHERE post_text LIKE '%{search_by_key}%';""")
        else:
            if not self.__db.connect():
                return 'CONNECTION_ERROR: Check your internet connection'
            else:
                post_info = self.__db.select(f"""SELECT post_id FROM Posts;""")

        if post_info == ():
            return 'SEARCH_ERROR: Posts with this id were not found'

        ids = []
        for i in post_info:
            ids.append(i['post_id'])

        return ids

    def getPostInfo(self, post_ids):

        if not self.__db.connect():
            return 'CONNECTION_ERROR: Check your internet connection'
        else:
            posts_info = self.__db.select(f"""SELECT * FROM Posts \
                                          WHERE post_id IN ({', '.join([str(i) for i in list(post_ids)])});""")

        for i in range(len(posts_info)):
            server_datetime = utc.localize(datetime.strptime(posts_info[i]['post_time'], "%Y-%m-%d %H:%M:%S"))
            posts_info[i]['post_time'] = server_datetime.astimezone(timezone(str(tzlocal.get_localzone()))).strftime(
                "%I:%M %p - %d %b %Y")

        return posts_info

# Example to using
# p = PostTools()
# print(p.createPost("я руся", 19, 45))
# ids = p.getPostIds(sort_by_time=True)
# print(p.getPostInfo(ids))
