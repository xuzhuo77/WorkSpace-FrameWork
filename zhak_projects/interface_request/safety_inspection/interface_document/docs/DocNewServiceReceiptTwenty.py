import requests
import json
from zhak_projects.interface_request import environment



doc_type="docNewServiceReceiptTwenty"
def createDoc(guid):
    url = environment.get_IP_PORT()+"safety/api/"+doc_type+"/createDoc"
    headers=environment.get_headers()
    payload = {"guid":guid}
    payload=json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data = payload)
    data=response.text
    # print(json.dumps(json.loads(data),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))
    return json.loads(data)

def saveDoc(guid):
    url = environment.get_IP_PORT()+"safety/api/"+doc_type+"/saveDoc"
    headers=environment.get_headers()
    payload = {"guid":guid}
    payload=json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data = payload)
    data=response.text
    # print(json.dumps(json.loads(data),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))
    return json.loads(data)

def pdfExport(guid):
    url = environment.get_IP_PORT()+"safety/api/"+doc_type+"/pdfExport"
    headers=environment.get_headers()
    payload = {"guid":guid}
    payload=json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data = payload)
    data=response.text
    # print(json.dumps(json.loads(data),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))
    return json.loads(data)


