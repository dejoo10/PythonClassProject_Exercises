import sys
import random

#This is exercise 4_6

#nxt or nyt = n in the question paper
#point_total = N in the question paper
#you made a list, the get the length of that list to creat n

point_total = float(input("Enter the total number of points to generate:.."))

x_axis = 1
y_axis = 1
i = 0
list1 = []
list2 = []
list3 = []
list4 = []

while i < point_total:
    point_x = random.random()
    point_y = random.random()

    i = i + 1
    test = point_x**2 + point_y**2
    if test < 1:
        list1.append(point_x)
        list2.append(point_y)
        #print("it fit into the circle")
    else:
        #print("it does not fit in the circle")
        list3.append(point_x)
        list4.append(point_y)


#print(list1)
#print(list2)
#print(list3)
#print(list4)
nxt = len(list1)
nyt = len(list2)
#print(nxt)
#print(nyt)
pi = (4*nxt)/point_total
print(f"{pi:.3f}")

