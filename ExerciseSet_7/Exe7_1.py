import random
import sys


user = int(input("Enter the number of the month:"))
seasons = ("spring", "summer", "autumn", "winter")
if user in range(3, 6):
    print(seasons[0])
elif user in range(6, 9):
    print(seasons[1])
elif user in range(9,12):
    print(seasons[2])
elif user in range(1, 2) or user == 12:
    print(seasons[3])
else:
    print("invalid")


sys.exit(0)



user = int(input("Enter the number of the month:"))

if user in range(2, 4):
    print("Spring")
elif user in range(5, 7):
    print("Summer")
elif user in range(8, 10):
    print( "Autumn")
elif user in range(11,12) or range(1):
    print("Winter")
else:
    print("Season not found")





#mnt = seasons[user-1]













sys.exit(0)