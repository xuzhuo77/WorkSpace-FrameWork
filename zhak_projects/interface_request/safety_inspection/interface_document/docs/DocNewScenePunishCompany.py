from zhak_projects.interface_request.safety_inspection.interface_document.interfacefactory import \
    InterfaceRequestFactory

doc_type = "docNewScenePunishCompany"
factory = InterfaceRequestFactory(doc_type)
guid = 'fff34a56-63cf-4b31-ab6d-d112bb402a5a'
checkLogGuid = "DC70E9EB-F158-3DAB-04AF-18400A9533B2"
# ilist=factory.list()
# ilist.payload={}
# ilist().print()

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