import logging
import sys
import threading
import time

from GameFactory import GameFactory, GameType

is_running = True
sleep_seconds = 1 * 60


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


def load_logging():
    logging.basicConfig(level=logging.INFO, filename="./Logs/logfile.txt", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
    sys.excepthook = handle_exception


def start_game(game_type):
    game = GameFactory.get_game(game_type)
    while is_running:
        game.get_rounds()
        time.sleep(sleep_seconds)


def start_all_game():
    # while not GameBase.login_action():
    #     time.sleep(5)
    load_logging()
    is_running = True
    threading.Thread(target=lambda: start_game(GameType.PC28)).start()
    threading.Thread(target=lambda: start_game(GameType.Crazy28)).start()
    threading.Thread(target=lambda: start_game(GameType.Korea28)).start()
    threading.Thread(target=lambda: start_game(GameType.Speed16)).start()


def stop_game():
    is_running = False
