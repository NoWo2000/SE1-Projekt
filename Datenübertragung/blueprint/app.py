import atexit
from apscheduler.schedulers.background import BackgroundScheduler

import blueprint.resources.utils.api as Api
from blueprint.watchtower import WatchTower
from blueprint.resources.utils import loggerFile, config
from blueprint.resources.server.main import app, socketio

class Blueprint:

    @staticmethod
    def run():
        loggerFile.log("*"*10 + " Start Application " + "*"*10)
        
        loggerFile.log("Setup BackgroundScheduler...")
        scheduler = BackgroundScheduler()
        tower = WatchTower()
        scheduler.add_job(func=tower.watch, trigger="interval", seconds=int(config['WATCHTOWER']['interval']))
        scheduler.start()
        loggerFile.log("BackgroundScheduler has been started")

        # Shutdown scheduler if the web process is stopped
        atexit.register(lambda: scheduler.shutdown(wait=True))

        loggerFile.log("Start http server")
        socketio.run(app, port=config['WEBSERVER']['port'])


