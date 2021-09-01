#Answering the Guess the Number question for Automate the Boring Stuff

import random
x = 0
x = random.randint(1,50)
def guess():
    y = int(input("Guess a number!\n"))
    if x > y:
        print("You number is too low!")
        guess()
    elif x < y:
        print("You number is too high")
        guess()
    elif x == y:
        print("You win!")

guess()
