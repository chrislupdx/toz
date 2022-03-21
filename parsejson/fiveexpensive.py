import json
import unittest

def printJSON(data):
    for item in data:
        print(item)
returnData = {}

#grab the 5 greatest prices from each category
def topfive(data, returnData):

    #count tne number of categories and the number of items in each category
    addedCategories = {}
    for item in data:
        if item["type"] not in addedCategories:
            addedCategories[item["type"]] = 0 #maybe throw on a count of items of that specific type?
        else: 
            addedCategories[item["type"]] =  addedCategories[item["type"]]  + 1
    print(addedCategories)

    #decrement each item{"type"} each time we find a specific type
    for item in data:
        

with open('sample.json') as f:
    data = json.loads( f.read() )
    topfive(data, returnData)
    # print("printing items in returndata")
    # for item in returnData:
    #     print(item)
f.close()