#Takes a user input of two numbers and those two numbers multiplied are over 1000 then instead it adds them. 
#Solving some basic python exercises with this

x = int(input("Type a number\n"))
y = int(input("Type a second number\n"))

if x * y > 1000:
    print(x+y)
else:
    print(x*y)
