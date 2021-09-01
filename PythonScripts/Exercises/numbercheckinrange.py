"""

Basic number range check to see if a value is below 100, within 100 to 1000, within 1001 to 2000, or above 2000. 

I would imagine there is a way to do this in a lot less code. If anyone actually sees this please feel free to show me. 

Maybe I'll update it way later on and see some progress or improvements. For now it's what I could do!

"""


x = int(input("Type a number up to 2500: "))
in_numbers = x in range(100,1000)
in_numbers2000 = x in range(1001,2000)
if in_numbers == True:
    print("Your number is between 100 and 1000!")
elif in_numbers2000 == True:
    print("You number is between 1001 and 2000!")
elif x <= 99:
    print("Your number is lower than 100")
elif x >= 2001:
    print("Your number is higher than 2000")
else:
    quit()

#Added a Windows/DOS only wait key
#Maybe not the most user-friendly or Pythonic way of doing it...
#but curiousity got the better of me, if it could be done. 

import msvcrt as m

def wait():
    m.getch()

wait()

"""

I did fix it with more code and there are some glaring errors I found while fixing this, such as a number higher than 2000 returned that it's lower than 100....

But my original issue persists, why if it's hitting one of the true statements does it return the else value in the below code?

Why does this return the else regardless of value? For example when running this you can enter a number between 100 and 1000
or a number between 1001 and 2000, and you'll get either print but you will additionally get the print message
that states your number is lower than 100. 

I need to do more research behind elif statements, I suppose. 


x = int(input("Type a number up to 2500: "))
in_numbers = x in range(100,1000)
in_numbers2000 = x in range(1001,2000)
if in_numbers == True:
    print("Your number is between 100 and 1000!")
elif in_numbers2000 == True:
    print("You number is between 1001 and 2000!")
else:
    print("Your number is lower than 100")


"""
