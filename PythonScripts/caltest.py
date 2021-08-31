"""
Extremely basic calendar that I might use later on,
could easily make for some cool looking front-end stuff
"""
   
import calendar
   
year = int(input("What year is it? : "))
month = int(input("What month is it? (numerical values only) : "))
   
"""
Returned value with formatted calendar look thanks to the calendar import
"""

print("Here is the monthly calendar you requested!")
print(calendar.month(year, month))
