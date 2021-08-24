"""
Extremely basic calendar that I might use later on,
could easily make for some cool looking front-end stuff
"""
   
import calendar
   
yy = int(input("What year is it? : "))
mm = int(input("What month is it? (numerical values only) : "))
   
# display the calendar
print("Here is the monthly calendar you requested!")
print(calendar.month(yy, mm))