import sys
import numbers





#This code is not working yet

number = (input("Enter a number to start:..."))
mylist = []
while number != "":
    number = (input("Enter number again:..."))
    if number == "":
        break
    mylist.append(number)
    mylist.sort(reverse=True)
print(mylist)
max = ({max(mylist)})
min = ({min(mylist)})




sys.exit(0)


mylist = []
x = []

empty = ""

number = input("enter any number to start:..")
while number != empty:
    number = input("enter number")
    if number == empty:
        break
    mylist.append(number)
mylist.sort(reverse=True)
print(mylist)
max = ({max(mylist)})
min = ({min(mylist)})





sys.exit(0)