import time
import os


def welcome():
    print ("Welcome to a basic Python login screen!")
    welcomemenu = str(input("Type \"Login\" or \"Register\" \n")).lower() 
    if welcomemenu == "login":
        print ("Welcome to the login screen")
        login()
    if welcomemenu == "register":
        print ("Welcome to the register screen")
        register()
    if welcomemenu not in ["login", "register"]:
        print("This is not recognized please try again")

def register():
    username =  str(input("Please enter a username \n")).lower()
    file = open("User_Data.txt","a")
    for line in open("User_Data.txt","r").readlines(): # Read the lines
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
    username = input("Please enter your username  \n").lower()
    for line in open("User_Data.txt","r").readlines(): # Read the lines
        login_info = line.split() # Split on the space, and store the results in a list of two strings
        if username == login_info[0]:
            print("Correct credentials!")
            print("You are now logged in!")
            startgame()
            return True
    print("Incorrect credentials.")
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
