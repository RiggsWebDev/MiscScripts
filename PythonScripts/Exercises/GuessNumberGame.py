import random

#starts with the number 15 they have to pick, afterwards randomizing during each call of guess()
x = 15

#keeps track of wins
winner = 0

"""
def makerandom():
    global x
    x = 0
    x = random.randint(1,50)
    guess()
"""

def guess():
    global x
    global winner


    #this is for troubleshooting, prints the number it picks. 
    #print(x)


    y = int(input("Guess a number!\n"))
    if x > y:
        print("You number is too low!")
        guess()
    elif ValueError: 
        print("Choose a number instead...")
        guess()
    elif x < y:
        print("You number is too high")
        guess()
    elif x == y:
        winner += 1
        x = random.randint(1,50)
        print("You win!")
        print("You've won",winner,"times!")
        
        #Every 5 wins it asks if you still want to play as to not be completely tedious
        if winner % 5 == 0:
            wn = input("Do you still want to play? (Y)es or (N)o\n").lower()
            if wn == "y":
                guess()
            if wn == "n":
                quit()
        guess()

guess()
