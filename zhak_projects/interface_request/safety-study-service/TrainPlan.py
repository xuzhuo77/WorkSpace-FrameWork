from zhak_projects.interface_request.interfacefactory import InterfaceX, InterfaceRequestFactory


class IqrCodeExport(InterfaceX):
    def __init__(self, parent,id):
        InterfaceX.__init__(self, parent)
        self.init("qrCodeExport",id)

class TrainPlan(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)

    def qrCodeExport(self,id):
        return IqrCodeExport(self,id)
doc_type = "trainPlan"
factory = TrainPlan(doc_type)
def test_list():
    ilist = factory.list()
    ilist.payload = {}
    ilist().print()

def test_qrCodeExport():
    ilist = factory.qrCodeExport(1316708885478899713)
    # ilist.payload = {"id":1316708885478899713}
    ilist().print()

# test_list()
test_qrCodeExport()