import sys
import random

#here is the exercise 4-4

randomA = int(input("Enter your guess:...."))

randomB = random.randint(1,10)

while randomA != randomB:
    print("your guess is", randomA, "and number is ", randomB)
    if (randomA != randomB) and (randomA > randomB):
        print(" number", randomA, "is too high ")
    elif (randomA != randomB) and ( randomA < randomB):
        print(" number", randomA, "is too low")

    randomA = int(input("Enter your guess again:.."))
    randomB = random.randint(1, 10)

print( "number", randomA, "is correct")
print( "numbers are", randomA, "and", randomB)




sys.exit(4)