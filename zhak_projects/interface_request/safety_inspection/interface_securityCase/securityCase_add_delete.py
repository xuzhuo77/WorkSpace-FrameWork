import requests
import json

from zhak_projects.interface_request import environment
from zhak_projects.interface_request.safety_inspection import s_request
from zhak_projects.interface_request.safety_inspection.interface_exception_print import myprint

doc_type = "docRegistCaseAudit"


def docRegistCaseAudit_get_by_guid(guid):
    url = environment.get_IP_PORT() + "safety/api/" + doc_type + "/getByGuid" + "/" + guid
    payload = {"guid": guid}
    data=s_request.post(payload,url)
    return json.loads(data)


def docRegistCaseAudit_saveCaseByAppro(save_json):
    """:arg
        通过新建立案审批表,给案件添加数据
    """
    url = environment.get_IP_PORT() + "safety/api/" + doc_type + "/saveCaseByAppro"
    payload = save_json
    data=s_request.post(payload,url)
    return json.loads(data)


def securityCase_remove(id):
    url = environment.get_IP_PORT() + "safety/api/" + "securityCase" + "/removeCaseByIds"
    payload =[id]
    data=s_request.post(payload,url)
    return json.loads(data)


def securityCase_list():
    url = environment.get_IP_PORT() + "safety/api/" + "securityCase" + "/loadCaseBaseList"
    payload = {"allGridGuid": "", "caseName": "", "caseType": 1, "countTotal": True, "endDate": None, "order": "DESC",
               "pageIndex": 1, "pageSize": 15, "sort": "acceptanceDate", "startDate": None, "steps": None, "total": 16}
    data=s_request.post(payload,url)
    return json.loads(data)


def securityCase_get_by_guid(guid):
    url = environment.get_IP_PORT() + "safety/api/" + "securityCase" + "/getByGuid" + "/" + guid
    payload = {"guid": guid}
    data=s_request.post(payload,url)
    return json.loads(data)


def doc_getDocList(ws_guid):
    url = environment.get_IP_PORT() + "safety/api/" + "doc" + "/list"
    payload = {"wsGuid": ws_guid}
    data=s_request.post(payload,url)
    return json.loads(data)


# myprint(createSecurityCase())
i=3
ceshi_guid="9d79b5e8-100b-9b28-0ada-ceshiGuid"+str(i)
save_json = {"address": "", "allCaseReason": [], "caseDate": "2020-06-30 08:00:00", "caseName": "",
             "caseOrigin": "执法检查",
             "caseReason": "", "caseSituation": "", "caseType": 1, "discussPersonnel": "zhadmin",
             "discussPersonnel1": "zhadmin",
             "discussPersonnelNNN": "", "documentDate": "2020-06-30 08:00:00", "documentNum": "(辽)应急立〔2020〕002号",
             "documentSerialNum": 1, "documentType": "", "enforcementNum": ",undefined",
             "guid": ceshi_guid, "inspectionDate": "2020-06-30 08:00:00", "legalPerson": "",
             "litigant": "", "litigantPhone": "", "marshalsTried": "zhadmin,zhadmin",
             "marshalsTriedGuid": ",1E9CE4E75E0B7DD6E05010AC32DE22B1,1E9CE4E75E0B7DD6E05010AC32DE22B1,",
             "persionGuid": "1E9CE4E75E0B7DD6E05010AC32DE22B1", "persionGuid1": "1E9CE4E75E0B7DD6E05010AC32DE22B1",
             "postalCode": "", "undertakerOpinion": ""}


def docNewServiceReceipt_createDoc(case_guid):
    url = environment.get_IP_PORT() + "safety/api/" + "docNewServiceReceipt" + "/createDoc"
    payload = {"caseGuid": case_guid, "caseNode": 6}
    data=s_request.post(payload,url)
    return json.loads(data)

def docNewServiceReceipt_saveDoc(case_guid):
    url = environment.get_IP_PORT() + "safety/api/" + "docNewServiceReceipt" + "/saveDoc"
    payload = {"caseGuid": "9bea3ad9-01f8-4bfa-be09-afdbfe4f4284", "caseName": "123", "caseNode": 6,
               "departmentNum": "",
               "docDate": "2020-06-30 18:02:38", "docNewServiceInfoList": [], "docNumber": "(辽)应急回〔2020〕001号",
               "docSimpleName": "辽", "docType": "应急回", "guid": "8f72e52f-1d71-4613-9422-3b261e5dd58d",
               "isManualInputNum": False,
               "serviceUnit": "测试企业银行", "wsGuid": ""}
    data=s_request.post(payload,url)
    return json.loads(data)



def securityCase_removed_by_docRegistCaseAudit_guid(ceshi_guid):
    doc = doc_getDocList(ceshi_guid)
    myprint(doc)
    case_guid=doc["data"]["items"][0]["caseGuid"]
    securityCase=securityCase_get_by_guid(case_guid)
    myprint(securityCase)
    id=securityCase["data"]["id"]
    myprint(securityCase_remove(id))


# myprint(docRegistCaseAudit_saveCaseByAppro(save_json))
securityCase_removed_by_docRegistCaseAudit_guid(ceshi_guid)