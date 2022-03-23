import json
import unittest

def printJSON(data):
    for itemList in data:
        print(itemList, "\n")

returnData = {}

def evictCheapest(typeArr):
    typeArr.sort(reverse = False, key = lambda items: items["price"])
    typeArr.pop(0)

def topfive(data, returnData):
    for item in data:
        if item["type"] not in returnData:
            returnData[item["type"]] = []
            returnData[item["type"]].append(item)
        elif len(returnData[item["type"]]) >= 5: #eviction
            returnData[item["type"]].append(item)
            evictCheapest(returnData[item["type"]])
        else:
            returnData[item["type"]].append(item)                    
    print(returnData)

with open('sample.json') as f:
    data = json.loads( f.read() )
    returnData = topfive(data, returnData)
    print("printing items in returndata")
    #printJSON(returnData)
    print(returnData)
f.close()

#RESULTS (parsed by hand)
#BOOK: 11.99, 12.99, 13.99, 14.99, 15.99
#dvd: 11.99, 11.99, 11.99, 11.99, 
#CD: 16.99, 17.99, 18.99, 19.99, 20.99. 

#expected
#Book: 15.99, 14.99, 13.99, 12.99, 11.99
#DVD: 11.99, 11.99, 11.99, 11.99
#CD: 16.99, 17.99, 18.99, 19.99, 20.99
