#from EvaluateAverage import evaluateAverage
#from EvaluateFlightplan import evaluateFlightplan
#from EvaluateRadar import evaluateRadar

def checkDataObject(obj):
    if len(obj) == 7:
        evaluateAverage(obj)
    if len(obj) == 14:
        evaluateFlightplan(obj)
    if len(obj) == 5:
        evaluateRadar(obj)  

class ITDataset:

    #Constructor
    def __init__(self, cpuUsage, ramUsage, serverLoginFailed, serverLoginSuccess, trafficUpload, trafficDownload, news):
        self.cpuUsage = cpuUsage
        self.ramUsage = ramUsage
        self.serverLoginFailed = serverLoginFailed
        self.serverLoginSuccess = serverLoginSuccess
        self.trafficUpload = trafficUpload
        self.trafficDownload = trafficDownload
        self.news = news

    def __dir__(self):
        return ["cpuUsage", "ramUsage", "serverLoginFailed", "serverLoginSuccess", "trafficUpload", "trafficDownload"]

class FlightplanDataset:

    def __init__(self, callsign, ssr, rules, aircraft, wvc, equipment, origin, eobt, 
                route, destination, eet, eta, status, registration, icao4444):
        self.callsign = callsign
        self.ssr = ssr
        self.rules = rules
        self.aircraft = aircraft
        self.wvc = wvc
        self.equipment = equipment
        self.origin = origin
        self.eobt = eobt
        self.route = route
        self.destination = destination
        self.eet = eet
        self.eta = eta
        self.status = status
        self.registration = registration
        self.icao4444 = icao4444

class RadarDataset:

    def __init__(self, callsign, date, lat, lon, alt):
        self.callsign = callsign
        self.date = date
        self.lat = lat
        self.lon = lon
        self.alt = alt