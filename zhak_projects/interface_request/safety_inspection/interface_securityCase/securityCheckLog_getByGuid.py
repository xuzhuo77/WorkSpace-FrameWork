import requests
import json
import sys



from zhak_projects.interface_request import environment

url = environment.get_IP_PORT()+"safety/api/securityCheckLog/getByGuid/00F10D08-13F4-5018-15D6-C223255BF366"
headers=environment.get_headers()
payload = "{}"
response = requests.request("POST", url, headers=headers, data = payload)
data=response.text
print(json.dumps(json.loads(data),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))


