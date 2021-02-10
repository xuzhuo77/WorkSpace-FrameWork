class PageObject(object):
    def __init__(self, driver):
        self.page_url = 'https://mail.qq.com/'
        self.driver = driver
        self.timeout = 30
        self.base_url = 'http://218.60.145.28:8080/'
        self.cookies_name = "liaoningcookie.json"
        self.page_name = "page_base_name"

    # 定义打开登录页面方法
    def _open(self):
        url = self.base_url
        self.driver.get(url)
        self.driver.switch_to.frame('login_frame')  # 切换到登录窗口的iframe

    # 定义定义open方法，调用_open()进行打开
    def open(self):
        self._open()

    # 定位方法封装
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def send_Keys(self, xpath, value):
        self.driver.find_element_by_xpath(xpath).send_keys(value)

    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()


