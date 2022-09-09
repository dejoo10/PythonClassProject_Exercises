import sys
#The code below is the exercise 4-1
max_num = 1000
num1 = 1
#remember the challenge you had in this exercise was getting the range specified into the storage

while num1 <= max_num:
    if num1 % 3 == 0:
        print(num1)
    num1 = num1 + 1


sys.exit(0)