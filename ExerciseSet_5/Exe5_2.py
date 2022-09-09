import sys
import numbers


mylist = []
x = []

empty = ""

number = input("enter any number to start:..")
while number != empty:
    number = input("enter number")
    if number == empty:
        break
    else:
        mylist.append(number)
print(mylist)
mylist.sort(reverse=True)
print(mylist)
max = ({max(mylist)})
min = ({min(mylist)})





sys.exit(0)