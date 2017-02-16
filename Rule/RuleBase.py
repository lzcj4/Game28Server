import Logger


class RuleBase:
    XIAO_BIAN_VALUES = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    ZHONG_VALUES = [63, 69, 73, 75, 75, 73, 69, 63]
    DA_BIAN_VALUES = XIAO_BIAN_VALUES[:]
    DA_BIAN_VALUES.reverse()
    ALL_VALUES = XIAO_BIAN_VALUES + ZHONG_VALUES + DA_BIAN_VALUES

    def __init__(self, game):
        self.count = 0
        self.start_count = 0
        self.game = game
        pass

    def get_rule_name(self):
        pass

    def get_data(self):
        pass

    def check_count(self):
        pass

    def start(self):
        current_round = self.game.currentRound
        next_round = self.game.nextStartRound
        http = self.game.get_http()
        if current_round is None or next_round is None:
            return

        self.check_count()

        if self.count >= self.start_count:
            game_name = self.game.get_game_name()
            index_url = "http://www.juxiangyou.com/fun/play/{0}/index".format(game_name)
            get_url = "http://www.juxiangyou.com/fun/play/{0}/jctz?id={1}".format(game_name, next_round.id)
            header = self.game.get_header()
            header["Referer"] = index_url
            r = http.get(get_url, header)
            str = r.text
            r.close()

            Logger.info("++{0},连的期数：{1}".format(self.get_rule_name(), self.count))
            data = self.get_data()
            header["Referer"] = get_url
            post_url = "http://www.juxiangyou.com/fun/play/interaction"
            r = http.post(post_url, data, header)
            str = r.text
            r.close()
