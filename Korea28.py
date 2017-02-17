from GameBase import GameBase


class Korea28(GameBase):
    GAME_INDEX = GameBase.HOST + "fun/play/korea28/index"
    TABLE = "tb_korea28"
    GAME_NAME = "korea28"

    def __init__(self, is_auto_fire=False):
        GameBase.__init__(self, is_auto_fire)

    def get_game_url(self):
        return self.GAME_INDEX

    def get_table_name(self):
        return self.TABLE

    def get_game_name(self):
        return self.GAME_NAME
