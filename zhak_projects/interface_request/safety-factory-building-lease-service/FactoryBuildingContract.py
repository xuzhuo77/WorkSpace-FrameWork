from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX


class ItemporarySave(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("temporarySave")


class IgetTemporary(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("getTemporary")


class IrecordContract(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("recordContract")


class Isurrender(InterfaceX):
    def __init__(self, parent,id):
        InterfaceX.__init__(self, parent)
        self.init("surrender",id)


class Iview(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("view")


class IlesseeContractVoList(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("lesseeContractVoList")
class IsaveAudit(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("saveAudit")

class FactoryBuildingContract(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)

    def temporarySave(self):
        return ItemporarySave(self)

    def getTemporary(self):
        return IgetTemporary(self)

    def recordContract(self):
        return IrecordContract(self)

    def surrender(self,id):
        return Isurrender(self,id)

    def view(self):
        return Iview(self)
    def lesseeContractVoList(self):
        return IlesseeContractVoList(self)
    def saveAudit(self):
        return IsaveAudit(self)
doc_type = "factoryBuildingContract"
factory = FactoryBuildingContract(doc_type)


def test_list():
    ilist = factory.list()
    ilist.payload = {}
    ilist().print()


def test_temporarySave():
    ilist = factory.temporarySave()
    ilist.payload = {"factoryBuildingContract":
        {

        }
    }
    ilist().print()


def test_getTemporary():
    ilist = factory.getTemporary()
    ilist.payload = {}
    ilist().print()


def test_recordContract_submit():
    ilist = factory.recordContract()
    ilist.payload = {}
    ilist().print()


def test_recordContract_notSubmmit():
    ilist = factory.recordContract()
    ilist.payload = {}
    ilist().print()


def test_surrender(id):
    ilist = factory.surrender(id)
    # ilist.payload = {}
    ilist().print()


def test_view(id):
    ilist = factory.view()
    ilist(id).print()


def test_getId(id):
    factory.get()(id).print()
def test_lesseeContractVoList():
    ilist = factory.lesseeContractVoList()
    ilist.payload = {"pageSize":2,
                     "lesseeCompanyName":"合"
                     }
    ilist().print()
def test_saveAudit():
    ilist = factory.saveAudit()
    ilist.payload = {"state":2,
                     "leaseArea":20}
    ilist().print()
#
test_list()
# test_temporarySave()
# test_getTemporary()
test_surrender(1316576699735150593)
# test_view(1308965248036032513)

# test_getId(1308965248036032513)


# test_recordContract_notSubmmit()

# test_lesseeContractVoList()
# test_saveAudit()