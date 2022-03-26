#this guy is a class interface
#import hasyear, authoralso, longcd, fiveexpensive

class interface():
    def menu():
        #this gets thrown into a while loop
        print("Tozny takehome (parsing json) \n 1. has year \n 2. author also \n 3. cd length \n 4. five most expensive")
        #takes in userintput via command line to pick wihch one
        userinput = 0
        if(userinput == 1):
            print('running has year')
        if(userinput == 2):
            print("running author also")
        if(userinput == 3):
            print("running cd length")
        if(userinput == 4):
            print("running five most expensive")


interface.menu()