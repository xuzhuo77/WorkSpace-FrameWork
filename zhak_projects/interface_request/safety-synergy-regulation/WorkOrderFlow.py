from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX


class ItroubleStats(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("troubleStats")
class WorkOrderFlow(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)



doc_type = "workOrderFlow"
# doc_type = "specialCheckItem"
factory = WorkOrderFlow(doc_type)

def test_list():
    list = factory.list()
    list.payload = {
        # "checkItem": "1",
        # "companyName":"2"
        "level":1
                           }
    list().print()
test_list()