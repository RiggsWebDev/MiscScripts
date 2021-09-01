# Just another test to use the random module + a while loop that does a few things when checking to see if the number is 9. 

""""
x = int(input("Type a number\n"))
y = int(input("Type a second number\n"))

if x * y > 1000:
    print(x+y)
else:
    print(x*y)



name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')
"""

import random
for i in range(5):
    print(random.randint(1, 10),"\n")



x = 0

while x != 9:
    print ("Randomly rolling until we hit number 9")
    x = random.randint(1,50)
    if x in [1, 50]:
        print("DING DING DING YOU HIT THE MAX OR MIN NUMBER")
    print (x)
