import authoralso, fiveexpensive, hasyear, longcd, json, pprint

def loadjson():
    with open('sample.json') as f: #implicitly closes file after done
        return json.loads( f.read() )

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
        data = loadjson()
        res = userfunc(data)
        pprint.pprint(res)
        #feed json into userfunc(json)

if __name__ == "__main__":
    '''if this file is being run as the main file, this is the main function'''
    menu()