import Logger


class RuleBase:
    XIAO_BIAN_VALUES = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    ZHONG_VALUES = [63, 69, 73, 75, 75, 73, 69, 63]
    DA_BIAN_VALUES = XIAO_BIAN_VALUES[:]
    DA_BIAN_VALUES.reverse()
    ALL_VALUES = XIAO_BIAN_VALUES + ZHONG_VALUES + DA_BIAN_VALUES

    VALUE_RATE = 10 * 10

    def __init__(self, game):
        self.count = 0
        self.game = game
        self.is_running = True
        pass

    def get_value_by_rate(self, i):
        return i * RuleBase.VALUE_RATE

    def get_start_index(self):
        return 4

    def get_end_index(self):
        return 6

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
            return

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

            data = self.get_data()
            header["Referer"] = get_url
            post_url = "http://www.juxiangyou.com/fun/play/interaction"
            r = http.post(post_url, data, header)
            if r is not None:
                html = r.text
                Logger.info(
                    "----》》 游戏{0}，{1} 连 {2} 期,投注期号:{3},投注结果:{4}".format(game_name, self.get_rule_name(), self.count,
                                                                     running_round.id, html))
                if "账户余额不足" in html:
                    self.is_running = False
                    Logger.error("----》》 当前账户余额不足,结束自动投注")
                r.close()
            else:
                Logger.error(
                    "----》》 游戏{0}，{1} 连 {2} 期, 投注期号:{3},投注结果:{4}".format(game_name, self.get_rule_name(), self.count,
                                                                     running_round.id, "投入失败"))
