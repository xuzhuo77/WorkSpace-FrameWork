# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from TestProject.test_selenium.login import insert_cookies, login


class AddSecurity(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.cookies_name = "liaoningcookie.json"

    def test_AddSecurity(self):
        driver = self.driver
        baseurl = 'http://218.60.145.28:8080/'

        type2 = baseurl + 'dljpSpecal?type=2'
        driver.get(type2)
        driver.implicitly_wait(20)
        insert_cookies(self.cookies_name, driver)
        driver.get("http://218.60.145.28:8080/inspectionCheck/checkMethod")
        time.sleep(2)
        if 'login' in driver.current_url:
            login(driver, baseurl, self.cookies_name)

        driver.get("http://218.60.145.28:8080/inspectionCasehandling/securityList")
        time.sleep(1)

        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/section/div/div/div[2]/button/span").click()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/ul/li[1]").click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div/div[4]/div/div[2]/div/div[4]/div').click()


        x=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/section/div/div[4]/div/div[2]/div/div[5]/form/div/div[2]/div/div/div/div/input")
        x.click()

        driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/ul/li[1]").click()
        driver.find_element_by_xpath("(//input[@name=''])[3]").click()
        driver.find_element_by_xpath("//tr[4]/td[5]/div/span").click()
        driver.find_element_by_xpath("(//input[@type='text'])[9]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[9]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[9]").send_keys(u"测试案件名称")
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[4]/div/div[2]/div/div[5]/form/div/div[6]/div/div/div/div/button/i").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/div/div/div[1]/form/div[1]/div/div/input").send_keys(u"测试abc")
        driver.find_element_by_xpath("//form/div[3]/div/button/span").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/div/div/div[2]/div/div[3]/table/tbody/tr/td[1]/div/label/span").click()
        driver.find_element_by_xpath("/html/body/div[7]/div/div[2]/div/div/div[1]/form/div[3]/div/button[3]").click()
        time.sleep(2)

        driver.find_element_by_xpath("(//input[@type='text'])[11]").send_keys("18516112475")
        driver.find_element_by_xpath("(//input[@type='text'])[13]").send_keys("110066")
        driver.find_element_by_xpath("(//input[@type='text'])[14]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").send_keys("")
        driver.find_element_by_xpath("(//input[@type='text'])[14]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[14]").send_keys(u"测试地址")
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[4]/div/div[2]/div/div[5]/form/div/div[11]/div/div/div/textarea").click()
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[4]/div/div[2]/div/div[5]/form/div/div[11]/div/div/div/textarea").clear()
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[4]/div/div[2]/div/div[5]/form/div/div[11]/div/div/div/textarea").send_keys(
            u"测试状况")
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[4]/div/div[2]/div/div[5]/form/div/div[12]/div/div/div/textarea").click()
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[4]/div/div[2]/div/div[5]/form/div/div[12]/div/div/div/textarea").clear()
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[4]/div/div[2]/div/div[5]/form/div/div[12]/div/div/div/textarea").send_keys(
            u"测试意见")
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[4]/div/div[2]/div/div[5]/form/div/div[15]/div/div/div/div/button/i").click()
        driver.find_element_by_xpath("//div[2]/div/div/div/div/div/span[2]").click()
        driver.find_element_by_xpath("//div[32]/div/span[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[7]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span").click()

        driver.find_element_by_xpath("//form/div[2]/div/button[2]/span").click()
        print(1)
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
