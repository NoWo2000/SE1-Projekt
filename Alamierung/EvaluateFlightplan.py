from Alarm import alarm

def eval(flightplanData):
    time = flightplanData.eta - flightplanData.eet
    if(flightplanData.eobt != time):
        alarm(75, ["eta", "eet", "eobt"])

        

