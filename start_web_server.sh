echo "----- stop GameWebServer process"
pkill -f "/data/nick/Game28/bin/python3 GameWebServer.py"

echo "+++++ start new GameWebServer process"
/data/nick/Game28/bin/python3 GameWebServer.py & 
