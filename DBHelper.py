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
        rows = self.db.select_one(sql)
        if rows[0] is not None:
            result = rows[0]
        return result

    def select_max_id(self, table):
        result = 0
        sql = DBHelper.SELECT_MAX_ID_SQL.format(table)
        rows = self.db.select_one(sql)
        if rows[0] is not None:
            result = rows[0]
        return result

    def select_all(self, sql):
        rows = self.db.select_all(sql)
        row_list = []
        for item in rows:
            row_list.append({'id': item[0], 'date': str(item[1]), 'value': item[2]})
        return row_list

    def insert(self, table, rows):
        sql = DBHelper.INSERT_SQL.format(table)
        for row in rows:
            sql += DBHelper.INSERT_VALUE_SQL.format(row[0], row[1], row[2])
        if sql.endswith(","):
            sql = sql[0: -1] + ";"
        self.db.insert(sql)
