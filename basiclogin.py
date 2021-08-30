import time
import os


def welcome():
    print ("Welcome to a basic Python login screen!")
    welcomemenu = str(input("Type \"Login\", \"Register\", or \"Close\" \n")).lower() 
    if welcomemenu == "login":
        print ("Welcome to the login screen")
        login()
    if welcomemenu == "register":
        print ("Welcome to the register screen")
        register()
    if welcomemenu == "close":
        quit()
    if welcomemenu not in ["login", "register", "close"]:
        print("This is not recognized please try again")
        welcome()

def register():
    username =  str(input("***CASE SENSITIVE***\nPlease enter a username \n")).lower() 
    file = open("C:/test/User_Dat.txt","a")
    for line in open("C:/test/User_Dat.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username == login_info[0]:
            print("There is already a user with this name please try again.")
            register()
    file.write(username)
    file.write(" ")
    file.write("\n")
    file.close()
    login()

def login():
    username = input("***CASE SENSITIVE***\nPlease enter your username  \n").lower() 
    for line in open("C:/test/User_Dat.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username == login_info[0]:
            print("Correct credentials!")
            print("You are now logged in!")
            startgame()
            return True
        else:
            print("Incorrect credentials.")
            time.sleep(2)
            welcome()
            return False

def startgame():
    print("Loading [--        ]")
    time.sleep(1)
    print("Loading [-----     ]")
    time.sleep(1)
    print("Loading [--------  ]")
    time.sleep(1)
    print("Loading [----------]")
    
welcome()
