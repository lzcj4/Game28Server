import datetime
import os

import bs4

import Logger
from DBHelper import DBHelper
from RoundModel import RoundModel
from Rule.DaBianRule import DaBianRule
from Rule.DaRule import DaRule
from Rule.DanRule import DanRule
from Rule.ShuangRule import ShuangRule
from Rule.XiaoBianRule import XiaoBianRule
from Rule.XiaoRule import XiaoRule
from Rule.ZhongRule import ZhongRule
from Rule.BianRule import BianRule
from WebCrawler import WebCrawler


class GameBase:
    HOST = "http://www.juxiangyou.com/"
    LOGIN_INDEX_URL = HOST + "fun/play/crazy28/index"
    VERIFY_URL = HOST + "verify"
    LOGIN_POST_URL = HOST + "login/auth"
    VERIFY_CODE_FILE_PATH = "/Img/verifyCode.png"
    LOGIN_CODE_SUCCEED = 10000
    LOAD_PAGES = 50
    webCrawler = WebCrawler()

    def __init__(self, is_auto_fire=False):
        self.dbHelper = DBHelper()
        """最近开的期"""
        self.latestRound = None
        """正在进去期"""
        self.runningRound = None
        self.count_zhong = 0
        self.count_bian = 0
        self.count_xiao_bian = 0
        self.count_da_bian = 0
        self.is_internal_logged = False

        self.rules = []
        if is_auto_fire:
            self.rules.append(XiaoBianRule(self))
            self.rules.append(ZhongRule(self))
            self.rules.append(DaBianRule(self))
            self.rules.append(BianRule(self))
            self.rules.append(DanRule(self))
            self.rules.append(ShuangRule(self))
            self.rules.append(XiaoRule(self))
            self.rules.append(DaRule(self))
            # if GameBase.webCrawler is None:
            #     GameBase.webCrawler = WebCrawler()

    def get_http(self):
        return GameBase.webCrawler

    def get_header(self):
        return GameBase.get_static_header()

    @staticmethod
    def get_static_header():
        headers = {"Host": "www.juxiangyou.com",
                   "Referer": "http://www.juxiangyou.com/",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2914.3 Safari/537.36",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Upgrade-Insecure-Requests": "1",
                   "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
                   "Accept-Encoding": "gzip, deflate, sdch"}
        return headers

    @staticmethod
    def get_verify_code():
        r = GameBase.webCrawler.get(GameBase.LOGIN_INDEX_URL, GameBase.get_static_header())
        if "游戏期号" in r.text:
            GameBase.close_request(r)
            return True
        r.close()
        r = GameBase.webCrawler.get(GameBase.VERIFY_URL, GameBase.get_static_header())
        verify_img = os.path.curdir + GameBase.VERIFY_CODE_FILE_PATH
        if r.status_code == 200:
            # if os.path.exists(verify_img):
            #     os.remove(verify_img)
            with open(verify_img, 'wb+') as f:
                for block in r.iter_content(1024):
                    f.write(block)
                Logger.info("当前验证码路径:{}".format(os.path.abspath(verify_img)))

        GameBase.close_request(r)
        return False

    @staticmethod
    def close_request(r):
        if r is not None:
            r.close

    @staticmethod
    def login(user, pwd, verify_code):
        data = (
            "jxy_parameter=%7B%22c%22%3A%22index%22%2C%22fun%22%3A%22login%22%2C%22account%22%3A%22{}%22%2C%22password" + \
            "%22%3A%22{}%22%2C%22verificat_code%22%3A%22{}%22%2C%22is_auto%22%3Atrue%7D").format(
            user, pwd, verify_code)
        header = GameBase.get_static_header()
        header["Referer"] = "http://www.juxiangyou.com/login/index?redirectUrl=/fun/play/crazy28/index"
        r = GameBase.webCrawler.post(GameBase.LOGIN_POST_URL, data, header)
        Logger.info(r.text)
        a = r.json()["code"]
        GameBase.close_request(r)
        return GameBase.LOGIN_CODE_SUCCEED == a

    @staticmethod
    def login_action():
        is_login = GameBase.get_verify_code()
        if not is_login:
            code = input("请录入登录信息，格式 用户名  密码   验证码：  ")
            user, pwd, code = code.split()
            is_login = GameBase.login(user, pwd, code)
        if not is_login:
            Logger.info("用户登录失败，请检查录入是否出错")
        return is_login

    def get_game_url(self):
        pass

    def get_table_name(self):
        pass

    def get_game_name(self):
        pass

    def get_rounds(self):
        # if not GameBase.login_action():
        #     return
        return self.get_pages(GameBase.LOAD_PAGES)

    def get_pages(self, page_num):
        table_name = self.get_table_name()
        game_name = self.get_game_name()
        max_round = self.dbHelper.select_max_id(table_name)
        if self.runningRound is not None:
            if datetime.datetime.now().minute - self.runningRound.date.minute < 1:
                '''去除太多重复日志'''
                if not self.is_internal_logged:
                    Logger.info("游戏：{0}，当前期{1}还没有开奖，直接返回 {2}".format(
                        game_name, self.runningRound.id, datetime.datetime.now()))
                    self.is_internal_logged = True
                return False

        self.is_internal_logged = False
        is_end = False

        latest_round = None
        running_round = None

        for page in range(page_num):
            url = ("http://www.juxiangyou.com/fun/play/interaction/?jxy_parameter=%7B%22c%22%3A%22quiz%22%2C%22" + \
                   "fun%22%3A%22getEachList%22%2C%22items%22%3A%22{}%22%2C%22pageSize%22%3A20%2C%22" + \
                   "pageIndex%22%3A{}%7D&xtpl=fun%2Fprivate%2Fjc-index-tbl&params%5Bitems%5D={}"). \
                format(game_name, page + 1, game_name)
            r = GameBase.webCrawler.get(url, self.get_header())
            try:
                json = r.json()
            except Exception as e:
                if r is None:
                    Logger.error("JSON 解析出错:{0},JSON为空没法获取".format(e))
                else:
                    Logger.error("JSON 解析出错:{0},{1}".format(e, r.text))
                continue
            finally:
                GameBase.close_request(r)

            rounds = []
            if json is None or "itemList" not in json:
                continue

            # 数据是按时间倒序
            for item in json["itemList"]:
                num = int(item["num"])
                temp_round = RoundModel(int(item["num"]), "{0}-{1}".format(datetime.datetime.now().year, item["date"]),
                                        item["jcjg2"])

                # 如果有多于一条历史记录时，这个会成为最早的记录，并非最近结束期号
                if page == 0:
                    if item["iskj"]:
                        if latest_round is None:
                            latest_round = temp_round
                    else:
                        running_round = temp_round

                if item["iskj"]:
                    if num <= max_round:
                        is_end = True
                        # Logger.info("开奖期号遍历结束，当前最新期号:{0}-{1}".format(max_round, game_name))
                        break
                    else:
                        rounds.append(
                            [num, "{0}-{1}".format(datetime.datetime.now().year, item["date"]), item["jcjg2"]])

            if len(rounds) > 0:
                self.dbHelper.insert(table_name, rounds)
                if len(rounds) == 1:
                    Logger.info("历史数据 {0} 值：{1}".format(game_name, rounds[0]))
                else:
                    Logger.info("{0} - 历史数据 {1}:{2}条".format(datetime.datetime.now(), game_name, len(rounds)))
            if is_end:
                break

        self.latestRound = latest_round
        self.runningRound = running_round
        return True

    def get_rows(self, html):
        """
    <tr>
        <td>589161</td>
        <td>01-16 09:41</td>
        <td class="num">

            0+1+5=<span class="ball-num">6</span>

        </td>
        <td>
            8,617,616,861<span class="udou"></span>
        </td>
        <td style="color:#ff4c4c">

            <a style="color:#ff4c4c" class="win-list" href="/fun/play/crazy28/zjrs?id=589161">359</a>

        </td>
        <td class="st-td">
            <span class="udou"></span>
            <span class="shou kui">收：0</span><br />
            <span class="jing">竞：0</span>
        </td>
        <td>

            <span class="yikai">已开奖</span>

        </td>
    </tr>
        :param html:  html get from crazy28 index page
        :return: 每条记录：期号，时间，数值
        """
        bs = bs4.BeautifulSoup(html, "lxml")
        result = []
        for row in bs.table.children:
            if row == "\n":
                continue
            item = []
            i = 0
            for td in row.children:
                if td == "\n":
                    continue
                if i == 0:
                    if td.text.isdigit():
                        id = int(td.text)
                        if id <= self.max_round:
                            return result
                        item.append(id)
                    else:
                        break
                elif i == 1:
                    item.append("{}-{}".format(datetime.datetime.now().year, td.text))
                    pass
                elif i == 2 and "class" in td.attrs and td.attrs["class"][0] == 'num' \
                        and len(td.contents) == 3:
                    span = td.contents[1]
                    if span != "\n" and "class" in span.attrs and span.attrs["class"][0] == "ball-num" and \
                            span.text.isdigit():
                        item.append(int(span.text))
                        break
                    else:
                        item = []
                i += 1

            if len(item) > 0:
                result.append(item)
        return result

    def post_next_round(self):
        for item in self.rules:
            item.start()
        pass
