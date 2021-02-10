import requests
import json
from zhak_projects.interface_request import environment
from zhak_projects.interface_request.safety_inspection import z_temp, accessPdf

url = environment.get_IP_PORT()+"safety/api/doc/listByDoc"
headers=environment.get_headers()
payload = {"checkLogGuid":z_temp.read_default()["checkLogGuid"],"countTotal":True,"order":"desc","pageIndex":1,"pageSize":100,"sort":"id","total":0}
payload=json.dumps(payload)
response = requests.request("POST", url, headers=headers, data = payload)
data=response.text
print(json.dumps(json.loads(data),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))



accessPdf.export_pdfs_by_doc(json.loads(data)["data"])
