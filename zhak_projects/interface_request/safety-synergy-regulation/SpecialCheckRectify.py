from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory


class SpecialCheckRectify(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)



doc_type = "specialCheckRectify"
factory = SpecialCheckRectify(doc_type)


def test_list():
    ilist = factory.list()
    ilist.payload = {}
    ilist().print()

def test_IlogicalDelete():
    logicalDelete = factory.logicalDelete()
    logicalDelete(1292741051102027778)

def test_IlogicalDelete_ids():
    logicalDelete_ids = factory.logicalDelete_ids()
    logicalDelete_ids.payload=[1292752596448075777]
    logicalDelete_ids()


# test_list()
# test_IlogicalDelete_ids()
# factory.logicalDelete_all()
test_list()
