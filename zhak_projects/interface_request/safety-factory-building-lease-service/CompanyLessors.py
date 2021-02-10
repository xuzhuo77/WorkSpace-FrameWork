from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory


class CompanyLessors(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)


doc_type = "companyLessors"
factory = CompanyLessors(doc_type)
def test_list():
    ilist = factory.list()
    ilist.payload = {}
    ilist().print()
test_list()



