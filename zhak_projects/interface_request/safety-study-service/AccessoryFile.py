from zhak_projects.interface_request.interfacefactory import InterfaceRequestFactory, InterfaceX


class IgenerateQRCodeFile(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("generateQRCodeFile")


class AccessoryFile(InterfaceRequestFactory):
    def __init__(self, doc_type):
        InterfaceRequestFactory.__init__(self, doc_type)

    def generateQRCodeFile(self):
        return IgenerateQRCodeFile(self)


doc_type = "accessoryFile"
factory = AccessoryFile(doc_type)


def test_list():
    ilist = factory.list()
    ilist.payload = {}
    ilist().print()


def test_generateQRCodeFile():
    ilist = factory.generateQRCodeFile()
    ilist.payload = {"implantUrl": 1231231,
                     "parentguid": "321-556",
                     "recordName":"recordName--2223",
                     "module":"TrainSignInLog"
                     }
    ilist().print()


# test_list()
test_generateQRCodeFile()
