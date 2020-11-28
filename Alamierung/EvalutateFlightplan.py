
def eval(flightplanData):
    time = flightplanData.eta - flightplanData.eet
    if(flightplanData.eobt != time):
        

