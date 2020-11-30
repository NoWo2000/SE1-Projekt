from .resources.fetch import FlightplansFetch, ItFetch, RadarFetch, TerminalFetch
from .resources.utils import loggerFile

class WatchTower():

    def __init__(self):
        self.flightplansFetch = FlightplansFetch()
        self.itFetch = ItFetch()
        self.radarFetch = RadarFetch()
        self.terminalFetch = TerminalFetch()

        loggerFile.log("WatchTower has been initalized!")

    def watch(self):
        loggerFile.log("Run WatchTower.watch ...")
        self.flightplansFetch.fetch()
        self.itFetch.fetch()
        self.radarFetch.fetch()
        self.terminalFetch.fetch()


        