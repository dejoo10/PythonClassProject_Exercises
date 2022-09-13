import random
import sys


def dic_roll(side):
    for i in range(side):
        roll = random.randint(1,6)
        print(roll)
    return

side_arg = int(input("Enter the numbers of sides of your dice:..."))
dic_roll(side_arg)



sys.exit(1)

#The code below run differently, it is not what the exercise asked, see the code on top.
def dice_roll():
    return random.randint(1,6)


value = dice_roll()
count = 0
side = int(input("number of side :..."))

while count < side:
    print("The result of dice roll is", value)
    value = dice_roll()
    count = count + 1
print("End")


sys.exit(0)