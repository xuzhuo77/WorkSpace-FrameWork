from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX


class IavailableArea(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("availableArea")


class FactoryBuilding(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)

    def availableArea(self):
        return IavailableArea(self)


doc_type = "factoryBuilding"
factory = FactoryBuilding(doc_type)


def test_list():
    ilist = factory.list()
    ilist.payload = {"parentIdIsNull":True}
    ilist().print()


def test_availableArea():
    ilist = factory.availableArea()
    # ilist.payload = {"ownerCompanyId":1306413711746113537}
    ilist().print()


test_availableArea()
# test_list()