iOS Client Config (Plist Injection)

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>ServerURL</key>
    <string>http://YOUR_IP:5000/api</string>
    <key>EnableCheats</key>
    <true/>
    <key>ResourceMultiplier</key>
    <real>1000.0</real>
    <key>BypassValidation</key>
    <true/>
    <key>SpeedHack</key>
    <real>0.01</real>
</dict>
</plist>


Docker Deployment (One-click setup)


# Dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y nginx supervisor

COPY hayday_server.py /app/
COPY requirements.txt /app/
WORKDIR /app

RUN pip install -r requirements.txt flask flask-socketio eventlet gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--worker-class", "eventlet", "hayday_server:app"]


# Build & Run
docker build -t hayday-pentest .
docker run -d -p 5000:5000 --name hayday-server hayday-pentest

run fast

python3 hayday_server.py


edit apk

python3 hayday_patcher.py HayDay.apk HayDay_Patched.apk
#  YOUR_IP  IP 


🎯  Pentest:
✅ 999M coins/diamonds 
✅ x1000 loot multiplier
✅ 100x speed hack
✅ Instant shipments
✅ Bypass SSL pinning
✅ Real-time loot injection
✅ SocketIO notifications
