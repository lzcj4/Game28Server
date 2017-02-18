from Crazy28 import Crazy28
from PC28 import PC28
from Korea28 import Korea28
from Speed16 import Speed16
from enum import Enum


class GameType(Enum):
    PC28 = 0x01
    Crazy28 = 0x02
    Korea28 = 0x04
    Speed16 = 0x08


class GameFactory:
    @staticmethod
    def get_game(game_type):
        result = None
        if game_type == GameType.PC28:
            result = PC28(True)
        elif game_type == GameType.Crazy28:
            result = Crazy28(True)
        elif game_type == GameType.Korea28:
            result = Korea28(True)
        elif game_type == GameType.Speed16:
            result = Speed16()

        return result
