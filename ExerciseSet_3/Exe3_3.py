import sys

#the code below is for the exercise 3-3


Gender_type = str(input(" What is your gender:..")).lower()
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