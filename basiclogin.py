def welcome():
    print ("Welcome to a basic Python login screen!")
    welcomemenu = str(input("Type \"Login\" or \"Register\" \n")).lower() 
    if welcomemenu == "login":
        print ("Welcome to the login screen")
    if welcomemenu == "register":
        print ("Welcome to the register screen")
    if welcomemenu not in ["login", "register"]:
        print("This is not recognized please try again")

welcome()