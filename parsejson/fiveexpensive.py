import json
import unittest
f = open('sample.json')
#json.dumps py object -> json
#what is json.loads() takes json -> py object

data = json.loads( f )
refinedata = json.loads(data)

#This function parses json for the 5 most expensive items from each category
#unit testing in python 
    #do we have an entire test class for the entire function?

#def printjson(data):
#    print(data)

#printjson()
print(refinedata)

f.close()
#figure out if p

#a function that takes sample.json

#write a function that parses the json by "type" for the highest price,
    #i think a simple grab the first of each type and iterate through each respective set of items for each type.
