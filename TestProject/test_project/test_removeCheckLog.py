# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

from TestProject.test_selenium.login import insert_cookies, login


class RemoveCheckLog(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

        self.cookies_name = "liaoningcookie.json"

    def test_remove_check_log(self):
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

        driver.get("http://218.60.145.28:8080/inspectionCheck/checkMethod")
        time.sleep(1)

        driver.find_element_by_id("companyName").clear()
        driver.find_element_by_id("companyName").send_keys(u"测试abc")
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div/div/div/div[2]/div/span/span/span").click()
        time.sleep(3)

        # 点删除
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td/div/label/span/span").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("//div[3]/button[2]/span").click()





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
