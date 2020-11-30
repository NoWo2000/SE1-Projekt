# pip install scipy
from scipy.interpolate import interp1d
from math import ceil
from Alarm import checkAlarm

SEV = {
    "CPU":0.6,
    "RAM":0.6,
    "LoginS":0.1,
    "LoginF":0.7,
    "TrafficUp":0.2,
    "TrafficDown":0.3
}

def calculateSeverity(avgDict):
    avgDict = {
        "cpuUsage": calcCPU(avgDict["cpuUsage"]),
        "ramUsage": calcRAM(avgDict["ramUsage"]),
        "serverLoginFailed": calcLoginFailed(avgDict["serverLoginFailed"]),
        "serverLoginSuccess": calcLoginSuccess(avgDict["serverLoginSuccess"]),
        "trafficUpload": calcTrafficUp(avgDict["trafficUpload"]),
        "trafficDownload": calcTrafficDown(avgDict["trafficDownload"])
    }
    severity = 0
    for key in avgDict:
        severity += avgDict[key]

    if severity >= 100:
        severity = 99

    checkAlarm(severity, avgDict)
    return severity

def calcCPU(value):
    x = [0, 60, 75, 90, 99]
    y = [0, 10, 30, 75, 99]
    return ceil(SEV["CPU"] * interp1d(x, y)(value))

def calcRAM(value):
    x = [0, 40, 60, 80, 99]
    y = [0, 10, 30, 75, 99]
    return ceil(SEV["RAM"] * interp1d(x, y)(value))

def calcLoginSuccess(value):
    x = [0, 1200, 1300, 1500, 100000]
    y = [0, 10, 20, 30, 40]
    return ceil(SEV["LoginS"] * interp1d(x, y)(value))

def calcLoginFailed(value):
    x = [0, 200, 250, 300, 500, 10000000]
    y = [0, 10, 30, 60, 90, 99]
    return ceil(SEV["LoginF"] * interp1d(x, y)(value))

def calcTrafficUp(value):
    x = [0, 75]
    y = [0, 30]
    return ceil(SEV["TrafficUp"] * interp1d(x, y)(value))

def calcTrafficDown(value):
    x = [0, 100]
    y = [0, 50]
    return ceil(SEV["TrafficDown"] * interp1d(x, y)(value))