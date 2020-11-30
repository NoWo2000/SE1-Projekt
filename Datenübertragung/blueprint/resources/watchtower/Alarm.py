import json
from datetime import datetime
from random import randint

def checkAlarm(p, pDict):
    if p >= 10:
        affectedSystems = [x for x in pDict if pDict[x] >= 10]
        alarm(p, affectedSystems)

def checkList():
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

def attacksType():
    attacks = ["Brute Force", "Privilege Escalations", "SQL-Injection", "DDoS"]
    return attacks[randint(0, len(attacks) - 1)]

def automaticReaction():
    reactions = ["Shut Down", "Do Nothing", "Ring Alarm", "Call Police"]
    return reactions[randint(0, len(reactions) - 1)]

def alarm(probability, affectedSystems):
    event = {
        "time": datetime.now().timestamp(), #String
        "affectedSystems": affectedSystems, #Array von Strings
        "suspectedAttackType": attacksType(), #String
        "probability": probability, #Zahl (10-100) (Zusendung von jedem Event ab 10% Probability)
        "automaticReaction": automaticReaction(), #Array von Strings
        "checklist": checkList() #Array von Strings
    }
    print(event)