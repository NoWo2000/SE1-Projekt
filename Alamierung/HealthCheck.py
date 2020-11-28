from Dataset import ITDataset, FlightplanDataset, RadarDataset
import EvaluateAverage
import EvaluateFlightplan
import EvaluateRadar
from Severity import calculateSeverity

    
checkList = []
CHECKLIST_MAX = 10

def main():
    #get Information from db, to fill checkList
    data1 = ITDataset(90, 90, 100, 1000, 45, 50, 1)
    listAppend(data1)
    data2 = ITDataset(90, 90, 100, 1000, 45, 50, 1)
    listAppend(data2)
    flightplanData = FlightplanDataset("EWG8XZ", "A1411", "IS", "A320", "M", "S/S", "LFPG", 1606262400000, "N0431F370 DH632",
                                        "EDDH", 7100000, 1606269600000, "closed", "DAAA", "FPL-EWG8XZ/A1411-IS-A320/M-S/S-LFPG0000-N0431F370 DH632-EDDH0200-REG/DAAAA")
    EvaluateFlightplan.evaluateFlightplan(flightplanData)
    radarData = RadarDataset("EWG36",
        1606315528655,
        10.240887,
        53.743989,
        -2)
    EvaluateRadar.evaluateRadar(radarData)
    avgDict = EvaluateAverage.evaluateAverage(checkList)
    calculateSeverity(avgDict)

# append to checklist and kicks first element out if length of checklist is larger than CHECKLIST_MAX
def listAppend(data):
    global checkList
    if len(checkList) <= CHECKLIST_MAX: 
        checkList.append(data)
    else:
        checkList = checkList[1:].append(data)

if __name__ == "__main__":
    main()