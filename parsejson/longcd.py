#parses the json for cds with length that runs longer that 60 minutes
#convert 60 minutes into seconds
# Which cds have a total running time longer than 60 minutes?
import json

#sixy minutes is 3600 seconds
minlen = 3600
returnData = []

#sum up track seconds
def sumTrackTime(cddata, totalLength):
    for tracks in cddata["tracks"]:
        totalLength = totalLength + tracks["seconds"]
    #print("in sumtrack totallength is", totalLength)
    return totalLength

#creates an array of cds with tracks longer than 60 minutes
def longerthansixty(data, returnData):
    for item in data:
        if item["type"] == "cd":
            totalLength = 0
            #print(item["tracks"])
            totalLength = sumTrackTime(item, totalLength)
            # print("totallength after is ", totalLength)
            if totalLength > minlen:
                returnData.append(item)

with open('sample.json') as f:
    data = json.loads( f.read() )
    longerthansixty(data, returnData)
    print(returnData)
f.close()