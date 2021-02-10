import requests
import json
from zhak_projects.interface_request import environment

import time

doc_type="docNewCfkyjds"
def list():
    url = environment.get_IP_PORT()+"safety/api/"+doc_type+"/list"
    headers=environment.get_headers()
    payload = {}
    payload=json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data = payload)
    data=response.text
    # print(json.dumps(json.loads(data),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))
    return json.loads(data)

def createDoc(guid,checkLogGuid=""):
    url = environment.get_IP_PORT()+"safety/api/"+doc_type+"/createDoc"
    headers=environment.get_headers()
    payload = {"guid":guid,
               "checkLogGuid":checkLogGuid}
    payload=json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data = payload)
    data=response.text
    # print(json.dumps(json.loads(data),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))
    return json.loads(data)

def saveDoc(guid,checkLogGuid=""):
    url = environment.get_IP_PORT()+"safety/api/"+doc_type+"/saveDoc"
    headers=environment.get_headers()
    payload = {"guid":guid,
               "checkLogGuid": checkLogGuid,
               "docDate":time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
               }
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

guid='0322ea50-5d73-4da7-8ef0-7c7c8461e62d'
# print(list())
checkLogGuid="DC70E9EB-F158-3DAB-04AF-18400A9533B2"
# print(createDoc("",checkLogGuid))
# print(saveDoc("22323gfdgfd",checkLogGuid))
# guid="22323gfdgfd"
# #
print(pdfExport(guid))
import os
r_v = os.system("C:\\TEMP\\storage\\pdf\\"+guid+".pdf")