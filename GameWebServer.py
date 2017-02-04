from flask import Flask, jsonify, abort, request

from DBHelper import DBHelper
import Logger

app = Flask(__name__)
dbHelper = DBHelper()
games = ["pc28", "crazy28", "korea28", "speed16"]


def check_game_name(game_name):
    if game_name is None or game_name.isspace() or \
            (game_name.lower() not in games):
        return False
    return True


@app.route('/count')
def get_count():
    dic = {}
    for t in games:
        table_name = "tb_{}".format(t.lower())
        count = dbHelper.select_count(table_name)
        dic[t] = count
    return jsonify({"code": 200, "count": dic})


@app.route('/maxid/<game_name>')
def get_max_id(game_name):
    if not check_game_name(game_name):
        abort(404)

    table_name = "tb_{}".format(game_name.lower())
    id = dbHelper.select_max_id(table_name)
    return jsonify({"code": 200, "maxid": str(id)})


@app.route('/recent10/<game_name>')
def get_recent_10_rounds(game_name):
    if game_name != "all":
        if not check_game_name(game_name):
            abort(404)

    if game_name == "all":
        pc_list = get_rows_from_table("tb_pc28")
        crazy_list = get_rows_from_table("tb_crazy28")
        korea_list = get_rows_from_table("tb_korea28")
        speed_list = get_rows_from_table("tb_speed16")
        return jsonify({"code": 200, "pc28_count": len(pc_list), "pc28_items": pc_list,
                        "crazy28_count": len(crazy_list), "crazy28_items": crazy_list,
                        "korea28_count": len(korea_list), "korea28_items": korea_list,
                        "speed16_count": len(speed_list), "speed_items": speed_list})
    else:
        table_name = "tb_{}".format(game_name.lower())
        sql = DBHelper.SELECT_ROWS_SQL.format(table_name) + " order by r_id desc limit 0,10"
        row_list = dbHelper.select_all(sql)
        return jsonify({"code": 200, "count": len(row_list), "items": row_list})


def get_rows_from_table(table_name):
    sql = DBHelper.SELECT_ROWS_SQL.format(table_name) + " order by r_id desc limit 0,10"
    row_list = dbHelper.select_all(sql)
    return row_list


@app.route('/rounds', methods=["post"])
def get_rounds():
    r_json = request.json
    game_name = r_json["game"]
    if not check_game_name(game_name):
        abort(404)
    table_name = "tb_{}".format(game_name.lower())
    start_date = end_date = start_id = end_id = None
    if "startdate" in r_json:
        start_date = r_json["startdate"]
    if "enddate" in r_json:
        end_date = r_json["enddate"]
    if "startid" in r_json:
        start_id = r_json["startid"]
    if "endid" in r_json:
        end_id = r_json["endid"]
    sql = DBHelper.SELECT_ROWS_SQL.format(table_name)
    sql_where = None
    if start_date is not None and not start_date.isspace():
        sql_where = "  where r_date >=" + repr(start_date)
    if end_date is not None and not end_date.isspace():
        if sql_where is None:
            sql_where = "  where r_date <=" + repr(end_date)
        else:
            sql_where += " and  r_date <=" + repr(end_date)
    if start_id is not None:
        if sql_where is None:
            sql_where = "  where r_id >={}".format(start_id)
        else:
            sql_where += " and  r_id >={}".format(start_id)
    if end_id is not None:
        if sql_where is None:
            sql_where = "  where r_id <={}".format(end_id)
        else:
            sql_where += " and  r_id <={}".format(end_id)
    sql += sql_where
    row_list = dbHelper.select_all(sql)
    return jsonify({"code": 200, "count": len(row_list), "items": row_list})


@app.route('/')
def index():
    return "Hello, Game28!"


if __name__ == '__main__':
    if Logger.IS_DEBUG:
        Logger.info("/-------  开始调试模式 ------/")
        app.run(debug=True)
    else:
        Logger.info("/***** 开始产品模式 *****/ ")
        app.run(host="0.0.0.0")
