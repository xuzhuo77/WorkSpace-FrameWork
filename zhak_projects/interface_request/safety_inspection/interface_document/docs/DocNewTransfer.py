from zhak_projects.interface_request.safety_inspection.interface_document.interfacefactory import \
    InterfaceRequestFactory

doc_type = "docNewTransfer"
factory = InterfaceRequestFactory(doc_type)
guid = '88806599BB79FDEAE050007F01001FC9'
checkLogGuid = "41e74a3e-dcf3-4f4f-97b9-5c3d8b08e699"
ilist=factory.list()
# ilist.payload={}
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
ipdfExport.open_pdf()


