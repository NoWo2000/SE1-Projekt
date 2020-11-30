# evalutes the average of the last 10 datasets
# returns dictionary
def evaluateAverage(checkList):
    average = {
        "cpuUsage": 0,
        "ramUsage": 0,
        "serverLoginFailed": 0,
        "serverLoginSuccess": 0,
        "trafficUpload": 0,
        "trafficDownload": 0
    }

    for dataset in checkList:
        for var in dir(dataset):
            average[var] += eval("dataset."+var)
    for key in average:
        average[key] /= len(checkList)
    
    return average