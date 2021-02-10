from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX


class ILessorRegist(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("lessorRegist")

class FactoryBuildingLessor(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)
    def lessorRegist(self):
        return  ILessorRegist(self)

doc_type = "factoryBuildingLessor"
factory = FactoryBuildingLessor(doc_type)
def test_list():
    ilist = factory.list()
    # ilist.payload = {"regionId":"320509100010"}
    ilist().print()

def test_lessorRegist():
    ilist = factory.lessorRegist()
    ilist.payload = {
    "userId":77,
     "userVersion":4444,
"companyName":"公司名称",
        "serialNumber":1112222211111,
        "username":1233333,
        "password":3123,
        # "guid": "String",
        "economicType": "String",
        "industry": "String",
        "industryIds": "String",
        "regionName": "String",
        "regionIds": "String",
        "registerAddress": "String",
        "safetyManager": "String",
        "safetyManagerPhone": "String",
        "scaleType": 0,

        "bureausIndustry": "String",
        "bureausIndustryId": "String",
        "superviseBureaus": "String",
        "superviseBureausIds": "String",
        "affiliation": "String",
        "longitude": 0,
        "latitude": 0,
        "legalRepresentative": "String",
        "legalRepresentativePhone": "String",
        "corporateDuty": "String",
        "employeeCount": 0,
        "constructionArea": 0,
        "superiorCompanyGuid": "String",
        "businessStatus": "String",
        "companyStatus": 0,
        "isCreateAccount": 0,
        "isLuShangShiYou": True,
        "version": 0,
        "pbAddress": "String",
        "gridGuid": "String",
        "type": "String",
        "companyId": 0,
        "adminUserId": 0,
        "adminUsername": "String",
        "adminName": "String",
        "regionId": 0,
        "socialCreditCode": "String",
        "legalPerson": "String",
        "address": "String",
        "economyType": "String",
        "industryCategory": "String",
        "safetyResponsiblePerson": "String",
        "safetyResponsibleMobile": "String",
        "provinceId": 0,
        "provinceName": "String",
        "cityId": 0,
        "cityName": "String",
        "countyId": 0,
        "countyName": "String",
        "townshipId": 0,
        "townshipName": "String",
        "publishState": 0

    }
    ilist().print()






test_list()
# test_lessorRegist()


import emoji
print(emoji.emojize('Python is :cold_sweat:', use_aliases=True))
