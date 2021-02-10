import requests
import json
import sys



from zhak_projects.interface_request import environment

module_name="docNewCheckPlan"
pageSize=2
guid="33c1b85d-99b0-4e02-a849-8a32b053aa17"
def exportPdf(module_name,guid,pdf_export,pdf_type):
    url = environment.get_IP_PORT()+"safety/api/"+module_name+"/"+pdf_export+"?guid="+guid+"&type={}".format(pdf_type) if pdf_type is not None else ""
    headers=environment.get_headers()
    payload=json.dumps({})
    response = requests.request("POST", url, headers=headers,data=payload)
    return json.loads(response.content)
    # print(json.dumps(json.loads(data),ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))


def list(module_name):
    url = environment.get_IP_PORT()+"safety/api/"+module_name+"/list"
    headers=environment.get_headers()
    payload=json.dumps({"pageSize":pageSize})
    response = requests.request("POST", url, headers=headers, data = payload)
    return json.loads(response.content)

# content=list()
# print(json.dumps(content, ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))
# exportPdf(guid)

if __name__ == '__main__':
    # list(module_name)
    print(exportPdf(module_name,guid,0))
