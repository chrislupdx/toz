#Which items have a title, track, or chapter that contains a year.
def hasyear(data, returnData):
    print("running hasyear")
    for item in data:
        if(item["title"] or item["tracks"] or item["chapter"]):
            if(item["year"]):
                returnData.append(item)
    return returnData