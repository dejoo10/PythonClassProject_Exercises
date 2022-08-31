

from random import randint

print("Below is the code that generate random numbers between 0 to 9")
tree_digit = ""
for i in range(3):
    tree_digit = tree_digit + str(randint(0,9))
print(tree_digit)

print("Below is the code that generate random numbers between 0 to 6")
four_digit = ""
for j in range(4):
    four_digit = four_digit + str(randint(0,6))
print(four_digit)
