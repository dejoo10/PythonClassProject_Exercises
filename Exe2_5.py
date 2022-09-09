#Here is exercise 2_5

import sys

print("This is a program that make use of the medieval units")
Talent = float(input("enter the value of talent:"))
Pounds = float(input("enter the value of pounds:"))
lot = float(input("enter the value of lot:"))
Value_lbs = Talent * 20
Value_lots = Value_lbs * 32

print("the value in g is =",Value_lots * 13.3 , "g")
print("the value in kilograms is =", (Value_lots * 13.3)/1000, "Kg")


sys.exit(4)
