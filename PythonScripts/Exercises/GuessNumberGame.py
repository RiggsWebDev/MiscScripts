import random
x = 15
winner = 0

"""

I danced around the possibility of making the game revolve around two seperate functions, but decided against it after prototyping a little.
Keeping this here in case I decide to change my mind. 

def makerandom():
    global x
    x = 0
    x = random.randint(1,50)
    guess()
"""

def guess():
    global x
    global winner
    print(x)
    y = int(input("Guess a number!\n"))
    if x > y:
        print("You number is too low!")
        guess()
    elif x < y:
        print("You number is too high")
        guess()
    elif x == y:
        winner += 1
        x = random.randint(1,50)
        print("You win!")
        print("You've won",winner,"times!")
        if winner > 5:
            wn = input("Do you still want to play? (Y)es or (N)o\n").lower()
            if wn == "y":
                guess()
            if wn == "n":
                quit()
        guess()

guess()
