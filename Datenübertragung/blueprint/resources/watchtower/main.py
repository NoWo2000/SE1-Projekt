from .flightplans import FlightplansTower
from .it import ItTower
from .radar import RadarTower
from .terminal import TerminalTower
from ..utils import loggerFile

class WatchTower():

    def __init__(self):
        self.flightplansFetch = FlightplansTower()
        self.itFetch = ItTower()
        self.radarFetch = RadarTower()
        self.terminalFetch = TerminalTower()

        loggerFile.log("WatchTower has been initalized!")

    def watch(self):
        loggerFile.log("Run WatchTower.watch ...")
        self.flightplansFetch.run()
        self.itFetch.run()
        self.radarFetch.run()
        self.terminalFetch.run()

        loggerFile.log("... finished WatchTower.watch!")


        