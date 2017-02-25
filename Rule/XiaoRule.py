from Rule.RuleBase import RuleBase
import Logger


class XiaoRule(RuleBase):
    """小投注"""

    def __init__(self, game):
        RuleBase.__init__(self, game)
        pass

    def get_rule_name(self):
        return "小投注"

    def check_count(self):
        current_round = self.game.latestRound
        if current_round is None or \
                        self.last_id == current_round.id:
            return
        self.last_id = current_round.id

        if current_round.value < 14:
            self.count += 1
            Logger.info("游戏: {0}，期号:{1} 值:{2}，小计数++：{3}".format(
                RuleBase.get_color_red(self.game.get_game_name()), RuleBase.get_color_red(current_round.id),
                RuleBase.get_color_red(current_round.value), RuleBase.get_color_green(self.count)))
        else:
            self.count = 0

    def get_data(self):
        next_round = self.game.runningRound
        game_name = self.game.get_game_name()
        content = ("jxy_parameter=%7B%22fun%22%3A%22lottery%22%2C%22c%22%3A%22quiz%22%2C%22items%22%3A%22{0}" + \
                   "%22%2C%22lssue%22%3A%22{1}" + "%22%2C%22lotteryData%22%3A%5B").format(game_name, next_round.id)
        bean_count = 0
        for i in range(len(RuleBase.ALL_VALUES)):
            if i < 14:
                new_value = self.get_value_by_rate(RuleBase.ALL_VALUES[i])
                bean_count += new_value
                content += "%22{0}%22%2C".format(new_value)
            else:
                content += "%22{0}%22%2C".format(0)
        content = content[0:-3] + "%5D%7D"
        return content, bean_count
