from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX


class IfindBySerialNumber(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("findBySerialNumber")


class Company(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)
    def findBySerialNumber(self):
        return IfindBySerialNumber(self)


doc_type = "company"
factory = Company(doc_type)
def test_list():
    ilist = factory.list()
    ilist.payload = {}
    ilist().print()

def test_findBySerialNumber(serialnumber=None):
    ilist = factory.findBySerialNumber()
    ilist.payload = {"serialNumber":serialnumber}
    ilist().print()

# test_list()
# test_findBySerialNumber('913205097933133056') #有user
test_findBySerialNumber('91320509685896857D') #无user
# test_findBySerialNumber('91320509558055713D') #无user
# test_findBySerialNumber() #无user


