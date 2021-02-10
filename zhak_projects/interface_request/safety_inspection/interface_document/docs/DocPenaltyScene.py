import requests
import json
from zhak_projects.interface_request import environment
from zhak_projects.interface_request.safety_inspection.interface_document.interfacefactory import \
    InterfaceRequestFactory

doc_type="docPenaltyScene"




factory = InterfaceRequestFactory(doc_type)
guid = '2b5eecfd-b4e9-4bb5-bf6c-1d7e69461ad2'
checkLogGuid = "6BFB82A5-96F4-55CF-F8BE-560B095FC688"
ilist=factory.list()
# ilist.payload={}
ilist().print()

# igetdoclist = factory.get_doc_list()
# igetdoclist.payload={"wsGuid":guid}
# igetdoclist().print()



# icreatedoc = factory.createDoc()
# icreatedoc.payload = {"wsGuid": guid,
#                       # "checkLogGuid": checkLogGuid,
#                       }
# #
# d=icreatedoc()
# d.print()
#
# isavedoc = factory.saveDoc()
# payload=d.pure()
# payload["personAddress"]='personAddress'
# payload["performanceMethod"]=True
# #
# isavedoc.payload =payload
# isavedoc().print()
#
#
# ipdfExport = factory.pdfExport(guid)
# ipdfExport()
# ipdfExport.open_pdf()