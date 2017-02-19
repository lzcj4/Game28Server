#!/usr/bin/env bash
echo "--- stop GameDaemon"
pkill -f "/data/nick/Game28/bin/python3 AppMain.py"

echo "++++ start new GameDaemon"
echo "/data/nick/Game28/bin/python3 AppMain.py &"