import random

"""

Welcome to Rock Paper Scissors!


"""

userinput = str(input("Choose (R)ock, (P)aper, (S)cissors, or (Q)uit\n")).lower()
pcinput = random.randint(1,3)
if pcinput == 1:
    pcinput = "r"
elif pcinput == 2:
    pcinput = "p"
elif pcinput == 3:
    pcinput = "s"


if userinput == "q":
    quit()
elif userinput == "r":
    quit()
