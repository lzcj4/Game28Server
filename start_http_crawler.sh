echo "--- stop GameDaemon"
pkill -f "/data/nick/Game28/bin/python3 AppMain.py"

echo "++++ start new GameDaemon"
/data/nick/Game28/bin/python3 AppMain.py &
