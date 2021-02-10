import requests
import json
from zhak_projects.interface_request import environment

def request(guid):
    url = environment.get_IP_PORT()+"safety/api/securityCase/findNewCaseStepDetil?guid="+guid
    headers=environment.get_headers()
    payload = {"guid":guid}
    payload=json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data = payload)
    data=response.text
    # print(json.dumps(json.loads(data),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))
    return json.loads(data)

