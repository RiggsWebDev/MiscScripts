import random

"""


Welcome to Rock Paper Scissors!


"""


#User chooses what he wants to play, or can choose to quit
userinput = str(input("Choose (R)ock, (P)aper, (S)cissors, or (Q)uit\n")).lower()

#Random generation choices for the PC
pcinput = random.randint(1,3)
if pcinput == 1:
    pcinput = "rock"
elif pcinput == 2:
    pcinput = "paper"
elif pcinput == 3:
    pcinput = "scissors"

#Declaration of choices
if userinput == "q":
    quit()
elif userinput == "r":
    print("\nYou've chosen rock!")
elif userinput == "p":
    print("\nYou've chosen paper!")
elif userinput == "s":
    print("\nYou've chosen scissors!")
else:
    print("Bye!")
    quit()

print("The computer has chosen",pcinput+"!\n")

#Rock Choices
if userinput == "r" and pcinput == "rock":
    print("It's a draw")
elif userinput == "r" and pcinput == "paper":
    print("You lose!")
elif userinput == "r" and pcinput == "scissors":
    print("You win")

#Paper Choices
elif userinput == "p" and pcinput == "rock":
    print("You win")
elif userinput == "p" and pcinput == "paper":
    print("It's a draw")
elif userinput == "p" and pcinput == "scissors":
    print("You lose!")

#Scissors Choices
elif userinput == "s" and pcinput == "rock":
    print("You lose!")
elif userinput == "s" and pcinput == "paper":
    print("You win")
elif userinput == "s" and pcinput == "scissors":
    print("It's a draw")
