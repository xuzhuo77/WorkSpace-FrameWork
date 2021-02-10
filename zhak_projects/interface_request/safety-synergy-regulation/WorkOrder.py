from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX


class IworkOrderAndTargetsSave(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("workOrderAndTargetsSave")

class IworkOrderAndTargetsList(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("workOrderAndTargetsList")


class IworkOrderVolist(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("workOrderVolist")

class WorkOrder(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)
    def workOrderAndTargetsSave(self):
        return IworkOrderAndTargetsSave(self)

    def workOrderAndTargetsList(self):
        return IworkOrderAndTargetsList(self)

    def workOrderVolist(self):
        return IworkOrderVolist(self)

doc_type = "workOrder"
# doc_type = "specialCheckItem"
factory = WorkOrder(doc_type)

def test_workOrderAndTargetsList():
    list = factory.workOrderAndTargetsList()
    list.payload = {
        # "checkItem": "1",
        # "companyName":"2"
        # "level":1
        # "targetId": 1111111111
        # "urgeState" :0

    }
    list().print()

def test_workOrderAndTargetsSave():
    list = factory.workOrderAndTargetsSave()
    list.payload = {
        "name":"测试名字",
        "orderNum":"1",
        "targetIds":[320800000000,1291650072160505857],
        "target":"1111111111n,222222222222n",
        "orderContent":"3213",
        "publishState":1
        }
    list().print()

def test_workOrderAndTargetsSave_rough_draft():
    list = factory.workOrderAndTargetsSave()
    list.payload = {
        "name":"测试名字",
        "orderNum":"测试名字",
        "targetIds":[320800000000,1291650072160505857],
        "target":"1111111111n,222222222222n",
        "orderContent":"3213",
        "publishState":0
        }
    list().print()

def test_workOrderVolist():
    list = factory.workOrderVolist()
    list.payload = {
        # "checkItem": "1",
        # "companyName":"2"
        # "level":1
        # "targetId": 1111111111

    }
    list().print()



test_workOrderAndTargetsList()
# test_workOrderAndTargetsSave()
# test_workOrderAndTargetsSave_rough_draft()
# test_workOrderVolist()


