import requests
import json
from zhak_projects.interface_request import environment
def post(payload,url):
    headers = environment.get_headers()
    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text
