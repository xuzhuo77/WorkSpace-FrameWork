# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from selenium.webdriver.support.wait import WebDriverWait

from TestProject.PageObjects.PO_InspectionCheck import PO_InspectionCheck
from TestProject.test_selenium.login import insert_cookies, login
from selenium.webdriver.support import expected_conditions as EC


class AddDocNewCheckResult(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.cookies_name = "liaoningcookie.json"

    def test_DocNewCheckResult(self):
        driver = self.driver
        baseurl = 'http://218.60.145.28:8080/'

        # 打开日常检查界面
        inspection=PO_InspectionCheck(driver)
        inspection.open()


        #
        # x = driver.find_element_by_css_selector(" html > body >ul[id^='dropdown-menu'] > li:nth-child(2)")
        # k=x.get_attribute("id")
        # x.click()

        # 选择 新建 日常检查/现场检查方案/双随机检查
        po = WebDriverWait(driver, 30, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                            " html > body >ul[id^='dropdown-menu'] > li:nth-child(1)")))
        po.click()
        # 查找被检查单位
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[4]/div/div[2]/div/form/div/div/div/div/div/div/div/button/i").click()
        time.sleep(3)
        driver.find_element_by_xpath("(//input[@type='text'])[20]").send_keys(u"测试abc")
        driver.find_element_by_xpath("//form/div[3]/div/button/span").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[2]/div/div[3]/table/tbody/tr/td/div/label/span/span").click()
        driver.find_element_by_xpath("(//button[@type='button'])[52]").click()

        # 填表
        driver.find_element_by_xpath("(//input[@type='text'])[10]").send_keys(u"职务")

        driver.find_element_by_xpath("(//input[@type='text'])[12]").send_keys(u"场所")
        driver.find_element_by_xpath("(//input[@name=''])[3]").click()
        driver.find_element_by_xpath("//tr[3]/td[4]/div/span").click()
        driver.find_element_by_xpath("(//input[@name=''])[4]").click()
        driver.find_element_by_xpath("//div[5]/div/div/div[3]/table/tbody/tr[3]/td[4]/div/span").click()
        driver.find_element_by_xpath("(//button[@type='button'])[13]").click()
        driver.find_element_by_xpath("//div[2]/div/div/div/div/div/span[2]").click()
        # 查找
        time.sleep(3)
        driver.find_element_by_xpath("//div[2]/div/div[3]/table/tbody/tr/td/div/label/span/span").click()
        driver.find_element_by_xpath("//div[2]/div/div[3]/table/tbody/tr[2]/td/div/label/span/span").click()
        driver.find_element_by_xpath("(//button[@type='button'])[66]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[67]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[16]").send_keys("21321,123123")
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[4]/div/div[2]/div/form/div[3]/button/span").click()
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[4]/div/div[2]/div/form/div[3]/button/span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //div[@id='app']/div/div[2]/section/div/div[4]/div/div[2]/div/form/div[3]/button/span | ]]
        driver.find_element_by_xpath("(//input[@type='text'])[19]").send_keys("abc")
        driver.find_element_by_xpath("(//input[@type='text'])[20]").send_keys("abc")
        # 缺少日期 缺少文书日期

        # 确定
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]/span").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
