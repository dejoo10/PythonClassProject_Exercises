import sys

number = int(input("Please enter an integer value"))
if number >= 1:
    for i in range(2, number // 2):
        if (number%i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

sys.exit(0)