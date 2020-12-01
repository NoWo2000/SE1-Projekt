import json
from datetime import datetime
from random import randint
from ..server import send_alert
from ..database.main import dbm, EVENT


class Alarm():

    def __init__(self, probability, affectedSystems):
        event = {
        "time": int(datetime.now().timestamp()), #String
        "affectedSystems": affectedSystems, #Array von Strings
        "suspectedAttackType": self.attacksType(), #String
        "probability": probability, #Zahl (10-100) (Zusendung von jedem Event ab 10% Probability)
        "automaticReaction": self.automaticReaction(), #Array von Strings
        "checklist": self.checkList() #Array von Strings
        }
        db_event = dbm.write(EVENT, event)
        event["id"] = db_event.id
        send_alert(event)

    def checkList(self):
        todos = ["Contact Manager", "Reboot System", "Drink Coffee", 
                 "Reboot Firewall", "Clear Cache", "Update System", 
                 "Notify Passangers", "Alt+F4", "Check Processes",
                 "Check IT-Desk", "Check Flightplan", "Check Radar"
                ]
    
        checklist = []
        listlength = randint(1, 3)
    
        while True:
            random = randint(0, len(todos) - 1)
            if todos[random] not in checklist:
                checklist.append(todos[random])
            if len(checklist) == listlength:
                return checklist
    
    def attacksType(self):
        attacks = ["Brute Force", "Privilege Escalations", "SQL-Injection", "DDoS"]
        return attacks[randint(0, len(attacks) - 1)]
    
    def automaticReaction(self):
        reactions = ["Shut Down", "Do Nothing", "Ring Alarm", "Call Police", "Call 112", "Sit back and relax", "Inform your Supervisor"]
        automaticReactions = []
        listlength = randint(2, 5)
        while True:
            random = randint(0, len(reactions) - 1)
            if reactions[random] not in automaticReactions:
                automaticReactions.append(reactions[random])
            if len(automaticReactions) == listlength:
                return automaticReactions