#here is exercise 3_4
import sys

year = int(input('Enter year : '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
sys.exit(1)