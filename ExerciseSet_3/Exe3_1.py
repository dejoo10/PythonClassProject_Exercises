import sys


#the code below is for the exercise 3-1


Got_zander = int(input("what is the length of the zander fish you got in cm:... "))
Zander_size = Got_zander - 42
if  Got_zander < 42:
    print("Return the fish into the lake, because the fish is", Zander_size , "cm shorter than the allowed limit ")
else:
    print(" Congratulations")





sys.exit(0)