import pymysql
import Logger


class DB:
    LOCAL_HOST = "127.0.0.1"
    LOCAL_USER = "root"
    LOCAL_PASSWORD = "root"
    LOCAL_DATABASE = "Game"

    HOST = "rds068v4i0ni5xbccq32.mysql.rds.aliyuncs.com"
    USER = "nick"
    PASSWORD = "Nick_game28"
    DATABASE = "game28"

    def __init__(self):
        try:
            if Logger.IS_DEBUG:
                self.db = pymysql.connect(DB.LOCAL_HOST, DB.LOCAL_USER, DB.LOCAL_PASSWORD, DB.LOCAL_DATABASE)
            else:
                self.db = pymysql.connect(DB.HOST, DB.USER, DB.PASSWORD, DB.DATABASE)
        except pymysql.err.Error as err:
            Logger.error("mysql 建立连接异常:{}".format(err))

    def select_all(self, sql):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except pymysql.err.Error as err:
            Logger.error("mysql select_all异常:{}".format(err))
        finally:
            cursor.close()

    def select_one(self, sql):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            return cursor.fetchone()
        except pymysql.err.Error as err:
            Logger.error("mysql select_one异常:{}".format(err))
        finally:
            cursor.close()

    def insert(self, sql):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()
        except pymysql.err.Error as err:
            Logger.error("mysql insert异常:{}".format(err))
        finally:
            cursor.close()
