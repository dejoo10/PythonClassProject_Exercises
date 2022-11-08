import sys
import requests
import json

keyword = "random"

request = "https://api.chucknorris.io/jokes/" + keyword
response = requests.get(request).json()
print(response["value"])


sys.exit(0)