import pymysql


class DB:
    HOST = "127.0.0.1"
    USER = "root"
    PASSWORD = "root"
    DATABASE = "Game"

    # HOST = "rds068v4i0ni5xbccq32.mysql.rds.aliyuncs.com"
    # USER = "nick"
    # PASSWORD = "Nick_game28"
    # DATABASE = "game"

    def __init__(self):
        self.db = pymysql.connect(DB.HOST, DB.USER, DB.PASSWORD, DB.DATABASE)

    def select_all(self, sql):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close()

    def select_one(self, sql):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            return cursor.fetchone()
        finally:
            cursor.close()

    def insert(self, sql):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()
        finally:
            cursor.close()
