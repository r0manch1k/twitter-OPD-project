import tzlocal
from src.main.objects.server.DataBase import DataBase
from src.main.objects.server.UserInfo import CurrentUser
from src.main.objects.server.Result import generateResult
from src.main.objects.server.Static import setConfigInfo, getConfigInfo
from src.main.objects.server.Validator import validateText, getValidString


class PostTools:
    def __init__(self):
        self.__db = DataBase()

    def createPost(self, post_text: str, image_id: int = None, video_id: int  = None):
        error = CurrentUser().updateOnline()
        if error["error"]:
            return error

        if validateText(post_text):
            return generateResult(validateText(post_text), "format")

        user_id = CurrentUser().userID['data']

        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            if image_id and video_id:
                self.__db.insert(
                    f"""INSERT INTO Posts (user_id, image_id, video_id, post_text, likes, dislikes, post_time) \
                        VALUES  ({user_id}, {image_id}, {video_id}, '{getValidString(post_text)}', 0, 0, NOW());""")
            elif image_id:
                self.__db.insert(
                    f"""INSERT INTO Posts (user_id, image_id, post_text, likes, dislikes, post_time) \
                        VALUES  ({user_id}, {image_id}, '{getValidString(post_text)}', 0, 0, NOW());""")
            elif video_id:
                self.__db.insert(
                    f"""INSERT INTO Posts (user_id, video_id, post_text, likes, dislikes, post_time) \
                        VALUES  ({user_id}, {video_id}, '{getValidString(post_text)}', 0, 0, NOW());""")
            else:
                self.__db.insert(
                    f"""INSERT INTO Posts (user_id, post_text, likes, dislikes, post_time) \
                        VALUES  ({user_id}, '{getValidString(post_text)}', 0, 0, NOW());""")
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
        error = CurrentUser().updateOnline()
        if error["error"]:
            return error

        if validateText(comment_text):
            return generateResult(validateText(comment_text), "format")
        
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            if self.__db.select(f"""SELECT likes FROM Posts WHERE post_id = {post_id};""") == ():
                return generateResult("This post isn't found", "format")

        user_id = CurrentUser().userID['data']

        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            self.__db.insert(
                f"""INSERT INTO Comments (post_id, user_id, comment_time, comment_text, likes, dislikes) \
                    VALUES  ({post_id}, {user_id}, NOW(), '{getValidString(comment_text)}', 0, 0);""")
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
        error = CurrentUser().updateOnline()
        if error["error"]:
            return error
        
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
            count_likes = self.__db.select(f"""SELECT likes FROM {table_name} WHERE {index} = {insert_value};""")[0]["likes"]
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            count_dislikes = self.__db.select(f"""SELECT dislikes FROM {table_name} WHERE {index} = {insert_value};""")[0]["dislikes"]

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
                    return generateResult(data={"like": {"set": True, "count": count_likes + 1},
                                                "dislike": {"set": False, "count": count_dislikes}})
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
                    return generateResult(data={"like": {"set": False, "count": count_likes}, 
                                                "dislike": {"set": True, "count": count_dislikes + 1}})
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
                        return generateResult(data={"like": {"set": False, "count": count_likes - 1}, 
                                                    "dislike": {"set": False, "count": count_dislikes}})
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
                        return generateResult(data={"like": {"set": True, "count": count_likes + 1}, 
                                                    "dislike": {"set": False, "count": count_dislikes - 1}})
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
                        return generateResult(data={"like": {"set": False, "count": count_likes}, 
                                                    "dislike": {"set": False, "count": count_dislikes - 1}})
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
                        return generateResult(data={"like": {"set": False, "count": count_likes - 1}, 
                                                    "dislike": {"set": True, "count": count_dislikes + 1}})
    
    def checkReaction(self, post_id=-1, comment_id=-1):
        error = CurrentUser().updateOnline()
        if error["error"]:
            return error
        
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
            return generateResult()
        else:
            return generateResult(data=reaction[0]['reaction'])
            
    def getPostIds(self, sort_by_likes=False, sort_by_dislikes=False, sort_by_comments=False, sort_by_all_reactions=False, search_by_key=""):
        if sort_by_likes:
            if not self.__db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                post_ids = self.__db.select("""SELECT post_id FROM Posts \
                                               ORDER BY (likes) DESC;""")
        elif sort_by_dislikes:
            if not self.__db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                post_ids = self.__db.select("""SELECT post_id FROM Posts \
                                               ORDER BY (dislikes) DESC;""")
        elif sort_by_comments:
            if not self.__db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                post_ids = self.__db.select("""SELECT post_id FROM Posts \
                                               ORDER BY \
                                               (SELECT COUNT(comment_id) FROM Comments WHERE Comments.post_id = Posts.post_id) \
                                               DESC;""")
        elif sort_by_all_reactions:
            if not self.__db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                post_ids = self.__db.select("""SELECT post_id FROM Posts \
                                               ORDER BY \
                                               ((SELECT COUNT(comment_id) FROM Comments WHERE Comments.post_id = Posts.post_id) + Posts.likes) \
                                               DESC;""")
        elif search_by_key != "":
            if not self.__db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                search_by_key = search_by_key.replace("'", "''")
                post_ids = self.__db.select(f"""SELECT post_id FROM Posts \
                                                WHERE post_text LIKE '%{search_by_key}%';""") 
        else:
            if not self.__db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                post_ids = self.__db.select("""SELECT post_id FROM Posts \
                                               ORDER BY (post_time) DESC;""")
        ids = []
        for i in post_ids:
            ids.append(i['post_id'])

        return generateResult(data=ids)

    def getPostsInfo(self, post_ids: list):
        local_tz = str(tzlocal.get_localzone())
        followingsIds = CurrentUser().followingsIds["data"]
        
        posts_info = []
        for post_id in post_ids:
            if not self.__db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                post_info = self.__db.select(
                    f"""SELECT Posts.post_id, \
                            Posts.image_id, \
                            Posts.video_id, \
                            Posts.post_text, \
                            Posts.likes, \
                            Posts.dislikes, \
                            DATE_FORMAT(CONVERT_TZ(Posts.post_time, @@SESSION.TIME_ZONE, '{local_tz}'), '%I:%i %p - %d %b %Y') AS post_time, \
                            Posts.user_id, \
                            Users.username, \
                            Users.name, \
                            Users.image_id, \
                            Users.access \
                        FROM Posts \
                        INNER JOIN Users \
                            ON Posts.user_id = Users.user_id \
                        WHERE Posts.post_id = {post_id};""")[0]

            if post_info["user_id"] in followingsIds:
                post_info["is_following"] = True
            else:
                post_info["is_following"] = False

            if not self.__db.connect():
                return generateResult("Check your internet connection", "connection")
            else:
                comments_info = self.__db.select(
                    f"""SELECT Comments.comment_id, \
                            Comments.post_id, \
                            Comments.user_id, \
                            Comments.comment_text, \
                            DATE_FORMAT(CONVERT_TZ(Comments.comment_time, @@SESSION.TIME_ZONE, '{local_tz}'), '%I:%i %p - %d %b %Y') AS comment_time, \
                            Comments.likes, \
                            Comments.dislikes, \
                            Users.user_id, \
                            Users.username, \
                            Users.name, \
                            Users.image_id, \
                            Users.access \
                        FROM Comments \
                        INNER JOIN Users \
                            ON Comments.user_id = Users.user_id \
                        WHERE Comments.post_id = {post_id} \
                        ORDER BY (Comments.comment_time) ASC;""")
                if comments_info != ():
                    for comment in range(len(comments_info)):
                        if comments_info[comment]["user_id"] in followingsIds:
                            comments_info[comment]["is_following"] = True
                        else:
                            comments_info[comment]["is_following"] = False
                    post_info["comments"] = comments_info
                else:
                    post_info["comments"] = None
            posts_info.append(post_info)

        return generateResult(data=posts_info)
    
    def checkNewPosts(self):
        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")
        else:
            max_post_id = self.__db.select("""SELECT post_id FROM Posts \
                                              WHERE post_time = (SELECT MAX(post_time) FROM Posts);""")
            if max_post_id == ():
                return generateResult(data=False)
            max_post_id = max_post_id[0]['post_id']

        if str(max_post_id) != str(getConfigInfo('const', 'last_post_id')):
            setConfigInfo('const', 'last_post_id', str(max_post_id))
            return generateResult(data=True)
        return generateResult(data=False)


# EXAMPLES FOR USING

# post_tools = PostTools()

# CREATE POST
# post_tools.createPost(post_text="wassupski")

# DELETE POST
# post_tools.deletePost(post_id=1)

# CREATE COMMENT
# post_tools.createComment(comment_text="assalamuallykum", post_id=2)

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
# post_tools.getPostIds() -> for get all post sorted by time 
# post_tools.getPostIds(sort_by_likes=True)
# post_tools.getPostIds(sort_by_comments=True)
# post_tools.getPostIds(sort_by_likes_comments=True)
# post_tools.getPostIds(search_by_key="some words")

# GET POSTS INFO
# post_tools.getPostsInfo(post_ids=[1, 2, 3, 4]) -> for get information about posts by id with user information and comments

# CHECK NEW POSTS
# post_tools.checkNewPosts() -> to check for new posts
