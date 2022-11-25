import sys
import requests
import json

# My key = f3c6b7ac910f2327d8538fdf4c514951

def get_temp_kelvin(city, api_key):
    request = "http://api.openweathermap.org/data/2.5/weather?q=" + city + f"&appid={api_key}"
    response = requests.get(request).json()
    kelvin = response['main']['temp']
    return kelvin
def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

city = input("Enter the name of the city you want to view: ")
api_key ="f3c6b7ac910f2327d8538fdf4c514951"
kelvin = get_temp_kelvin(city, api_key)
celsius = kelvin_to_celcius(kelvin)
print(f"The temperature in {city} is {round(celsius,1)} degrees celsius")


sys.exit(0)