from Rule.RuleBase import RuleBase
import Logger
from termcolor import colored


class BianRule(RuleBase):
    """边投注"""

    def __init__(self, game):
        RuleBase.__init__(self, game)
        pass

    def get_start_index(self):
        return RuleBase.BIAN_START_COUNT

    def get_end_index(self):
        return RuleBase.BIAN_END_COUNT

    def get_rule_name(self):
        return "边投注"

    def check_count(self):
        current_round = self.game.latestRound
        if current_round is None or \
                        self.last_id == current_round.id:
            return
        self.last_id = current_round.id

        if 0 <= current_round.value <= 9 or \
                                18 <= current_round.value <= 27:
            self.count += 1
            Logger.info("游戏: {0}，期号:{1} 值:{2}，边计数++：{3}".format(
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
        for i in RuleBase.XIAO_BIAN_VALUES:
            new_value = self.get_value_by_rate(i)
            bean_count += new_value
            content += "%22{0}%22%2C".format(new_value)
        for i in RuleBase.ZHONG_VALUES:
            content += "%22{0}%22%2C".format(0)
        for i in RuleBase.DA_BIAN_VALUES:
            new_value = self.get_value_by_rate(i)
            bean_count += new_value
            content += "%22{0}%22%2C".format(new_value)
        content = content[0:-3] + "%5D%7D"
        return content, bean_count
