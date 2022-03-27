def evictCheapest(typeArr):
    typeArr.sort(reverse = False, key = lambda items: items["price"])
    typeArr.pop(0)

def topfive(data, returnData):
    print("running topfive")
    for item in data:
        if item["type"] not in returnData:
            returnData[item["type"]] = []
            returnData[item["type"]].append(item)
        elif len(returnData[item["type"]]) >= 5: #eviction
            returnData[item["type"]].append(item)
            evictCheapest(returnData[item["type"]])
        else:
            returnData[item["type"]].append(item)                    
    return returnData