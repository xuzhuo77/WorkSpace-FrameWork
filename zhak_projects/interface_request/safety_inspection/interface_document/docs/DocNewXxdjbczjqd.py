from zhak_projects.interface_request.safety_inspection.interface_document.interfacefactory import \
    InterfaceRequestFactory

doc_type = "docNewXxdjbczjqd"
factory = InterfaceRequestFactory(doc_type)
guid = 'f9e25bc0-d603-4f15-973a-775d3dfc26dc'
checkLogGuid = "DC70E9EB-F158-3DAB-04AF-18400A9533B2"
# ilist=factory.list()
# ilist.payload={}
# ilist().print()


icreatedoc = factory.createDoc()
icreatedoc.payload = {"wsGuid": guid,
                      # "checkLogGuid": checkLogGuid,
                      }
#
# icreatedoc().print()

isavedoc = factory.saveDoc()
payload=icreatedoc().pure()
# payload["checkLogGuid"]=checkLogGuid
payload["caseGuid"]='c66379d7-d311-469d-a5a4-b4721cd73948'
isavedoc.payload =payload
#
isavedoc().print()

ipdfExport = factory.pdfExport(guid)
ipdfExport()
# ipdfExport.open_pdf()


