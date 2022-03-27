#Which authors have also released cds?
def authorsboth(data, returnData):
    print("running authorsboth:")
    cdAuthors = []
    bookAuthors = []
    for item in data:
        if item["type"] == "cd":
            cdAuthors.append(item["author"])
        if item["type"] == "book":
            bookAuthors.append(item["author"])
    setbookAuthor = set(bookAuthors)
    setcdAuthor = set(cdAuthors)
    returnData = setbookAuthor.intersection(setcdAuthor)
    return returnData