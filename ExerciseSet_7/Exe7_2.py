import sys
from collections import Counter

#This code is not working properly yet

names = set()
empty = ""
en = len(names)

user = input("Enter a name")
while True:
    user = input("Enter a name")
    names.add(user)
    print(names)
    if user in names:
        print("Exist")
    else:
        print("new")
    if user == empty:
        break






sys.exit(0)
empty = "x"
names = set()

count = 0
while empty != "":
    user = input("Enter any name")
    names.add(user)
    if user == "":
        break
        count = count + 1
    print(names)
    for user in names:
        if user == names:
            print("Existing name")
        else:
            print("New name")

sys.exit(0)
while user != "":
    user = input("Enter name again")
    names.add(user)
    if user == "":
        break
    print(names)
print(names)


