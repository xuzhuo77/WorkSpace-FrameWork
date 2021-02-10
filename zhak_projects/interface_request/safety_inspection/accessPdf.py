import requests
import json
import os

from zhak_projects.interface_request.safety_inspection import z_temp
from zhak_projects.interface_request.safety_inspection.doc_wsmc_wszl_modulename import get_module_name_by_wszl
from zhak_projects.interface_request import environment

PDF_FILE_PATH = 'E:\pythonWebWorkSpace\zhak_projects\interface_request\safety_inspection\pdfs'


def get_pdf(moduleName,parentGuid, name, check_log_guid,module_name):
    url = environment.get_IP_PORT() + "safety/api/accessoryFile/getAccessoryFileId"
    headers = environment.get_headers()
    payload = {"moduleName": moduleName, "parentGuid": parentGuid}

    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.text
    print(json.dumps(json.loads(data), ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))

    url = environment.get_IP_PORT() + "safety/api/accessoryFile/download/" + json.loads(data)["data"]
    headers = environment.get_headers()
    data = requests.get(url, headers=headers)
    pdf_path = PDF_FILE_PATH + os.sep + module_name+"_"+check_log_guid
    if not os.path.exists(pdf_path):
        os.makedirs(pdf_path)
    pdf_path += os.sep + name + ".pdf"
    with open(pdf_path, "wb") as code:
        code.write(data.content)
    # print(json.dumps(json.loads(data),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))



def export_pdfs_by_doc(data):
    for doc in data:
        # print(doc)
        get_pdf(get_module_name_by_wszl(doc["wszl"]),doc["wsGuid"],doc["wsmc"],z_temp.read_default()["checkLogGuid"],"checklog")


def get_pdf_security(moduleName,parentGuid, name, check_log_guid,module_name):
    url = environment.get_IP_PORT() + "safety/api/accessoryFile/getAccessoryFileId"
    headers = environment.get_headers()
    payload = {"moduleName": moduleName, "parentGuid": parentGuid}

    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.text
    print(json.dumps(json.loads(data), ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))

    url = environment.get_IP_PORT() + "safety/api/accessoryFile/download/" + json.loads(data)["data"]
    headers = environment.get_headers()
    data = requests.get(url, headers=headers)
    pdf_path = PDF_FILE_PATH + os.sep +module_name +"_"+check_log_guid
    if not os.path.exists(pdf_path):
        os.makedirs(pdf_path)
    pdf_path += os.sep + name + ".pdf"
    with open(pdf_path, "wb") as code:
        code.write(data.content)
    # print(json.dumps(json.loads(data),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))


def download_securitycase_pdfs(data):
    for doc in data:
        # print(doc)
        get_pdf_security(get_module_name_by_wszl(doc["wszl"]),doc["wsGuid"],doc["wsmc"],z_temp.read_default()["caseGuid"],"securitycase")