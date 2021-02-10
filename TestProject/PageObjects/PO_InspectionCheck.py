import time

from TestProject.PageObjects.PO_Login import PO_Login
from TestProject.PageObjects.PageObject import PageObject


class PO_InspectionCheck(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "日常检查"
        self.page_url = "inspectionCheck/checkMethod"

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



