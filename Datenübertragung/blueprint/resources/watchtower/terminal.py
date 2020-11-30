from ..utils import Endpoints, ApiRequest
from ..database import dbm, TerminalSchema, TERMINAL


class TerminalFetch():
    def __init__(self):
        self.api = ApiRequest()
        self.db = dbm

    def prepareAndSave(self, data):
        terminal_obj_list = []
        for terminalData in data:
            terminal_obj = TerminalSchema(**terminalData)
            terminal_obj_list += [terminal_obj, ]
            self.db.write(TERMINAL, terminal_obj)

    def fetch(self):
        data = self.api.get(Endpoints.TERMINAL)
        self.prepareAndSave(data)


if __name__ == '__main__':
    terminalData = [
        {
            "level": "warning",
            "message": "Mr.Schmidt please go to your flight."
        },
        {
            "level": "warning",
            "message": "Mr.Fruck please help me."
        },
        {
            "level": "warning",
            "message": "Mr.Losem please go to your flight."
        }
    ]
    rf = TerminalFetch()
    rf.prepareAndSave(terminalData)
