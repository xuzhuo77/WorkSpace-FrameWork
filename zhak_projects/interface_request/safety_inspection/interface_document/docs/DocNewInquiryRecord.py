from zhak_projects.interface_request.safety_inspection.interface_document.interfacefactory import \
    InterfaceRequestFactory

doc_type = "docNewInquiryRecord"
factory = InterfaceRequestFactory(doc_type)
guid = '2c5e8903-82f4-4ad6-9736-3fd1c8a1dabc'
checkLogGuid = "2dd9a725-8bc1-4a50-83a5-bd6b754855e2"
# ilist=factory.list()
# # ilist.payload={}
# ilist().print()

# igetdoclist = factory.get_doc_list()
# igetdoclist.payload={"wsGuid":guid}
# igetdoclist().print()



icreatedoc = factory.createDoc()
icreatedoc.payload = {"wsGuid": guid,
                      "checkLogGuid": checkLogGuid,
                      }
#
d=icreatedoc()
d.print()

isavedoc = factory.saveDoc()
payload=d.pure()
payload["partyMember"]='否'
payload["sex"]='222'
payload["age"]='fasdf1'

isavedoc.payload =payload
isavedoc().print()


ipdfExport = factory.pdfExport(guid)
ipdfExport()
ipdfExport.open_pdf()


