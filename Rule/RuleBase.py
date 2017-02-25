import Logger
import datetime
from termcolor import colored


class RuleBase:
    XIAO_BIAN_VALUES = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    ZHONG_VALUES = [63, 69, 73, 75, 75, 73, 69, 63]
    DA_BIAN_VALUES = XIAO_BIAN_VALUES[:]
    DA_BIAN_VALUES.reverse()
    ALL_VALUES = XIAO_BIAN_VALUES + ZHONG_VALUES + DA_BIAN_VALUES

    BIAN_START_COUNT = 2
    BIAN_END_COUNT = 3

    LIAN_START_COUNT = 3
    LIAN_END_COUNT = 6

    VALUE_RATE = 1 * 10 * 10

    def __init__(self, game):
        self.count = 0
        self.game = game
        self.is_running = True
        self.last_id = 0
        pass

    def get_value_by_rate(self, i):
        return i * RuleBase.VALUE_RATE

    @staticmethod
    def get_color_red(str):
        if str is not None:
            return colored(str, "red")
        return str

    @staticmethod
    def get_color_green(str):
        if str is not None:
            return colored(str, "green")
        return str

    def get_start_index(self):
        return RuleBase.LIAN_START_COUNT

    def get_end_index(self):
        return RuleBase.LIAN_END_COUNT

    def get_rule_name(self):
        pass

    def get_data(self):
        pass

    def check_count(self):
        pass

    def start(self):
        # if not self.is_running:
        #     return
        latest_round = self.game.latestRound
        running_round = self.game.runningRound
        http = self.game.get_http()
        if latest_round is None or running_round is None:
            return False

        self.check_count()

        if self.get_start_index() <= self.count < self.get_end_index():
            game_name = self.game.get_game_name()
            index_url = "http://www.juxiangyou.com/fun/play/{0}/index".format(game_name)
            get_url = "http://www.juxiangyou.com/fun/play/{0}/jctz?id={1}".format(game_name, running_round.id)
            header = self.game.get_header()
            header["Referer"] = index_url
            r = http.get(get_url, header)
            if r is not None:
                # html = r.text
                # Logger.info(html)
                r.close()

            data, bean_count = self.get_data()
            header["Referer"] = get_url
            post_url = "http://www.juxiangyou.com/fun/play/interaction"
            r = http.post(post_url, data, header)
            if r is not None:
                html = r.text
                Logger.info(
                    "- - - >> 游戏{0}，{1} 连 {2} 期,投注期号:{3},豆子：{4},投注结果:{5},{6}".format(
                        RuleBase.get_color_red(game_name), RuleBase.get_color_red(self.get_rule_name()),
                        RuleBase.get_color_green(self.count),
                        RuleBase.get_color_red(running_round.id),
                        RuleBase.get_color_red(bean_count), html,
                        datetime.datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S")))
                return True
                if "账户余额不足" in html:
                    self.is_running = False
                    Logger.error("- - - >> 当前账户余额不足,结束自动投注")
                r.close()
            else:
                Logger.error(
                    "- - - >>  游戏{0}，{1} 连 {2} 期, 投注期号:{3},投注结果:{4},{5}".format(
                        RuleBase.get_color_red(game_name), RuleBase.get_color_red(self.get_rule_name()),
                        RuleBase.get_color_green(self.count),
                        RuleBase.get_color_red(running_round.id),
                        RuleBase.get_color_red("投入失败"),
                        datetime.datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S")))
                return False
