from zhak_projects.interface_request.safety_inspection.interface_document.interfacefactory import \
    InterfaceRequestFactory

doc_type = "docLocalDeal"
factory = InterfaceRequestFactory(doc_type)
guid = 'BB7D1660-D0AC-3807-62B4-4BC11EB8B6BF'
# checkLogGuid = "41e74a3e-dcf3-4f4f-97b9-5c3d8b08e699"
# ilist=factory.list()
# # ilist.payload={}
# ilist().print()

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
ipdfExport.pdf_export_interface="/pdfLocalDealExport"
ipdfExport()
# ipdfExport.open_pdf()


