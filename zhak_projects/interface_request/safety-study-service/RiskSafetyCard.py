from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX


class IexportPdf(InterfaceX):
    def __init__(self, parent,id):
        InterfaceX.__init__(self, parent)
        self.init("exportPdf",id)

class RiskSafetyCard(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)
    def exportPdf(self,id):
        return IexportPdf(self,id)

doc_type = "riskSafetyCard"
factory = RiskSafetyCard(doc_type)
def test_list():
    ilist = factory.list()
    ilist.payload = {}
    ilist().print()


test_list()

def test_exportPdf():
    ilist = factory.exportPdf(1115933512676999170)
    # ilist.payload = {"id":1316708885478899713}
    ilist().print()

# test_list()
test_exportPdf()