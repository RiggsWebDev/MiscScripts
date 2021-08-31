"""

Practicing the fundamentals of loops that counts to 100 and afterwards states that it counted to 100. 


"""

counter = 1 
while counter < 100:
    counter = counter + 1
    print(counter)
total = counter
if counter >= 100:
    print("The script has finished counting to",counter)
    print("Because I put the total variable set to the counte after the loop it also equals",total)
