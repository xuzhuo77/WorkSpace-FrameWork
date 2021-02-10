from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX
from faker import Faker


class IspecialCheckDetailListCreate(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("specialCheckDetailListCreate")


class IspecialCheckDetailListLogicalDelete(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("specialCheckDetailListLogicalDelete")


class IspecialCheckDetailListGet(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("specialCheckDetailListGet")


class ItroubleList(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("troubleList")


class ItroubleStats(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("troubleStats")


class SpecialCheck(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)

    def specialCheckDetailListCreate(self):
        return IspecialCheckDetailListCreate(self)

    def specialCheckDetailListLogicalDelete(self):
        return IspecialCheckDetailListLogicalDelete(self)

    def specialCheckDetailListGet(self):
        return IspecialCheckDetailListGet(self)

    def troubleList(self):
        return ItroubleList(self)

    def troubleStats(self):
        return ItroubleStats(self)


doc_type = "specialCheck"
factory = SpecialCheck(doc_type)


def test_list():
    ilist = factory.list()
    ilist.payload = {
        # "checkYear":2018,
        # "status":1,
        "checkResult":2
    }
    ilist().print()


def test_specialCheckDetailList_Create():
    specialCheckDetailListCreate = factory.specialCheckDetailListCreate()
    fake = factory.fake
    specialCheckDetailListCreate.payload = {
        "specialCheckParam": {"planName": fake.company()},
        "specialCheckItemRectifyReviewParams": [
            {"specialCheckItemParam": {"item": fake.job()},
             "specialCheckRectifyParam": {"rectifyUser": fake.company()},
             "specialCheckReviewParam": {"reviewUser": fake.name()}
             },
            {"specialCheckItemParam": {"item": fake.job()},
             "specialCheckRectifyParam": {"rectifyUser": fake.name()},
             "specialCheckReviewParam": {"reviewUser": fake.name()}
             },
        ]
    }
    specialCheckDetailListCreate()


def test_specialCheckDetailList_Save(payload):
    specialCheckDetailListSave = factory.specialCheckDetailListCreate()
    payload = payload.pure()
    payload = {"specialCheckParam": payload["specialCheckVO"],
               "specialCheckItemRectifyReviewParams":
                   [{"specialCheckItemParam": t["specialCheckItemVO"],
                     "specialCheckRectifyParam": t["specialCheckRectifyVO"],
                     "specialCheckReviewParam": t["specialCheckReviewVO"]
                     }
                    for t in payload["specialCheckItemRectifyReviewVO"]]
               }
    payload["specialCheckParam"]["planName"] = "123312"
    payload["specialCheckItemRectifyReviewParams"][0]["specialCheckItemParam"]["item"] = "花边新闻"

    specialCheckDetailListSave.payload = payload
    specialCheckDetailListSave()


def test_specialPlanDetailList_Delete():
    specialCheckDetailListLogicalDelete = factory.specialCheckDetailListLogicalDelete()
    specialCheckDetailListLogicalDelete(1293026440467464193)


def test_specialPlanDetailList_Get():
    specialCheckDetailListGet = factory.specialCheckDetailListGet()
    data = specialCheckDetailListGet(1293093510459830274)
    data.print()
    return data


def test_trouble_list():
    troubleList = factory.troubleList()
    troubleList.payload = {
        # "checkItem": "1",
        # "companyName":"2"

    }
    troubleList().print()


def test_troubleStats():
    troubleStats = factory.troubleStats()
    troubleStats.payload = {"year": 2020, "pageIndex": 1, "pageSize": 20, "countTotal": True,
                            "companyId": 1299317754598854657}
    troubleStats().print()


if __name__ == '__main__':
    # test_specialCheckDetailList_Create()

    # test_specialPlanDetailList_Delete()
    # data=test_specialPlanDetailList_Get()
    # data=test_specialPlanDetailList_Get()
    # test_specialCheckDetailList_Save(data)
    # data=test_specialPlanDetailList_Get()

    # factory.logicalDelete_all()

    test_list()
    # test_trouble_list()

    # test_troubleStats()
    pass
