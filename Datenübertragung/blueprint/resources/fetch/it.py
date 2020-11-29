from ..utils import Endpoints, ApiRequest
from ..database import dbm, ItSchema, IT


class ItFetch():
    def __init__(self):
        self.api = ApiRequest()
        self.db = dbm

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
