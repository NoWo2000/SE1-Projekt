from .setup import db
from .schema.it import ItSchema, it
from .schema.event import EventSchema, event
from .schema.flightplans import FlightplansSchema, flightplans
from .schema.radar import RadarSchema, radar
from .schema.terminal import TerminalSchema, terminal
from .schema.test import TestSchema


class DatabaseManager():

    def __init__(self):
        db.create_all()

    def write(self, documentType, data):
        if documentType == it:
            return self._write_it(data)
        if documentType == event:
            return self._write_event(data)

    def _write_it(self, data):
        itdict = {}
        for elem in data:
            key = elem['name'].replace('-', '_')
            itdict[key] = elem['value']
        it_obj = ItSchema(**itdict)
        db.session.add(it_obj)
        db.session.commit()
        return it_obj

    def _write_event(self, event):
        event_obj = EventSchema(**event)
        db.session.add(event_obj)
        db.session.commit()

# debug DatabaseManager-class
if __name__ == '__main__':
    dbm = DatabaseManager()
    dbm.write("event", {
        "affectedSystems": ["it"],
        "suspectedAttackType": "Bruteforce",
        "probability": 55,
        "automaticReaction": [],
        "checklist": ["High CPU Usage", "SSH login failed"]
    })
    print(EventSchema.query.filter_by(id=1).first())
    
    # print('*'*10 + ' Debug: DatabaseManager ' + '*'*10 )

    # print(len(TestSchema.query.all()))
    # doc = TestSchema(news='Test')
    # doc.save()
    # print(TestSchema.query.all())
    # doc.remove()
    # print(TestSchema.query.all())
