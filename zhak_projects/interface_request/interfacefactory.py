import requests
import json
import os

from faker import Faker

# from zhak_projects.interface_request import environment_huaian
from zhak_projects.interface_request import environment
from zhak_projects.interface_request.safety_inspection.interface_exception_print import myprint, DataWarp


class InterfaceX():
    def __init__(self, parent):
        self.parent = parent
        self.payload = {}

    def init(self, interface_name,id=None):
        if id:
            self.url = self.parent.base_url + "safety/api/" + self.parent.doc_type + "/" + interface_name+"/"+str(id)
        else:
            self.url = self.parent.base_url + "safety/api/" + self.parent.doc_type + "/" + interface_name
        self.request = requests.request

    @property
    def pay_load(self):
        return json.dumps(self.payload)

    def __call__(self, *args, **kwargs):
        if args:
            self.url += ["/" + str(args[0]) if args[0] else ""][0]
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


class Isave(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.url = parent.base_url + "safety/api/" + parent.doc_type + "/save"
        self.request = requests.request

class Iget(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("get")

class IsaveDoc(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.url = parent.base_url + "safety/api/" + parent.doc_type + "/saveDoc"
        self.request = requests.request



class Idelete(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("delete")


class Idelete_ids(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("delete")


class IlogicalDelete(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("logicalDelete")


class IlogicalDelete_ids(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.init("logicalDelete")


class get_doc_list(InterfaceX):
    def __init__(self, parent):
        InterfaceX.__init__(self, parent)
        self.url = parent.base_url + "safety/api/" + "doc" + "/list"
        self.request = requests.request


class IpdfExport(InterfaceX):
    def __init__(self, parent, guid):
        InterfaceX.__init__(self, parent)
        self.url = parent.base_url + "safety/api/" + parent.doc_type + "/pdfExport" + "?guid=" + guid + "&type={}".format(
            parent.doc_type) if parent.doc_type is not None else ""
        self.request = requests.request
        self.guid = guid

    def open_pdf(self, guid=None):
        os.system("C:\\TEMP\\storage\\pdf\\" + self.guid + ".pdf")
class IpdfExport_id(InterfaceX):
    def __init__(self, parent, id):
        InterfaceX.__init__(self, parent)
        self.url = parent.base_url + "safety/api/" + parent.doc_type + "/exportPdf" + "/" + str(id)
        self.request = requests.request
        self.guid = id

    def open_pdf(self, guid=None):
        os.system("C:\\TEMP\\storage\\pdf\\" + self.guid + ".pdf")

class InterfaceRequestFactory():
    def __init__(self, doc_type=""):
        self.base_url = environment.get_IP_PORT()
        self.headers = environment.get_headers()
        self.doc_type = doc_type
        self.fake = Faker('zh_CN')

    def list(self):
        return Ilist(self)

    def save(self):
        return Isave(self)

    def get(self):
        return Iget(self)

    def delete(self):
        return Idelete(self)

    def delete_ids(self):
        return Idelete_ids(self)

    def logicalDelete(self):
        return IlogicalDelete(self)

    def logicalDelete_ids(self):
        return IlogicalDelete_ids(self)

    def createDoc(self):
        return IcreateDoc(self)

    def saveDoc(self):
        return IsaveDoc(self)

    def pdfExport(self, guid=None):
        return IpdfExport(self, guid)
    def pdfExport_id(self, id=None):
        return IpdfExport_id(self, id)
    def open_pdf(self, guid):
        os.system("C:\\TEMP\\storage\\pdf\\" + guid + ".pdf")

    def get_doc_list(self):
        return get_doc_list(self)

    def logicalDelete_all(self):
        ilist = self.list()
        ids = [int(item["id"]) for item in ilist().pure()["items"]]
        logicalDelete_ids = self.logicalDelete_ids()
        logicalDelete_ids.payload = ids
        logicalDelete_ids()
