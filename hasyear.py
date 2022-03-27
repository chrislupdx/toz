'''Which items have a title, track, or chapter that contains a year.'''
def hasyear(data):
    '''hasyear returns returns an list of items with a year section which also has a title, track, or chapter'''
    print("running hasyear:")
    returnData = []
    for item in data:
        if(item["title"] or item["tracks"] or item["chapter"]):
            if(item["year"]):
                returnData.append(item)
    return returnData