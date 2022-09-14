import sys

def con_value(slave):
    for num in slave:
        if num % 2 == 0:
            list_2.append(num)
    print("Here is the original list", slave)
    print("Here is the list without uneven numners", list_2)


list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list_2 = []

con_value(list_1)






sys.exit(0)