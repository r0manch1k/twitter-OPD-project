import tzlocal
from datetime import datetime
from pytz import timezone, utc
from src.main.objects.server.DataBase import DataBase
from src.main.objects.server.UserInfo import CurrentUser
from src.main.objects.server.Result import generateResult
from src.main.objects.server.Validator import validateText
from src.main.objects.server.Authorization import Authorization


class PostTools:
    def __init__(self):
        self.__db = DataBase()

    def createPost(self, post_text: str, image_id: int, video_id: int):
        message = Authorization().checkAuthorization()
        if message["errors"]:
            return message

        if validateText(post_text):
            return generateResult(validateText(post_text), "format")

        utc_time = datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S")
        fixed_post_text = post_text.replace("'", "''")
        user_id = CurrentUser().userID['data']

        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            self.__db.insert(
                f"""INSERT INTO Posts (user_id, image_id, video_id, post_text, likes, dislikes, post_time) \
                    VALUES  ({user_id}, {image_id}, {video_id}, '{fixed_post_text}', 0, 0, '{utc_time}');""")
        return generateResult()

    def deletePost(self, post_id: int):
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            if self.__db.select(f"""SELECT * FROM Posts WHERE post_id = {post_id};""") == ():
                return generateResult("This object isn't found", "format")
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            comment_ids = self.__db.select(
                f"""SELECT comment_id FROM Comments 
                    WHERE post_id = {post_id};""")
            ids = []
            for i in comment_ids:
                ids.append(i['comment_id'])
            if ids != []:
                if not self.__db.connect():
                    return generateResult("Check your internet connection", "connection")
                else:
                    self.__db.insert(
                    f"""DELETE FROM Reactions WHERE comment_id IN ({', '.join([str(i) for i in ids])});""")
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            self.__db.insert(
            f"""DELETE FROM Comments WHERE post_id = {post_id};""")
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            self.__db.insert(
            f"""DELETE FROM Reactions WHERE post_id = {post_id};""")
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            self.__db.insert(
            f"""DELETE FROM Posts WHERE post_id = {post_id};""")

        return generateResult()

    def createComment(self, comment_text: str, post_id: int):
        message = Authorization().checkAuthorization()
        if message["errors"]:
            return message

        if validateText(comment_text):
            return generateResult(validateText(comment_text), "format")

        utc_time = datetime.now(utc).strftime("%Y-%m-%d %H:%M:%S")
        fixed_comment_text = comment_text.replace("'", "''")
        user_id = CurrentUser().userID['data']

        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            self.__db.insert(
                f"""INSERT INTO Comments (post_id, user_id, comment_time, comment_text, likes, dislikes) \
                    VALUES  ({post_id}, {user_id}, '{utc_time}', '{fixed_comment_text}', 0, 0);""")
        return generateResult()

    def deleteComment(self, comment_id: int):
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            if self.__db.select(f"""SELECT * FROM Comments WHERE comment_id = {comment_id};""") == ():
                return generateResult("This object isn't found", "format")
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            self.__db.insert(
            f"""DELETE FROM Reactions WHERE comment_id = {comment_id};""")
            
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            self.__db.insert(
            f"""DELETE FROM Comments WHERE comment_id = {comment_id};""")

        return generateResult()

    def createReaction(self, post_id=-1, comment_id=-1, is_like=False, is_dislike=False):
        message = Authorization().checkAuthorization()
        if message["errors"]:
            return message
        
        user_id = CurrentUser().userID['data']
        if post_id != -1:
            table_name = "Posts"
            index = "post_id"
            insert_value = post_id
        elif comment_id != -1:
            table_name = "Comments"
            index = "comment_id"
            insert_value = comment_id
        else:
            return generateResult("The index was not entered", "format")
        if not is_like and not is_dislike:
            return generateResult("The type of reaction was not entered", "format")
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            if self.__db.select(f"""SELECT * FROM {table_name} WHERE {index} = {insert_value};""") == ():
                return generateResult("This object isn't found", "format")

        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            server_reaction = self.__db.select(
                f"""SELECT reaction FROM Reactions
                    WHERE user_id = {str(user_id)} AND {index} = {str(insert_value)};""")
            if server_reaction == ():
                if is_like:
                    if not self.__db.connect():
                        return generateResult("Check your internet connection", "connection")
                    else:
                        self.__db.insert(
                            f"""INSERT INTO Reactions (user_id, {index}, reaction) \
                                VALUES  ({str(user_id)}, {str(insert_value)}, '{"like"}');""")
                    if not self.__db.connect():
                        return generateResult("Check your internet connection", "connection")
                    else:
                        self.__db.insert(
                            f"""UPDATE {table_name} SET likes = likes + 1 \
                                WHERE {index} = {str(insert_value)};""")
                if is_dislike:
                    if not self.__db.connect():
                        return generateResult("Check your internet connection", "connection")
                    else:
                        self.__db.insert(
                            f"""INSERT INTO Reactions (user_id, {index}, reaction) \
                                VALUES  ({str(user_id)}, {str(insert_value)}, '{"dislike"}');""")
                    if not self.__db.connect():
                        return generateResult("Check your internet connection", "connection")
                    else:
                        self.__db.insert(
                            f"""UPDATE {table_name} SET dislikes = dislikes + 1 \
                                WHERE {index} = {str(insert_value)};""")
            else:
                server_reaction = server_reaction[0]['reaction']
                if is_like:
                    if server_reaction == "like":
                        if not self.__db.connect():
                            return generateResult("Check your internet connection", "connection")
                        else:
                            self.__db.insert(
                                f"""DELETE FROM Reactions
                                    WHERE user_id = {str(user_id)} AND {index} = {str(insert_value)};""")
                        if not self.__db.connect():
                            return generateResult("Check your internet connection", "connection")
                        else:
                            self.__db.insert(
                                f"""UPDATE {table_name} SET likes = likes - 1 \
                                    WHERE {index} = {str(insert_value)};""")
                    if server_reaction == "dislike":
                        if not self.__db.connect():
                            return generateResult("Check your internet connection", "connection")
                        else:
                            self.__db.insert(
                                f"""UPDATE Reactions SET reaction = '{"like"}'
                                    WHERE user_id = {str(user_id)} AND {index} = {str(insert_value)};""")
                        if not self.__db.connect():
                            return generateResult("Check your internet connection", "connection")
                        else:
                            self.__db.insert(
                                f"""UPDATE {table_name} SET dislikes = dislikes - 1, likes = likes + 1 \
                                    WHERE {index} = {str(insert_value)};""")
                if is_dislike:
                    if server_reaction == "dislike":
                        if not self.__db.connect():
                            return generateResult("Check your internet connection", "connection")
                        else:
                            self.__db.insert(
                                f"""DELETE FROM Reactions
                                    WHERE user_id = {str(user_id)} AND {index} = {str(insert_value)};""")
                        if not self.__db.connect():
                            return generateResult("Check your internet connection", "connection")
                        else:
                            self.__db.insert(
                                f"""UPDATE {table_name} SET dislikes = dislikes - 1 \
                                    WHERE {index} = {str(insert_value)};""")
                    if server_reaction == "like":
                        if not self.__db.connect():
                            return generateResult("Check your internet connection", "connection")
                        else:
                            self.__db.insert(
                                f"""UPDATE Reactions SET reaction = '{"dislike"}'
                                    WHERE user_id = {str(user_id)} AND {index} = {str(insert_value)};""")
                        if not self.__db.connect():
                            return generateResult("Check your internet connection", "connection")
                        else:
                            self.__db.insert(
                                f"""UPDATE {table_name} SET likes = likes - 1, dislikes = dislikes + 1 \
                                    WHERE {index} = {str(insert_value)};""")
        return generateResult()
    
    def checkReaction(self, post_id=-1, comment_id=-1):
        user_id = CurrentUser().userID['data']
        if post_id != -1:
            index = "post_id"
            table_name = "Posts"
            insert_value = post_id
        elif comment_id != -1:
            index = "comment_id"
            table_name = "Comments"
            insert_value = comment_id
        else:
            return generateResult("The index was not entered", "format")
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            if self.__db.select(f"""SELECT * FROM {table_name} WHERE {index} = {insert_value};""") == ():
                return generateResult("This object isn't found", "format")
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            reaction = self.__db.select(
                f"""SELECT reaction FROM Reactions 
                    WHERE user_id = {user_id} AND {index} = {insert_value};""")
        
        if reaction == ():
            return generateResult("No reactions on this object", "format")
        else:
            return generateResult(data=reaction[0]['reaction'])
            

    def getPostIds(self, sort_by_time=False, sort_by_likes=False, search_by_key=None):
        if sort_by_time:
            if not self.__db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                post_ids = self.__db.select("""SELECT post_id FROM Posts ORDER BY (post_time) DESC;""")
        elif sort_by_likes:
            if not self.__db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                post_ids = self.__db.select("""SELECT post_id FROM Posts ORDER BY (likes) DESC;""")
        elif search_by_key is not None:
            if not self.__db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                post_ids = self.__db.select(f"""SELECT post_id FROM Posts WHERE post_text LIKE '%{search_by_key}%';""")
        else:
            if not self.__db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                post_ids = self.__db.select("""SELECT post_id FROM Posts;""")

        if post_ids == ():
            return generateResult("Posts were not found", "format")

        ids = []
        for i in post_ids:
            ids.append(i['post_id'])

        return generateResult(data=ids)

    def getPostsInfo(self, post_ids: list):
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
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
            return generateResult("Check your internet connection", "connection")
        else:
            comments_info = self.__db.select(
                f"""SELECT Comments.comment_id, \
                           Comments.post_id, \
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

        return generateResult(data=dict_posts_info)


# EXAMPLES FOR USING

# post_tools = PostTools()

# CREATE POST
# post_tools.createPost(post_text="всем хай", image_id=666, video_id=69)

# DELETE POST
# post_tools.deletePost(post_id=1)

# CREATE COMMENT
# post_tools.createComment(comment_text="wassupski", post_id=1337)

# DELETE COMMENT
# post_tools.deleteComment(comment_id=1)

# CREATE REACTION
# post_tools.createReaction(post_id=1, is_like=True) -> for set like on post
# post_tools.createReaction(post_id=1, is_dislike=True) -> for set dislike on post
# post_tools.createReaction(comment_id=1, is_like=True) -> for set like on comment
# post_tools.createReaction(comment_id=1, is_dislike=True) -> for set dislike on comment

# CHECK REACTION
# post_tools.checkReaction(post_id=1) -> for check if there is a reaction to this post from current user
# post_tools.checkReaction(comment_id=1) -> for check if there is a reaction to this comment from current user

# GET POST IDS
# post_tools.getPostIds() -> for get all post ids without filters
# post_tools.getPostIds(sort_by_time=True)
# post_tools.getPostIds(sort_by_likes=True)
# post_tools.getPostIds(search_by_key=True)

# GET POSTS INFO
# post_tools.getPostsInfo(post_ids=[1, 2, 3, 4]) -> for get information about posts by id with user information and comments
