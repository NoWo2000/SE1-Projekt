from ..utils import Endpoints, ApiRequest
from ..database import DatabaseManager, ItSchema, it


class ItFetch():
    def __init__(self):
        self.api = ApiRequest()
        self.db = DatabaseManager()

    def prepareAndSave(self, data):
        itdict = {}
        for elem in data:
            key = elem['name'].replace('-', '_')
            itdict[key] = elem['value']
        it_obj = ItSchema(**itdict)
        self.db.write(it, it_obj)

    def fetch(self):
        data = self.api.get(Endpoints.IT)
        self.prepareAndSave(data)
