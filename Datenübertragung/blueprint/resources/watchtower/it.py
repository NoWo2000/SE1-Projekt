import .Severity
from ..utils import Endpoints, ApiRequest
from ..database import dbm, ItSchema, IT

class ItTower():
    def __init__(self):
        self.api = ApiRequest()
        self.db = dbm

    def run(self):
        

    def prepareAndSave(self, data):
        itdict = {}
        for elem in data:
            key = elem['name'].replace('-', '_')
            itdict[key] = elem['value']
        it_obj = ItSchema(**itdict)
        self.db.write(IT, it_obj)

    def fetch(self):
        data = self.api.get(Endpoints.IT)
        self.prepareAndSave(data)
        # TODO: self.db.get(IT, limit=10)

    def evaluateAverage(checkList):
        average = {
            "cpuUsage": 0,
            "ramUsage": 0,
            "serverLoginFailed": 0,
            "serverLoginSuccess": 0,
            "trafficUpload": 0,
            "trafficDownload": 0
        }
        
        for dataset in checkList:
            for var in dir(dataset):
                average[var] += eval("dataset."+var)
        for key in average:
            average[key] /= len(checkList)

        return average

    def calculate(avgDict):
        avgDict = {
           "cpuUsage": _calc_cpu(avgDict["cpuUsage"]),
           "ramUsage": _calc_ram(avgDict["ramUsage"]),
           "serverLoginFailed": _calc_login_failed(avgDict["serverLoginFailed"]),
           "serverLoginSuccess": _calc_login_success(avgDict["serverLoginSuccess"]),
           "trafficUpload": _calc_traffic_up(avgDict["trafficUpload"]),
           "trafficDownload": _calc_traffic_down(avgDict["trafficDownload"])
        }
        severity = 0
        for key in avgDict:
           severity += avgDict[key]

        if severity >= 100:
           severity = 99
        
        checkAlarm(severity, avgDict)
        return severity