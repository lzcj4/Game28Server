echo "--- stop GameDaemon"
pkill -f "/data/nick/Game28/bin/python3 GameDaemon.py"

echo "++++ start new GameDaemon"
/data/nick/Game28/bin/python3 GameDaemon.py
