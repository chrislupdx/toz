import authoralso, fiveexpensive, hasyear, longcd, json

class interface():
    def openjson(userfunc):
        #returnData = {}
        if userfunc is hasyear or longcd:
           returnData = []
        if userfunc is fiveexpensive or authoralso:
           returnData = {}
        with open('sample.json') as f:
            data = json.loads( f.read() )
            returnData = userfunc(data, returnData) #then hit that
            print("printing return data \n", returnData)
        f.close()

    def menu():
        print("Tozny takehome (parsing json) \n 1. has year \n 2. author also \n 3. cd length \n 4. five most expensive")
        userinput = int(input())
        if(userinput == 1):
            userfunc = hasyear.hasyear
        if(userinput == 2):
            userfunc = authoralso.authorsboth
        if(userinput == 3):
            userfunc = longcd.longerthansixty
        if(userinput == 4):
            userfunc = fiveexpensive.topfive
        interface.openjson(userfunc)


interface.menu()