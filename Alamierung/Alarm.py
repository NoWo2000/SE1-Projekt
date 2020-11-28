import json
from datetime import datetime

ID = 1

def checkAlarm(p, pDict):
    if p >= 10:
        affectedSystems = [x for x in pDict if pDict[x] >= 10]
        alarm(p, affectedSystems)

def alarm(probability, affectedSystems):
    global ID
    event = {
        "id": ID, #Zahl (Auto-Inkrement)
        "time": datetime.now().strftime("%H:%M:%S"), #String
        "date": datetime.now().strftime("%d.%m.%Y"), #String
        "affectedSystems": affectedSystems, #Array von Strings
        "suspectedAttackType": "suspectedAttackType", #String
        "probability": probability, #Zahl (10-100) (Zusendung von jedem Event ab 10% Probability)
        "automaticReaction": "automaticReaction", #Array von Strings
        "checklist": "checklist" #Array von Strings
    }
    ID += 1
    print(event)