from zhak_projects.interface_request.safety_inspection.interface_document.interfacefactory import \
    InterfaceRequestFactory

doc_type = "docNewjaspb"
factory = InterfaceRequestFactory(doc_type)
guid = 'bb807215-50f5-49ab-9f45-edd3e2f3bdc6'
checkLogGuid = "DC70E9EB-F158-3DAB-04AF-18400A9533B2"
ilist=factory.list()
ilist.payload={}
ilist().print()

# icreatedoc = factory.createDoc()
# icreatedoc.payload = {"guid": guid,
#                       "checkLogGuid": checkLogGuid,
#                       }

# guid = "sdafdfsa2ssa333f"
# isavedoc = factory.saveDoc()
# payload=icreatedoc().pure()
# payload["checkLogGuid"]=checkLogGuid
# isavedoc.payload =payload
#
# isavedoc().print()


ipdfExport = factory.pdfExport(guid)
ipdfExport()
ipdfExport.open_pdf()