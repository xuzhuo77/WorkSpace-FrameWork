from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory


class SpecialCheckItem(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)



doc_type = "specialCheckItem"
factory = SpecialCheckItem(doc_type)

def test_list():
    ilist = factory.list()
    ilist.payload = {}
    ilist().print()

test_list()