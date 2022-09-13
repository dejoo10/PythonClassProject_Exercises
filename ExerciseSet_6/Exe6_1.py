
import random
import sys


def dice_roll():
    return random.randint(1,6)


value = dice_roll()

while value != 6:
    print("The result of dice rolled is", value)
    value = dice_roll()
    if value == 6:
        print("End of rolling because you have a", value)


sys.exit(0)

