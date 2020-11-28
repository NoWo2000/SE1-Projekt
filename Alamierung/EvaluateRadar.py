from Dataset import RadarDataset
from Alarm import alarm

def eval(radarDataset):
    if len(radarDataset.callsign) < 4 or len(radarDataset.callsign) > 7:
        alarm(75, ['Callsign'])
    if radarDataset.alt < 0:
        alarm(75, ['Altidude'])
    if radarDataset.lat < -180 or radarDataset.lat > 180:
        alarm(75, ['Latidude'])
    if radarDataset.lon < -90 or radarDataset.lon > 90:
        alarm(75, ['Longitude'])
   
    