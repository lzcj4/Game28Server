from GameBase import GameBase


class PC28(GameBase):
    GAME_INDEX = GameBase.HOST + "fun/play/pc28/index"
    TABLE = "tb_pc28"
    GAME_NAME = "pc28"

    def __init__(self, is_auto_fire=False):
        GameBase.__init__(self, is_auto_fire)

    def get_game_url(self):
        return self.GAME_INDEX

    def get_table_name(self):
        return self.TABLE

    def get_game_name(self):
        return self.GAME_NAME
