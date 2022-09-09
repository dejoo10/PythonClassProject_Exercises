import sys

#The code below is the exercise 4-3





mylist = []
enter_values = int(input("Enter any number to start:..."))

while enter_values != "":

    enter_values = (input("Enter number again:..."))
    if enter_values == "":
        break
    mylist.append(enter_values)
print("End of listing, below is the list you made")
print(mylist)
print(f"The smallest number is {min(mylist)}")
print(f"The largest number is {max(mylist)}")


#print(f"end : smallest and largest number are: {smallest} and {largest}")






sys.exit(0)
