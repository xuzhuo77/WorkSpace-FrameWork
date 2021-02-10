import requests
import json
import sys



from zhak_projects.interface_request import environment

url = "http://localhost:9030/safety/api/suppliesWarehouse/statisticsBenchmark"
headers=environment.get_headers()
payload = "{\n\n    \"regionId\"    :210203000000\n\n          \n}"
response = requests.request("POST", url, headers=headers, data = payload)
data=response.text.encode('utf-8')
print("{}".format(json.loads(data)))
print(json.dumps(json.loads(data), sort_keys=True, indent=4, separators=(', ', ': ')))


