from DB import DB


class DBHelper:
    INSERT_SQL = "insert into {}(r_id,r_date,r_value) values "
    INSERT_VALUE_SQL = " ({},'{}',{}),"
    SELECT_MAX_ID_SQL = "select max(r_id) from {}"
    SELECT_COUNT_SQL = "select count(*) from {}"
    SELECT_ROWS_SQL = "select r_id,r_date,r_value from {}"

    def __init__(self):
        self.db = DB()

    def select_count(self, table):
        result = 0
        sql = DBHelper.SELECT_COUNT_SQL.format(table)
        row = self.db.select_one(sql)
        if row[0] is not None:
            result = row[0]
        return result

    def select_max_id(self, table):
        result = 0
        sql = DBHelper.SELECT_MAX_ID_SQL.format(table)
        row = self.db.select_one(sql)
        if row[0] is not None:
            result = row[0]
        return result

    def select_all(self, sql):
        result = self.db.select_all(sql)
        return result

    def insert(self, table, rows):
        sql = DBHelper.INSERT_SQL.format(table)
        for row in rows:
            sql += DBHelper.INSERT_VALUE_SQL.format(row[0], row[1], row[2])
        if sql.endswith(","):
            sql = sql[0: -1] + ";"
        self.db.insert(sql)
