from GameBase import GameBase


class Crazy28(GameBase):
    GAME_INDEX = GameBase.HOST + "fun/play/crazy28/index"
    TABLE = "tb_crazy28"
    GAME_NAME = "crazy28"

    def get_game_url(self):
        return self.GAME_INDEX

    def get_table_name(self):
        return self.TABLE

    def get_game_name(self):
        return self.GAME_NAME
