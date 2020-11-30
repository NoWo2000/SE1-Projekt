from .Severity import *
from .Alarm import Alarm
from ..utils import Endpoints, ApiRequest
from ..database import dbm, ItSchema, IT

class ItTower():
    def __init__(self):
        self.api = ApiRequest()
        self.db = dbm

    def run(self):
        data = self.fetch()
        self.prepareAndSave(data)
        avgDict = self.evaluateAverage()
        self.calculate(avgDict)

    def prepareAndSave(self, data):
        itdict = {}
        for elem in data:
            key = elem['name'].replace('-', '_')
            itdict[key] = elem['value']
        it_obj = ItSchema(**itdict)
        self.db.write(IT, it_obj)

    def fetch(self):
        data = self.api.get(Endpoints.IT)
        return data

    def evaluateAverage(self):
        """
        evalutes the average of the last 10 datasets
        returns dictionary
        """

        checkList = self.db.get_last_it(10)
        average = {
            "cpuUsage": 0,
            "ramUsage": 0,
            "serverLoginFailed": 0,
            "serverLoginSuccess": 0,
            "trafficUpload": 0,
            "trafficDownload": 0
        }
        
        for dataset in checkList:
            average["cpuUsage"] += dataset.server_cpu_usage
            average["ramUsage"] += dataset.server_ram_usage
            average["serverLoginFailed"] += dataset.server_login_failed
            average["serverLoginSuccess"] += dataset.server_login_success
            average["trafficUpload"] += dataset.traffic_upload
            average["trafficDownload"] += dataset.traffic_download
        for key in average:
            average[key] /= len(checkList)

        return average

    def calculate(self, avgDict):
        avgDict = {
           "cpuUsage": calc_cpu(avgDict["cpuUsage"]),
           "ramUsage": calc_ram(avgDict["ramUsage"]),
           "serverLoginFailed": calc_login_failed(avgDict["serverLoginFailed"]),
           "serverLoginSuccess": calc_login_success(avgDict["serverLoginSuccess"]),
           "trafficUpload": calc_traffic_up(avgDict["trafficUpload"]),
           "trafficDownload": calc_traffic_down(avgDict["trafficDownload"])
        }
        severity = 0
        for key in avgDict:
           severity += avgDict[key]

        if severity >= 100:
           severity = 99

        if severity >= 10:
            affectedSystems = [x for x in avgDict if avgDict[x] >= 10]
            Alarm(severity, affectedSystems)

if __name__ == "__main__":
    tower = ItTower()
    tower.run()