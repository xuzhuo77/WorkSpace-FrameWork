import requests
import json
from zhak_projects.interface_request import environment



doc_type="docPenalty"
def list():
    url = environment.get_IP_PORT()+"safety/api/"+doc_type+"/list"
    headers=environment.get_headers()
    payload = {}
    payload=json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data = payload)
    data=response.text
    # print(json.dumps(json.loads(data),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))
    return json.loads(data)

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
    url = environment.get_IP_PORT()+"safety/api/"+doc_type+"/pdfExport"+"?guid="+guid+"&type={}".format(doc_type) if doc_type is not None else ""
    headers=environment.get_headers()
    payload = {"guid":guid}
    payload=json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data = payload)
    data=response.text
    # print(json.dumps(json.loads(data),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))
    return json.loads(data)


guid='52c13791-867d-4642-9682-e7f35e69d57b'
print(pdfExport(guid))
import os
r_v = os.system("C:\\TEMP\\storage\\pdf\\"+guid+".pdf")
# print(list())