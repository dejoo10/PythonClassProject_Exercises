import sys
import random

dice_roll = []

monta = int(input("Enter the amount of dice to roll"))

for x in range(monta):
    dice1 = random.randint(1, 6)
    dice_roll.append(dice1)

print(dice_roll)
print(f"sum of the rolled diced is {sum(dice_roll)}")