from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory


class RiskSafetyCard(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)


doc_type = "riskSafetyCard"
factory = RiskSafetyCard(doc_type)
def test_list():
    ilist = factory.list()
    ilist.payload = {}
    ilist().print()


test_list()
id=1115933512676999170
ipdfExport = factory.pdfExport_id(id)
ipdfExport()
ipdfExport.open_pdf()