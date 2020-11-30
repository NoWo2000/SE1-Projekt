from .Alarm import Alarm
from ..utils import Endpoints, ApiRequest
from ..database import dbm, RadarSchema, RADAR

class RadarTower():
    def __init__(self):
        self.api = ApiRequest()
        self.db = dbm

    def run(self):
        data = self.fetch()
        radar_obj_list = self.prepareAndSave(data)
        for radar_obj in radar_obj_list:
            self.evaluate(radar_obj)

    def prepareAndSave(self, data):
        radar_obj_list = []
        for radarData in data:
            radar_obj = RadarSchema(**radarData)
            radar_obj_list += [radar_obj, ]
            self.db.write(RADAR, radar_obj)
        return radar_obj_list

    def fetch(self):
        data = self.api.get(Endpoints.RADAR)
        return data

    def evaluate(self, radarDataset):
        if len(radarDataset.callsign) < 4 or len(radarDataset.callsign) > 7:
            Alarm(75, ['Callsign'])
        if radarDataset.alt < 0:
            Alarm(75, ['Altidude'])
        if radarDataset.lat < -180 or radarDataset.lat > 180:
            Alarm(75, ['Latidude'])
        if radarDataset.lon < -90 or radarDataset.lon > 90:
            Alarm(75, ['Longitude'])

if __name__ == '__main__':
    radarData = [
        {
            "callsign": "EWG036",
            "date": 1606315528655,
            "lat": 10.240887,
            "lon": 53.743989,
            "alt": 2500
        },
        {
            "callsign": "EWG034",
            "date": 1606315528655,
            "lat": 10.240887,
            "lon": 53.743989,
            "alt": 26
        },
        {
            "callsign": "EWG346",
            "date": 1123415528655,
            "lat": 12.20887,
            "lon": 70.743989,
            "alt": 2501
        },
    ]
    rf = RadarFetch()
    rf.prepareAndSave(radarData)
