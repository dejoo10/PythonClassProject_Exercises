import sys

#The code below is the exercise 4-2


inch_value = float(input("enter value in inches:..."))
#1 inch = 2.54cm

while inch_value >= 0:
    cm_value = inch_value * 2.54
    print(f"value of", inch_value ,"inches in cm is ", cm_value, "cm")
    inch_value = float( input( " enter value in inches again:..."))
else:
    print( "end")



sys.exit(0)