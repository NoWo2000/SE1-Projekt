from datetime import datetime
from flask import render_template, request, jsonify
from .setup import app, socketio
from ..database import dbm
from ..utils import loggerFile

def send_alert(data):
    """
    entrypoint to notify frontend about alerts
    """
    socketio.emit('alert', data)
    loggerFile.debug('Sent alert to socket')

@app.route('/', methods=['GET'])
def index():
    """
    Serve static frontend
    """
    return render_template('./index.html')

@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    """
    Get all alerts or filter by date using url parameters
    """
    start = request.args.get('start') or 0
    end = request.args.get('end') or datetime.now().timestamp()
    events = dbm.get_events_by_date(start, end)
    res = []
    for ev in events:
        res.append(ev.as_dict())
    return jsonify(res), 200
