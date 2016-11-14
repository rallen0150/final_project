import requests

url = "http://localhost:8000/api/foodtrucks/"

json_result = requests.get(url).json()

# print(json_result)

for x in json_result:
    print("{}, {}".format(x['latitude'], x['longitude']))
