from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX


class IgroupByDepartment(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("groupByDepartment")



class WorkOrder(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)
    def groupByDepartment(self):
        return IgroupByDepartment(self)



doc_type = "workOrderStatistics"
factory = WorkOrder(doc_type)

def test_groupByDepartment():
    list = factory.groupByDepartment()
    list.payload = {
        # "checkItem": "1",
        # "companyName":"2"
        # "level":1
        # "targetId": 1111111111
        "urgeState" :0

    }
    list().print()


# test_groupByDepartment()


