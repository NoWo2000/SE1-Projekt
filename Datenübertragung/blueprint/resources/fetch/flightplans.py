from ..utils import Endpoints, ApiRequest
from ..database import dbm, FlightplansSchema, FLIGHTPLANS


class FlightplansFetch():
    def __init__(self):
        self.api = ApiRequest()
        self.db = dbm

    def prepareAndSave(self, data):
        flightplans_obj_list = []
        for flightplansData in data:
            flightplans_obj = FlightplansSchema(**flightplansData)
            flightplans_obj_list += [flightplans_obj, ]
            self.db.write(FLIGHTPLANS, flightplans_obj)

    def fetch(self):
        data = self.api.get(Endpoints.FLIGHTPLANS)
        self.prepareAndSave(data)


if __name__ == '__main__':
    flightplansData = [
        {
            "callsign": "EWG8XZ",
            "ssr": "A1411",
            "rules": "IS",
            "aircraft": "A320",
            "wvc": "M",
            "equipment": "S/S",
            "origin": "LFPG",
            "eobt": 1606262400000,
            "route": "N0431F370 DH632",
            "destination": "EDDH",
            "eet": 7200000,
            "eta": 1606269600000,
            "status": "closed",
            "registration": "DAAA",
            "icao4444": """FPL-EWG8XZ/A1411-IS
                        A320/M-S/S-LFPG0000-N0431F370 DH632-
                        EDDH0200-REG/DAAAA"""
        },
        {
            "callsign": "EWG7753",
            "ssr": "A1505",
            "rules": "IS",
            "aircraft": "A320",
            "wvc": "M",
            "equipment": "S/S",
            "origin": "LOWW",
            "eobt": 1606266000000,
            "route": "N0431F370 DH612",
            "destination": "EDDH",
            "eet": 7200000,
            "eta": 1606273200000,
            "status": "closed",
            "registration": "DAAA",
            "icao4444": """FPL-EWG7753/A1505-IS-
                        A320/M-S/S-LOWW0100-N0431F370 DH612-
                        EDDH0200-REG/DAAAB"""
        }
    ]
    rf = FlightplansFetch()
    rf.prepareAndSave(flightplansData)
