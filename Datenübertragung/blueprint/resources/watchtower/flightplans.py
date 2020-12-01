from .Alarm import Alarm
from ..utils import Endpoints, ApiRequest
from ..database import dbm, FlightplansSchema, FLIGHTPLANS


class FlightplansTower():
    def __init__(self):
        self.api = ApiRequest()
        self.db = dbm

    def run(self):
        data = self.fetch()
        flightplans_obj_list = self.prepareAndSave(data)
        for flightplan in flightplans_obj_list:
            self.evaluate(flightplan)

    def prepareAndSave(self, data):
        result = []
        for flightplansData in data:
            fl = FlightplansSchema.query.filter(
                FlightplansSchema.icao4444 == flightplansData["icao4444"]
            ).first()

            if fl is not None and fl.as_dict() != flightplansData:
                flightplans_obj = FlightplansSchema(**flightplansData)
                result.append(flightplans_obj)
                self.db.update(FLIGHTPLANS, fl, flightplans_obj)
            else:
                flightplans_obj = FlightplansSchema(**flightplansData)
                result.append(flightplans_obj)
                self.db.write(FLIGHTPLANS, flightplans_obj)

        return result

    def fetch(self):
        data = self.api.get(Endpoints.FLIGHTPLANS)
        return data

    def evaluate(self, flightplanData):
        time = flightplanData.eta - flightplanData.eet
        if flightplanData.eobt != time:
            Alarm(75, ["eta", "eet", "eobt"])
        if flightplanData.status not in ['closed', 'scheduled', 'departed', 'initiated', 'in_block', 'off-block']:
            Alarm(75, ['Status'])
        if len(flightplanData.registration) != 4:
            alarm(75, ['Registration'])
        if len(flightplanData.destination) != 4:
            Alarm(75, ['Destination'])
        if len(flightplanData.origin) != 4:
            Alarm(75, ['Origin'])
        if len(flightplanData.callsign) < 4 or len(flightplanData.callsign) > 7:
            Alarm(75, ['Callsign']) 



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
    rf = FlightplansTower()
    rf.prepareAndSave(flightplansData)
