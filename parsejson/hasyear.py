import json
#Which items have a title, track, or chapter that contains a year.
returnData = []

def hasyear(data, returnData):
    for item in data:
        #check if it has a title, track, or chapter
        if(item["title"] or item["tracks"] or item["chapter"]):
            if(item["year"]):
                print(item)
                returnData.append(item)
    return returnData

with open('sample.json') as f:
    data = json.loads( f.read() )
    returnData = hasyear(data, returnData)
    #print(returnData)
f.close()