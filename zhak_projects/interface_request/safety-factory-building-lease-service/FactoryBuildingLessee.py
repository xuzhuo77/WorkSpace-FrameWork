from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory


class FactoryBuildingLessee(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)


doc_type = "factoryBuildingLessee"
factory = FactoryBuildingLessee(doc_type)
def test_list():
    ilist = factory.list()
    ilist.payload = {}
    ilist().print()


test_list()