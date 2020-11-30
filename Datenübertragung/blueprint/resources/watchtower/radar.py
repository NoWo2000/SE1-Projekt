from ..utils import Endpoints, ApiRequest
from ..database import dbm, RadarSchema, RADAR


class RadarFetch():
    def __init__(self):
        self.api = ApiRequest()
        self.db = dbm

    def prepareAndSave(self, data):
        radar_obj_list = []
        for radarData in data:
            radar_obj = RadarSchema(**radarData)
            radar_obj_list += [radar_obj, ]
            self.db.write(RADAR, radar_obj)

    def fetch(self):
        data = self.api.get(Endpoints.RADAR)
        self.prepareAndSave(data)

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
