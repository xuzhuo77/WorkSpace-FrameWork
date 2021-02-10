""":arg
    基于案件guid
    1 查看案件详细情况
    2 下载案件全部pdf

"""



import requests
import json
from zhak_projects.interface_request import environment
from zhak_projects.interface_request.safety_inspection import z_temp, accessPdf
from zhak_projects.interface_request.safety_inspection.interface_securityCase import securityCase_findNewCaseStepDetil

url = environment.get_IP_PORT() + "safety/api/securityCase/findNewCaseDetil"
headers = environment.get_headers()
payload = {"guid": z_temp.read_default()["caseGuid"], "type": "web"}
payload = json.dumps(payload)
response = requests.request("POST", url, headers=headers, data=payload)
data = response.text
print(json.dumps(json.loads(data), ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))
data = json.loads(data)["data"]

step_guids = [step["guid"] for step in data["stepList"]]
print(step_guids)


def security_download_pdfs(step_guid):
    data = securityCase_findNewCaseStepDetil.request(step_guid)
    print(data)
    accessPdf.download_securitycase_pdfs(data["data"]["docList"])


for step_guid in step_guids:
    security_download_pdfs(step_guid)

# export_pdfs_by_doc(data)
