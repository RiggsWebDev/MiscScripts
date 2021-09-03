import time, sys

banana = 0 
bananabomb = True

try:
    while True:
        print(' ' * banana, end='')
        print('banana')
        time.sleep(0.025)

        if bananabomb == True:
            # space the bananas out:
            banana = banana + 1
            if banana == 20:
                # bananas go the other way now:
                bananabomb = False
        else:
            banana = banana - 1
            if banana == 0:
                bananabomb = True
except KeyboardInterrupt:
    sys.exit()
