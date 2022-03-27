#parses the json for cds with length that runs longer that 60 minutes
minlen = 3600 #sixy minutes is 3600 seconds
def sumTrackTime(cddata, totalLength):
    for tracks in cddata["tracks"]:
        totalLength = totalLength + tracks["seconds"]
    return totalLength

def longerthansixty(data, returnData):
    print("running longer than sixty seconds")
    for item in data:
        if item["type"] == "cd":
            totalLength = 0
            totalLength = sumTrackTime(item, totalLength)
            if totalLength > minlen:
                returnData.append(item)
    return returnData