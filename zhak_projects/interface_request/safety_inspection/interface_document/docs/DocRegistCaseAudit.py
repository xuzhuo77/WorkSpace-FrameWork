from zhak_projects.interface_request.safety_inspection.interface_document.interfacefactory import \
    InterfaceRequestFactory

doc_type = "docRegistCaseAudit"
factory = InterfaceRequestFactory(doc_type)
guid = '2f859c52-2771-4da4-9e59-7d84b34ac0a3'
# checkLogGuid = "41e74a3e-dcf3-4f4f-97b9-5c3d8b08e699"
ilist=factory.list()
ilist.payload={"pageSize":20}
ilist().print()

# igetdoclist = factory.get_doc_list()
# igetdoclist.payload={"wsGuid":guid}
# igetdoclist().print()


# icreatedoc = factory.createDoc()
# icreatedoc.payload = {"guid": guid,
#                       "checkLogGuid": checkLogGuid,
#                       }
#
# icreatedoc().print()
# isavedoc = factory.saveDoc()
# payload=icreatedoc().pure()
# payload["partyMember"]='true'
# isavedoc.payload =payload
# isavedoc().print()


ipdfExport = factory.pdfExport(guid)
ipdfExport()
# ipdfExport.open_pdf()


