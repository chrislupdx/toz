import json
import unittest
f = open('sample.json', 'r')
data = json.loads(f)
for i in data:
    print(i) 


# with open('sample.json') as f:
#     data = json.loads( f.read() )
#     for item in data: 
#         print(item)
#This function parses json for the 5 most expensive items from each category
#unit testing in python 
    #do we have an entire test class for the entire function?

#def printjson(data):
#    print(data)

#printjson()
#print(refinedata)

f.close()
#figure out if p

#a function that takes sample.json

#write a function that parses the json by "type" for the highest price,
    #i think a simple grab the first of each type and iterate through each respective set of items for each type.

