from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX


class ItroubleStats(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("troubleStats")
class SpecialCheckItem(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)

    def troubleStats(self):
        return ItroubleStats(self)

doc_type = "specialCheck"
# doc_type = "specialCheckItem"
factory = SpecialCheckItem(doc_type)

def test_troubleStats():
    troubleList = factory.troubleStats()
    troubleList.payload = {
        # "checkItem": "1",
        # "companyName":"2"
        "level":1
                           }
    troubleList().print()
test_troubleStats()