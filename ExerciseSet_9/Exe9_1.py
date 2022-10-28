import sys


class Car:

    def __init__(self, registration_number, Max_speed, Current_speed = 0, Travelled_distance = 0):
        self.registration_number = registration_number
        self.Max_speed = Max_speed
        self.Current_speed = Current_speed
        self.Travelled_distance = Travelled_distance

car1 = Car("ABC-123", "142 Km/h")

print(car1.Max_speed)
print(car1.registration_number)
print(car1.Travelled_distance)
print(car1.Current_speed)




sys.exit(0)