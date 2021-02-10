from zhak_projects.interface_request.safety_inspection import doc_wsmc_wszl_modulename
from zhak_projects.interface_request.safety_inspection.document_interfaces import documents_controller
from zhak_projects.interface_request.safety_inspection.document_interfaces.documents_models import all_documents_models
from zhak_projects.interface_request.safety_inspection.interface_exception_print import myprint


def interface_test_documents_list():
    """
    测试 文书的 list
    """
    exceptions_module_name = []
    documents_controller.pageSize = 1
    for doc in all_documents_models():
        print(doc.controller_name)
        try:
            content = documents_controller.list(doc.controller_name)
            myprint(content)
        except:
            exceptions_module_name.append(doc.controller_name)
    print("error_documents", exceptions_module_name)


# content = generate_documents_template.list("docRegistCaseAudit")
# print(json.dumps(content, ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))


def interface_test_random_exportPdf():
    exceptions_module_name = []
    exceptions_module_pdfs = []
    type_code = []
    """
    随机抽取个guid
    """
    documents_controller.pageSize = 1
    content = None
    for doc in all_documents_models():
        print(doc.controller_name)
        if doc.controller_name == "doc":
            try:
                content = documents_controller.list("securityCase")
            except:
                exceptions_module_name.append(doc.controller_name)

        else:
            try:
                content = documents_controller.list(doc.controller_name)
            except:
                exceptions_module_name.append(doc.controller_name)
        """
        pdf查找
        """
        if content:
            if content["data"]["items"]:
                guid = content["data"]["items"][0]["guid"]
                try:
                    print(guid)
                    content = documents_controller.exportPdf(doc.controller_name, guid, doc.interfaces.export_pdf,
                                                             doc.interfaces.pdf_type)
                    myprint(content)
                    if content:
                        if content["code"] == 500:
                            type_code.append(doc.controller_name)
                except:
                    exceptions_module_pdfs.append(doc.controller_name)
                    print("\033[1;31m error {} \033[0m".format(doc.controller_name))

            else:
                print("\033[1;36m error {} \033[0m".format("Item Empty"))

    print("error_documents", exceptions_module_name)
    print("error_documents_pdf", exceptions_module_pdfs)
    print("error_documents_pdf", type_code)


interface_test_random_exportPdf()
# interface_test_documents_list()
