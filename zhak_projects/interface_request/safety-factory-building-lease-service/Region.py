from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX


class IloadRegionTree(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("loadRegionTree")


class Region(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)
    def loadRegionTree(self):
        return IloadRegionTree(self)


doc_type = "region"
factory = Region(doc_type)
def test_list():
    ilist = factory.list()
    ilist.payload = {}
    ilist().print()

def test_loadRegionTree(parentId=None):
    ilist = factory.loadRegionTree()
    if parentId:
        ilist.payload = {"parentId":parentId}
    ilist().print()


test_loadRegionTree(320509000000) #无user
# test_loadRegionTree() #无user



