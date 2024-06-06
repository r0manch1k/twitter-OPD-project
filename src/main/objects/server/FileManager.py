import os
import uuid
import atexit
import ftplib
import shutil
import tempfile
from ftplib import FTP
from functools import partial

from .Result import generateResult
from .Static import getConfigInfo
from src.main.objects.server.DataBase import DataBase


class Singleton:
    _instance = None

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance


class FileManager(Singleton):
    def __init__(self):

        self.__host = getConfigInfo('ftp_server', 'host')
        self.__user = getConfigInfo('ftp_server', 'user')
        self.__passwd = getConfigInfo('ftp_server', 'password')

        self.__db = DataBase()
        self.__ftp = FTP(self.__host)

        self.__tempDir = None

        atexit.register(self.__clear)

    @property
    def tempPath(self):

        if self.__tempDir:
            return self.__tempDir + "/"

        self.__createTempDir()
        return self.__tempDir + "/"

    def __createTempDir(self) -> None:

        self.__tempDir = os.path.abspath(tempfile.mkdtemp(dir="../../", prefix="."))

    def getFilePath(self, imageID: int = None, videoID: int = None) -> dict:

        if not imageID and videoID:
            raise ValueError("Wrong parameters: imageID, videoID are both null!")
        elif imageID and videoID:
            raise ValueError("Wrong parameters: imageID, videoID are both not null!")
        elif (imageID and imageID < 1) or (videoID and videoID < 1):
            raise ValueError("Wrong parameters: ID must be positive number!")

        if not self.__tempDir:
            self.__createTempDir()

        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")

        if imageID:
            row = self.__db.select(f"SELECT path FROM Images WHERE image_id = {imageID}")[0]
            UUID = row["path"].split(".")[0]
        else:
            row = self.__db.select(f"SELECT path FROM Videos WHERE video_id = {videoID}")[0]
            UUID = row["path"].split(".")[0]

        if imageID:
            fileType = ".png"
        else:
            fileType = ".mp4"

        path = "/" + "/".join(UUID[i:i + 2] for i in range(0, len(UUID), 2)) + "/"

        makeDirectory = partial(os.makedirs, exist_ok=True)
        makeDirectory(self.__tempDir + path)

        try:

            with open(self.__tempDir + path + UUID + fileType, "rb") as _:
                pass

        except FileNotFoundError:

            try:
                self.__ftp.login(user=self.__user, passwd=self.__passwd)

            except AttributeError:
                self.__ftp = FTP(self.__host)
                self.__ftp.login(user=self.__user, passwd=self.__passwd)

            with open(self.__tempDir + path + UUID + fileType, "wb") as file:
                self.__ftp.retrbinary("RETR " + path + UUID + fileType, file.write)

            self.__ftp.quit()

        return generateResult(data=self.__tempDir + path + UUID + fileType)

    def loadFile(self, fp: str, imageID: int = None, videoID: int = None) -> dict:
        """Takes imageID/videoID as argument. If imageID/videoID equals '1' it will add a new image/video to the tabel.
         Otherwise, it will replace an existing one.
         P.S. You won't change image with imageID = 1 using this function!"""

        if not imageID and videoID:
            raise ValueError("Wrong parameters: imageID, videoID both null!")
        elif imageID and videoID:
            raise ValueError("Wrong parameters: imageID, videoID both not null!")
        elif (imageID and imageID < 1) or (videoID and videoID < 1):
            raise ValueError("Wrong parameters: ID must be positive number!")

        try:
            with open(fp, "rb") as _:
                pass

        except FileNotFoundError:
            return generateResult("Invalid path to image", "format")

        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")

        if imageID and imageID > 1:
            row = self.__db.select(f"SELECT path FROM Images WHERE image_id = {imageID}")[0]
            UUID = row["path"].split(".")[0]
        elif videoID and videoID > 1:
            row = self.__db.select(f"SELECT path FROM Videos WHERE video_id = {videoID}")[0]
            UUID = row["path"].split(".")[0]
        else:
            UUID = str(uuid.uuid4())

        if imageID:
            fileType = ".png"
        else:
            fileType = ".mp4"

        path = "/" + "/".join(UUID[i:i + 2] for i in range(0, len(UUID), 2)) + "/"

        makeDirectory = partial(os.makedirs, exist_ok=True)
        makeDirectory(self.__tempDir + path)

        try:
            shutil.copy(fp, self.__tempDir + path + UUID + fileType)
        except shutil.SameFileError:
            pass

        try:
            self.__ftp.login(user=self.__user, passwd=self.__passwd)

        except AttributeError:
            self.__ftp = FTP(self.__host)
            self.__ftp.login(user=self.__user, passwd=self.__passwd)

        dirs = path.split("/")
        for i in range(2, len(dirs)):
            try:
                self.__ftp.mkd("/".join(dirs[0:i]))
            except ftplib.error_perm:
                pass

        for file in self.__ftp.nlst(path):
            try:
                self.__ftp.delete(file)
            except (ftplib.error_perm, ftplib.error_reply):
                pass

        with open(self.__tempDir + path + UUID + fileType, "rb") as file:
            self.__ftp.storbinary("STOR " + path + UUID + fileType, file)

        self.__ftp.quit()

        if imageID and imageID > 1:
            self.__db.insert(f"""UPDATE Images SET path = '{UUID + fileType}' WHERE image_id = {str(imageID)};""")
        elif imageID and imageID == 1:
            self.__db.insert(f"INSERT INTO Images (path) VALUES ('{UUID + fileType}')")
            imageID = self.__db.select(f"SELECT image_id FROM Images WHERE path = '{UUID + fileType}'")[0]["image_id"]

        if videoID and videoID > 1:
            self.__db.insert(f"""UPDATE Videos SET path = '{UUID + fileType}' WHERE image_id = {str(videoID)};""")
        elif videoID and videoID == 1:
            self.__db.insert(f"INSERT INTO Videos (path) VALUES ('{UUID + fileType}')")
            videoID = self.__db.select(f"SELECT video_id FROM Videos WHERE path = '{UUID + fileType}'")[0]["video_id"]

        if imageID:
            return generateResult(data=imageID)
        return generateResult(data=videoID)

    def deleteFile(self, imageID: int = None, videoID: int = None) -> dict:

        if not imageID and videoID:
            raise ValueError("Wrong parameters: imageID, videoID both null!")
        elif imageID and videoID:
            raise ValueError("Wrong parameters: imageID, videoID both not null!")
        elif (imageID and imageID < 1) or (videoID and videoID < 1):
            raise ValueError("Wrong parameters: ID must be positive number!")

        if not self.__db.connect():
            return generateResult("Check your internet connection", "connection")

        if imageID and imageID > 1:
            row = self.__db.select(f"SELECT path FROM Images WHERE image_id = {imageID}")[0]
            UUID = row["path"].split(".")[0]
        elif videoID and videoID > 1:
            row = self.__db.select(f"SELECT path FROM Videos WHERE video_id = {videoID}")[0]
            UUID = row["path"].split(".")[0]
        else:
            raise ValueError("Can't delete default imageID/videoID!")

        if imageID:
            fileType = ".png"
        else:
            fileType = ".mp4"

        path = "/" + "/".join(UUID[i:i + 2] for i in range(0, len(UUID), 2)) + "/"

        try:
            self.__ftp.login(user=self.__user, passwd=self.__passwd)

        except AttributeError:
            self.__ftp = FTP(self.__host)
            self.__ftp.login(user=self.__user, passwd=self.__passwd)

        self.__ftp.delete(path + UUID + fileType)
        dirs = path.split("/")
        for i in range(len(dirs) - 1, 1, -1):
            try:
                self.__ftp.rmd("/".join(dirs[0:i]))
            except ftplib.error_perm:
                pass

        self.__ftp.quit()

        if imageID:
            self.__db.insert(f"DELETE FROM Images WHERE image_id = {imageID};")
            self.__db.insert(f"UPDATE Users SET image_id = 1 WHERE image_id IS NULL")
        else:
            self.__db.insert(f"DELETE FROM Videos WHERE video_id = {videoID};")
            self.__db.insert(f"UPDATE Users SET video_id = 1 WHERE video_id IS NULL")

        return generateResult(data=1)

    def __clear(self) -> None:
        if self.__tempDir:
            shutil.rmtree(self.__tempDir, ignore_errors=True)

    def __del__(self):
        print("__del__ in FileManager has called")
        if self.__tempDir:
            shutil.rmtree(self.__tempDir, ignore_errors=True)
