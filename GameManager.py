import threading
import time

from GameFactory import GameFactory, GameType
from GameBase import GameBase

is_running = True
sleep_seconds = 1 * 10


def start_game(game_type):
    game = GameFactory.get_game(game_type)
    while is_running:
        if game.get_rounds():
            '''刚开奖会要等会'''
            # time.sleep(5)
            game.post_next_round()
        time.sleep(sleep_seconds)


def start_all_game():
    while not GameBase.login_action():
        time.sleep(5)
    is_running = True
    threading.Thread(target=lambda: start_game(GameType.Crazy28)).start()
    threading.Thread(target=lambda: start_game(GameType.Korea28)).start()
    threading.Thread(target=lambda: start_game(GameType.PC28)).start()
    threading.Thread(target=lambda: start_game(GameType.Speed16)).start()


def stop_game():
    is_running = False
