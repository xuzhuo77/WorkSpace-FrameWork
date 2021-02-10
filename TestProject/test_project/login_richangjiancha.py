# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import json


class LoginRichangjiancha(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_richangjiancha(self):
        driver = self.driver
        driver.get("http://218.60.145.28:8080/login")
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("sunyy")
        driver.find_element_by_xpath("//input[@type='password']").click()
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("WE@3dfsa")
        time.sleep(5)

        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[3]/div/div/div/div/div[2]/form/div[5]/div/button/span").click()
        time.sleep(2)

        driver.find_element_by_xpath("//div[@id='app']/div/header/div/div/div/div[2]/ul/li[2]/div/span").click()
        driver.find_element_by_xpath("//div[@id='pane-first']/div/div/div/div[2]/div[2]/div").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.switch_to.window(driver.window_handles[-1])
        driver.implicitly_wait(30)

        driver.find_element_by_xpath("//div[@id='app']/div/div/div/div/div/ul/div[5]/a/li/span").click()

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
