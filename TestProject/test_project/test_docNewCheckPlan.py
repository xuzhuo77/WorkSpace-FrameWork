# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from TestProject.test_selenium.login import login, insert_cookies


class AddDocNewCheckPlan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

        self.cookies_name = "liaoningcookie.json"

    def test_addDocNewCheckPlan(self):
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
        driver.find_element_by_xpath("//div[@id='app']/div/div[2]/section/div/div/div/div/div/div/div/button").click()
        time.sleep(1)
        #
        # x = driver.find_element_by_css_selector(" html > body >ul[id^='dropdown-menu'] > li:nth-child(2)")
        # k=x.get_attribute("id")
        # x.click()


        # 选择 新建 日常检查/现场检查方案/双随机检查
        po = WebDriverWait(driver, 30, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                            " html > body >ul[id^='dropdown-menu'] > li:nth-child(2)")))
        po.click()

        # 查询企业 "测试abc"
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[7]/div/div[2]/div/form/div/div/div/div/div/div/button/i").click()
        # driver.find_element_by_xpath("(//input[@type='text'])[15]").send_keys(u"测试abc")

        # '/html/body/div[4]/div/div[2]/div/div[1]/form/div[3]/div/button[1]'
        # 查询按钮
        # driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[1]/form/div[3]/div/button[1]").click()
        # time.sleep(3)
        # x = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[1]/div/label/span")
        # x.click()
        # driver.find_element_by_xpath("//div[3]/div/button[3]/span").click()

        time.sleep(3)
        driver.find_element_by_xpath("(//input[@type='text'])[15]").send_keys(u"测试abc")
        driver.find_element_by_xpath("//form/div[3]/div/button/span").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[2]/div/div[3]/table/tbody/tr/td/div/label/span/span").click()
        driver.find_element_by_xpath("(//button[@type='button'])[48]").click()

        # 填写表单
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@type='text'])[8]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(u"地址")
        driver.find_element_by_xpath("(//input[@type='text'])[9]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[9]").send_keys(u"战三")
        driver.find_element_by_xpath("(//input[@type='text'])[10]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[10]").send_keys(u"中粮")
        # driver.find_element_by_xpath("//tr[3]/td[4]/div/span").click()

        driver.find_element_by_xpath("(//input[@name=''])[3]").click()
        driver.find_element_by_xpath("//td[5]/div/span").click()
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[7]/div/div[2]/div/form/div[3]/div[2]/div/div/div/div/button/i").click()

        driver.find_element_by_xpath("//div[5]/div/div[2]/div/div/div/div/div").click()
        time.sleep(3)
        driver.find_element_by_xpath(
            "/html/body/div[5]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span").click()
        driver.find_element_by_xpath(
            "/html/body/div[5]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[2]/td[1]/div/label/span").click()

        driver.find_element_by_xpath("//form/div[2]/div/button[2]/span").click()
        driver.find_element_by_xpath("//div[2]/div/div[3]/div/button/span").click()

        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[7]/div/div[2]/div/form/div[5]/button/span").click()
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[7]/div/div[2]/div/form/div[5]/button/span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //div[@id='app']/div/div[2]/section/div/div[7]/div/div[2]/div/form/div[5]/button/span | ]]

        driver.find_element_by_xpath("(//input[@type='text'])[13]").send_keys("123")

        driver.find_element_by_xpath("(//input[@type='text'])[14]").send_keys("123")
        driver.find_element_by_xpath("(//input[@type='text'])[15]").click()
        x = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/ul/li[1]")
        k = x.tag_name
        x.click()

        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[7]/div/div[2]/div/form/div[8]/div/div/div/div/textarea").click()

        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[7]/div/div[2]/div/form/div[8]/div/div/div/div/textarea").clear()
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[7]/div/div[2]/div/form/div[8]/div/div/div/div/textarea").send_keys(
            u"备注")
        # 确定保存
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div[7]/div/div[3]/div/button[2]/span").click()

        #     assert 添加成功
        driver.find_element_by_id("companyName").clear()
        driver.find_element_by_id("companyName").send_keys(u"测试abc")
        driver.find_element_by_xpath(
            "//div[@id='app']/div/div[2]/section/div/div/div/div/div[2]/div/span/span/span").click()
        time.sleep(3)
        company_name=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr/td[2]/div').text
        self.assertEqual(company_name,u"测试abc","公司名字错误或不存在")




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
