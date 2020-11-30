from datetime import datetime
from .schema import EVENT, EventSchema
from .setup import db


class DatabaseManager():

    def __init__(self):
        db.create_all()

    def write(self, documentType, obj):
        if documentType == EVENT:
            obj = EventSchema(**obj)
        db.session.add(obj)
        db.session.commit()
        return obj

    def update(self, documentType, obj, new_obj):
        db.session.delete(obj)
        db.session.commit()
        self.write(documentType, new_obj)

    def get_events_by_date(self, lower_time, upper_time):
        return EventSchema.query.filter(
            EventSchema.time <= upper_time,
            EventSchema.time >= lower_time
            ).all()

dbm = DatabaseManager()

# debug DatabaseManager-class
if __name__ == '__main__':
    dbm.write("event", {
        "affectedSystems": ["it"],
        "suspectedAttackType": "Bruteforce",
        "probability": 55,
        "automaticReaction": [],
        "checklist": ["High CPU Usage", "SSH login failed"]
    })
    datetime_str = '2020-11-28 18:57:51'
    dt = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    ts = dt.timestamp()
    datetime_str = '2020-11-27 13:27:51'
    dt = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    tl = dt.timestamp()
    a = dbm.get_events_by_date(tl, ts)
    print(a)
    # print(EventSchema.query.filter(id=1).first())

    # print('*'*10 + ' Debug: DatabaseManager ' + '*'*10 )

    # print(len(TestSchema.query.all()))
    # doc = TestSchema(news='Test')
    # doc.save()
    # print(TestSchema.query.all())
    # doc.remove()
    # print(TestSchema.query.all())
