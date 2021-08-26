def evenorodd(x):
    if x % 2 == 0:
        print("You entered an even number!")
    if x % 2 > 0:
        print("Odd number.")

x = int(input("Pick a number: "))
evenorodd(x)