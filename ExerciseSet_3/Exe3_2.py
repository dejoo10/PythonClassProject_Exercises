import sys

#The code below is for the exercise 3-2

Cabin_class = (input("Enter the cabin class you belong:...")).upper()
if Cabin_class == "A" :
    print(" above the car deck, equipped with a window")
elif Cabin_class == "B":
    print("windowless cabin above the car deck.")
elif Cabin_class == "C" :
    print("windowless cabin below the car deck.")
elif Cabin_class == "LUX":
    print(" upper-deck cabin with a balcony.")
else:
    print(" Invalid cabin class")


sys.exit(0)