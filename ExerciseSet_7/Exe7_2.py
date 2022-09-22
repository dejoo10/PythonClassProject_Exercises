import sys

#This code is not working properly yet

names = set()
empty = ""

count = 0
while True:
    user = input("Enter any name")
    names.add(user)

    if user == "":
        break
        count = count + 1
for i in names:
    if user == i in names:
        print("name exist")
    else:
        print("name is new")



print(names)




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


