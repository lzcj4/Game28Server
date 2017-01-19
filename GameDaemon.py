import time

import daemon

import GameManager
from GameBase import GameBase

# while not GameBase.login_action():
#     time.sleep(5)

with daemon.DaemonContext():
    GameManager.start_all_game()
