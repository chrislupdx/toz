import authoralso, fiveexpensive, hasyear, longcd, json

class interface():
    def openjson(userfunc):
        #I tried grouping these together and python didn't quite like that so that's why each condition gets its own unique elif
        if userfunc is hasyear.hasyear:
            returnData = []
        elif userfunc is longcd.longerthansixty:
            returnData = []
        elif userfunc is authoralso.authorsboth:
            returnData = {}
        elif userfunc is fiveexpensive.topfive:
            returnData = {}
        with open('sample.json') as f:
            data = json.loads( f.read() )
            returnData = userfunc(data, returnData)
            print("returnData after is ", returnData)
        f.close()

    def menu():
        done = False
        while(done is False):
            print("Tozny takehome (parsing json) \n 1. has year \n 2. author also \n 3. cd length \n 4. five most expensive \n 5. exit")
            userinput = int(input())
            if(userinput == 1):
                userfunc = hasyear.hasyear
            if(userinput == 2):
                userfunc = authoralso.authorsboth
            if(userinput == 3):
                userfunc = longcd.longerthansixty
            if(userinput == 4):
                userfunc = fiveexpensive.topfive
            if(userinput == 5):
                print("exiting, bye!")
                return
            interface.openjson(userfunc)

interface.menu()