from flask import Flask, render_template
from flask_socketio import SocketIO
from ..utils import loggerFile

app = Flask(__name__)

socketio = SocketIO(app)

socketio.run(app)

def send_alert(data):
    """
    entrypoint to notify frontend about alters
    """
    socketio.emit('alert', data)
    loggerFile.debug('Sent alert to socket')

@app.route('/', methods=['GET'])
def index():
    """
    Plain html site that loggs socket events to browser console
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
