import requests
import json
import os

from zhak_projects.interface_request import environment
from zhak_projects.interface_request.safety_inspection.interface_exception_print import myprint, DataWarp

class InterfaceX():
    def __init__(self, parent):
        self.parent = parent
        self.payload = {}

    @property
    def pay_load(self):
        return json.dumps(self.payload)
    def make_url(self):
        self.url=""

    def __call__(self, *args, **kwargs):
        self.make_url()
        response = self.request("POST", self.url, headers=self.parent.headers, data=self.pay_load)
        data = response.text
        return DataWarp(data)


class Ilist(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.url = parent.base_url + "safety/api/" + parent.doc_type + "/list"
        self.request = requests.request


class IcreateDoc(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.url = parent.base_url + "safety/api/" + parent.doc_type + "/createDoc"
        self.request = requests.request


class IsaveDoc(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.url = parent.base_url + "safety/api/" + parent.doc_type + "/saveDoc"
        self.request = requests.request

class get_doc_list(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.url = parent.base_url + "safety/api/" + "doc" + "/list"
        self.request = requests.request


class IpdfExport(InterfaceX):
    def __init__(self, parent,guid):
        InterfaceX.__init__(self, parent)
        self.pdf_export_interface="/pdfExport"
        self.parent=parent
        self.request = requests.request
        self.guid=guid
    def make_url(self):
        self.url = self.parent.base_url + "safety/api/" + self.parent.doc_type + self.pdf_export_interface + "?guid=" + self.guid + "&type={}".format(
            self.parent.doc_type) if self.parent.doc_type is not None else ""

    def open_pdf(self, guid=None):
        os.system("C:\\TEMP\\storage\\pdf\\" + self.guid + ".pdf")

class InterfaceRequestFactory():
    def __init__(self, doc_type=""):
        self.base_url = environment.get_IP_PORT()
        self.headers = environment.get_headers()
        self.doc_type = doc_type

    def list(self):
        return Ilist(self)

    def createDoc(self):
        return IcreateDoc(self)

    def saveDoc(self):
        return IsaveDoc(self)

    def pdfExport(self,guid=None):
        return IpdfExport(self,guid)

    def open_pdf(self, guid):
        os.system("C:\\TEMP\\storage\\pdf\\" + guid + ".pdf")
    def get_doc_list(self):
        return get_doc_list(self)
