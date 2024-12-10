import json
import requests


r = requests.get(
    "https://raw.githubusercontent.com/jeffheaton/"
    + "t81_558_deep_learning/master/person.json"
)
print(r.json())


json_string = '{"first":"jeff", "last":"Heaton"}'

obj = json.loads(json_string)
print(f"First Name: {obj['first']}")
