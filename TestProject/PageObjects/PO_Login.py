import json
import time

from TestProject.PageObjects.PageObject import PageObject


# 登录
class PO_Login(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.page_name = "login"
        self.page_url = "login"
        self.cookies_name = "liaoningcookie.json"

        self.xpath_username = "//input[@type='text']"
        self.xpath_password = "//input[@type='password']"
        self.confim = "//div[@id='app']/div/div[3]/div/div/div/div/div[2]/form/div[5]/div/button/span"

    def open(self):
        driver = self.driver
        url = self.base_url + self.page_url
        driver.get(url)

    def login(self):
        # self.open()
        self.send_Keys(self.xpath_username, "sunyy")
        self.send_Keys(self.xpath_password, "WE@3dfsa")
        time.sleep(4)
        self.click(self.confim)
        self.driver.implicitly_wait(30)
        self.acquire_cookies()

    def acquire_cookies(self):
        cookies = self.driver.get_cookies()
        with open(self.cookies_name, 'w') as f:
            json.dump(cookies, f)

    def insert_cookies(self):
        with open(self.cookies_name, 'r') as f:
            cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)

    def isLogin(self):
        if 'login' in self.driver.current_url:
            self.login()
