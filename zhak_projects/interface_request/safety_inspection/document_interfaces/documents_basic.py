
class Interfaces():

    def __init__(self):
        self.list = "list"
        self.export_pdf = "pdfExport"
        self.pdf_type = 0
    def set_export_pdf(self,name):
        self.export_pdf=name

class ClassDocumentBasic():
    def __init__(self,wsmc,model_name,module_name):
        self.wsmc =wsmc
        self.model_name =model_name
        self.module_name =module_name
        self.interfaces=Interfaces()
    @property
    def controller_name(self):
        return self.model_name[0].lower()+self.model_name[1:]





