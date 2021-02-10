from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX



class RiskControlMeasures(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)



doc_type = "riskControlMeasures"
# doc_type = "specialCheckItem"
factory = RiskControlMeasures(doc_type)



def test_list():
    list = factory.list()

    list().print()
# test_troubleStats()

test_list()
