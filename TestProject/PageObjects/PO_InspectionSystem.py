import time

from TestProject.PageObjects.PO_Login import PO_Login
from TestProject.PageObjects.PageObject import PageObject

""":arg
        inspectionSystem/caseApprovalConfig
        inspectionSystem / documentConfig
        inspectionSystem / doubleRandom
        inspectionSystem / checkConfiguration
        inspectionSystem / lawBasisCollection
"""


class PO_InspectionSystem_caseApprovalConfig(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "审批人员配置"
        self.page_url = "inspectionSystem/caseApprovalConfig"

    def open(self):
        driver = self.driver
        url = self.base_url + self.page_url
        type2 = self.base_url + 'dljpSpecal?type=2'
        driver.get(type2)
        driver.implicitly_wait(20)
        po_login = PO_Login(driver)
        po_login.insert_cookies()
        driver.get(self.base_url + self.page_url)
        time.sleep(2)
        po_login.isLogin()
        driver.get(url)
        time.sleep(1)


class PO_InspectionSystem_documentConfig(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "文书配置"
        self.page_url = "inspectionSystem / documentConfig"

    def open(self):
        driver = self.driver
        url = self.base_url + self.page_url
        type2 = self.base_url + 'dljpSpecal?type=2'
        driver.get(type2)
        driver.implicitly_wait(20)
        po_login = PO_Login(driver)
        po_login.insert_cookies()
        driver.get(self.base_url + self.page_url)
        time.sleep(2)
        po_login.isLogin()
        driver.get(url)
        time.sleep(1)


class PO_InspectionSystem_doubleRandom(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "双随机配置"
        self.page_url = "inspectionSystem / doubleRandom"

    def open(self):
        driver = self.driver
        url = self.base_url + self.page_url
        type2 = self.base_url + 'dljpSpecal?type=2'
        driver.get(type2)
        driver.implicitly_wait(20)
        po_login = PO_Login(driver)
        po_login.insert_cookies()
        driver.get(self.base_url + self.page_url)
        time.sleep(2)
        po_login.isLogin()
        driver.get(url)
        time.sleep(1)


class PO_InspectionSystem_checkConfiguration(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "常用检查项配置"
        self.page_url = "inspectionSystem / checkConfiguration"

    def open(self):
        driver = self.driver
        url = self.base_url + self.page_url
        type2 = self.base_url + 'dljpSpecal?type=2'
        driver.get(type2)
        driver.implicitly_wait(20)
        po_login = PO_Login(driver)
        po_login.insert_cookies()
        driver.get(self.base_url + self.page_url)
        time.sleep(2)
        po_login.isLogin()
        driver.get(url)
        time.sleep(1)


class PO_InspectionSystem_lawBasisCollection(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "法律法规收藏"
        self.page_url = "inspectionSystem / lawBasisCollection"

    def open(self):
        driver = self.driver
        url = self.base_url + self.page_url
        type2 = self.base_url + 'dljpSpecal?type=2'
        driver.get(type2)
        driver.implicitly_wait(20)
        po_login = PO_Login(driver)
        po_login.insert_cookies()
        driver.get(self.base_url + self.page_url)
        time.sleep(2)
        po_login.isLogin()
        driver.get(url)
        time.sleep(1)
