# A program that outputs whether or not it is a weekday.
# Author: Ben Janning

# Import 'datetime' library so we can use its functions:
from datetime import datetime

# Create a variable which is equal to the value of below function
# and will output the day of the week.
# Monday - Sunday are represented by 0-6.
dayOfWeek = datetime.today().weekday()

#Create an if/else statement to calculate the day of week and print the result.
if dayOfWeek <= 4:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")