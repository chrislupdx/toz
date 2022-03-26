#which authors have released cds?
import json
#an array of authors that have released books and CDs
returnData = {}

#traverses JSON for 
def authorsboth(data, returnData):
    cdAuthors = []
    bookAuthors = []
    commonAuthors = {}
    for item in data:
        if item["type"] == "cd":
            #should we assume each author named john is distinct?
            #print(item["author"])
            cdAuthors.append(item["author"])
        if item["type"] == "book":
            bookAuthors.append(item["author"])
    # print("bookauthor is ", bookAuthors)
    # print("cdautor is ", cdAuthors)
    setbookAuthor = set(bookAuthors)
    setcdAuthor = set(cdAuthors)
    returnData = setbookAuthor.intersection(setcdAuthor)
    return returnData

with open('sample.json') as f:
    data = json.loads( f.read() )
    returnData = authorsboth(data, returnData)
    print(returnData)
f.close()