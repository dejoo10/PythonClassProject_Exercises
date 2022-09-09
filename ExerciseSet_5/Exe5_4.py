import sys


my_city = []

for n in range(0,5):
    city = input("Enter the name of a city:...")
    my_city.append(city)
print(my_city)
for i in my_city:
    print(f"{i}")


sys.exit(0)


my_cities = []
#cities = input("Enter the name of a city:...")
count = 0

while count<5:
    cities = input("Enter the name of a city:...")
    my_cities.append(cities)

    count = count+1
print(my_cities)
for i in my_cities:
    print(f"{i}!")




sys.exit(0)