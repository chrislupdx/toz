'''What are the 5 most expensive items from each category? '''

def evictCheapest(typeArr):
    '''evictCheapest is a helper function that removes the cheapest item from a list of items'''
    typeArr.sort(reverse = False, key = lambda items: items["price"])
    typeArr.pop(0)

# def topfive(data, returnData):
def topfive(data):
    '''topfive returns an map from category to the five most expensive items in that respective category'''
    print("running topfive:")
    returnData = {}
    for item in data:
        if item["type"] not in returnData:
            returnData[item["type"]] = []
            returnData[item["type"]].append(item)
        elif len(returnData[item["type"]]) >= 5:
            returnData[item["type"]].append(item)
            evictCheapest(returnData[item["type"]])
        else:
            returnData[item["type"]].append(item)                    
    return returnData