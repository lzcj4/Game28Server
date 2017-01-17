from GameBase import GameBase


class Speed16(GameBase):
    GAME_INDEX = GameBase.HOST + "fun/play/speed16/index"
    TABLE = "tb_speed16"
    GAME_NAME = "speed16"

    def get_game_url(self):
        return self.GAME_INDEX

    def get_table_name(self):
        return self.TABLE

    def get_game_name(self):
        return self.GAME_NAME
