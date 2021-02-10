# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('http://180.97.151.94:9012/login')
# username=browser.find_element_by_name("username")
# password=browser.find_element_by_name("password")
#
# username.send_keys("admin")
# password.send_keys("WE@3dfsa")

xpath_username='/html/body/div[1]/div/form/div[1]/div/div/input'
xpath_password='/html/body/div[1]/div/form/div[2]/div/div/input'
xpath_submit='/html/body/div[1]/div/form/div[4]/div/div/div[1]/button'

#!/usr/bin/python3
# -*- coding:utf-8 -*-
__author__ = 'mayi'

# 导入webdriver
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
# # 调用环境变量指定的PhantomJS浏览器创建浏览器对象，executable_path：指定PhantomJS位置
# driver = webdriver.PhantomJS(executable_path=r"phantomjs-2.1.1-windows\bin\phantomjs")
#
# # get()方法会一直等到页面被完全加载，然后才会继续程序
# driver.get("http://180.97.151.94:9012/login")
# driver.save_screenshot("baidu.jpg")
# print(driver)
# driver.find_element_by_class_name("el-input__inner").send_keys("admin")
#
# time.sleep(2)
# username=driver.find_element_by_xpath(xpath_username)
# password=driver.find_element_by_xpath(xpath_username)
# confirm=driver.find_element_by_xpath(xpath_submit)


he={"Host": "180.97.151.94:9012",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
"Accept": "image/webp,*/*",
"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding": "gzip, deflate",
"Connection": "keep-alive",
"Referer": "http://180.97.151.94:9012/dljpSpecal",
"Cookie": "safetyUIUrl=http://180.97.151.94:9012/safety; Admin-Token=","eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjciLCJ1c2VyR3VpZCI6IjIyNENDNDE3RjI0OTQ3OTBCNUQ1OTYxRDRDNDQ2RDc4IiwiZXhwIjoxNTg1MDU5NzU3fQ.4tf9geky-qQof6t1hQdZGbnFkH_aKeFbJPE_umC1Ddk"
}

cookie={
    "value":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjciLCJ1c2VyR3VpZCI6IjIyNENDNDE3RjI0OTQ3OTBCNUQ1OTYxRDRDNDQ2RDc4IiwiZXhwIjoxNTg1MDU5NzU3fQ.4tf9geky-qQof6t1hQdZGbnFkH_aKeFbJPE_umC1Ddk"
    ,"name":"Admin-Token"
}

import time
from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(firefox_options=options)
driver.get('http://180.97.151.94:9012/login')
driver.find_element_by_xpath(xpath_username).send_keys("admin")
driver.find_element_by_xpath(xpath_password).send_keys("WE@3dfsa")
driver.find_element_by_xpath(xpath_submit).submit()
time.sleep(5)

# 获取页面名为wrapper的id标签的文本内容
# data = driver.find_element_by_id("wrapper").text



# # 打印获取的文本内容
# print(data)
#
# # 打印页面标题：百度一下，你就知道
# print(driver.title)
#
# # 生成当前页面快照并保存
# driver.save_screenshot("baidu.jpg")
#
# # 在百度搜索输入框中输入“蚂蚁”
# driver.find_element_by_id("kw").send_keys("蚂蚁")
#
# # 模拟点击“百度一下”按钮
# driver.find_element_by_id("su").click()
# # 等待2秒，让页面加载
# time.sleep(2)
#
# # 获取搜索后的页面快照
# driver.save_screenshot("蚂蚁.jpg")
#
# # 打印网页渲染后的源代码
# # print(driver.page_source)
#
# # 获取当前页面Cookie
# print(driver.get_cookies())
#
# # Ctrl + a 全选输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "a")
#
# # Ctrl + x 剪切输入框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL, "x")
#
# # 输入框重新输入内容
# driver.find_element_by_id("kw").send_keys("python")
#
# # 模拟Enter回车键
# driver.find_element_by_id("su").send_keys(Keys.ENTER)
#
# # 等待2秒，让页面加载
# time.sleep(2)
#
# # 清除输入框内容
# driver.find_element_by_id("kw").clear()
#
# # 获取新的快照
# driver.save_screenshot("python.jpg")
#
# # 获取当前url
# print(driver.current_url)
#
# # 关闭当前页面，如果只有一个页面，会关闭浏览器
# driver.close()

# 关闭浏览器
driver.quit()