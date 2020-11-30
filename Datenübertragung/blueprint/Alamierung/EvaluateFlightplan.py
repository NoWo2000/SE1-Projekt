

def evaluateFlightplan(flightplanData):
    time = flightplanData.eta - flightplanData.eet
    if flightplanData.eobt != time:
        alarm(75, ["eta", "eet", "eobt"])
    if flightplanData.status not in ['closed', 'scheduled', 'departed', 'initiated']:
        alarm(75, ['Status'])
    if len(flightplanData.registration) != 4:
        alarm(75, ['Registration'])
    if len(flightplanData.destination) != 4:
        alarm(75, ['Destination'])
    if len(flightplanData.origin) != 4:
        alarm(75, ['Origin'])
    if len(flightplanData.callsign) < 4 or len(flightplanData.callsign) > 7:
        alarm(75, ['Callsign']) 
    