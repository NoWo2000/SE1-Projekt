import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from flask import Flask, render_template, request
from flask_socketio import SocketIO
from ..database import DatabaseManager
from ..utils import loggerFile

app = Flask(__name__, static_url_path='', static_folder='static')
socketio = SocketIO(app)

dbm = DatabaseManager()

scheduler = BackgroundScheduler()
scheduler.add_job(func=fetch_api, trigger="interval", seconds=30)
scheduler.start()

# Shutdown scheduler if the web process is stopped
atexit.register(lambda: scheduler.shutdown(wait=True))

def fetch_api():
    """
    main app entrypoint?
    """
    print('fetch...')

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
    res = dbm.get_events_by_date(start, end)
    return res, 200

socketio.run(app)
