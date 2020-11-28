from datetime import datetime
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

    def _write_it(self, it_obj):
        db.session.add(it_obj)
        db.session.commit()
        return it_obj

    def _write_event(self, event):
        event_obj = EventSchema(**event)
        db.session.add(event_obj)
        db.session.commit()
        return event_obj

    def get_events_by_date(self, lower_time, upper_time):
        return EventSchema.query.filter(
            EventSchema.time <= upper_time,
            EventSchema.time >= lower_time
            ).all()
# debug DatabaseManager-class
if __name__ == '__main__':
    dbm = DatabaseManager()
    ev = dbm.write("event", {
        "affectedSystems": ["it"],
        "suspectedAttackType": "Bruteforce",
        "probability": 55,
        "automaticReaction": [],
        "checklist": ["High CPU Usage", "SSH login failed"]
    })
    datetime_str = '2020-11-28 15:57:51'
    dt = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    ts = dt.timestamp()
    datetime_str = '2020-11-27 13:27:51'
    dt = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    tl = dt.timestamp()
    a = dbm.get_event_by_date(tl, ts)
    print(a)
    # print(EventSchema.query.filter(id=1).first())
    
    # print('*'*10 + ' Debug: DatabaseManager ' + '*'*10 )

    # print(len(TestSchema.query.all()))
    # doc = TestSchema(news='Test')
    # doc.save()
    # print(TestSchema.query.all())
    # doc.remove()
    # print(TestSchema.query.all())
