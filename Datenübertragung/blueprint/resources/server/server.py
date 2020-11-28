import atexit
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from ..utils import loggerFile

app = Flask(__name__)
socketio = SocketIO(app)

def fetch_api():
    print('fetch...')

scheduler = BackgroundScheduler()
scheduler.add_job(func=fetch_api, trigger="interval", seconds=30)
scheduler.start()

# Shutdown scheduler if the web process is stopped
atexit.register(lambda: scheduler.shutdown(wait=True))

def send_alert(data):
    """
    entrypoint to notify frontend about alters
    """
    socketio.emit('alert', data)
    loggerFile.debug('Sent alert to socket')

@app.route('/alerts', methods=['GET'])
def get_alerts():
    start = request.args.get('start') or int(datetime.now().timestamp())
    end = request.args.get('end')
    print(start)
    return jsonify([start, end]), 200

@app.route('/', methods=['GET'])
def index():
    """
    Plain html site that logs socket events to browser console
    ToDo: Remove before production
    """
    return render_template('./index.html')

@app.route('/test', methods=['GET'])
def send_example_alert():
    """
    send example dataset to websocket
    ToDo: Remove before production
    """
    send_alert({
        "id": 42,
        "time": "15:15:15",
        "date": "26-11-2020",
        "affectedSystems": ["it"],
        "suspectedAttackType": "Bruteforce",
        "probability": 55,
        "automaticReaction": [],
        "checklist": ["High CPU Usage", "SSH login failed"]
    })
    return 'data sent', 200

socketio.run(app)
