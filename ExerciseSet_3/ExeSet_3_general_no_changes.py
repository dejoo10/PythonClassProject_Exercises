import math
import random


#The code below is for the exercise 3-4



Year_value = int(input("Enter a year:..."))
if (Year_value % 4 == 0 and Year_value % 100 !=0) or (Year_value % 400 == 0) :
    print( Year_value, "is a leap year")
else:
    print(Year_value, "is not a leap year")


sys.exit(0)

#the code below is for the exercise 3-3


Gender_type = str(input(" What is your gender:.."))
Hemoglobin_value = float(input(" Enter your hemoglobin value:..."))

if Gender_type == "female" and Hemoglobin_value < 117:
    print(" Your hemoglobin value is low")
elif Gender_type == "female" and 117 <= Hemoglobin_value <=155:
    print(" Your hemoglobin value is normal ")
elif Gender_type == "female" and Hemoglobin_value >155:
    print(" Your hemoglobin value is high.")
elif Gender_type == "male" and Hemoglobin_value < 134:
    print(" Your hemoglobin value is low")
elif Gender_type == "male" and 134 <= Hemoglobin_value <=167:
    print(" Your hemoglobin value is normal ")
elif Gender_type == "male" and Hemoglobin_value >167:
    print(" Your hemoglobin value is high.")
else:
    print(" Invalid ")





sys.exit(0)

#The code below is for the exercise 3-2

Cabin_class = (input("Enter the cabin class you belong:..."))
if Cabin_class == "A" :
    print(" above the car deck, equipped with a window")
elif Cabin_class == "B":
    print("windowless cabin above the car deck.")
elif Cabin_class == "C" :
    print("windowless cabin below the car deck.")
elif Cabin_class == "LUX":
    print(" upper-deck cabin with a balcony.")
else:
    print(" Invalid cabin class")


sys.exit(0)
#the code below is for the exercise 3-1


Got_zander = int(input("what is the length of the zander fish you got in cm:... "))
Zander_size = Got_zander - 42
if  Got_zander < 42:
    print("Return the fish into the lake, because the fish is", Zander_size , "cm shorter than the allowed limit ")
else:
    print(" Congratulations")





sys.exit(0)