import json
import time


def login(driver, baseurl, cookie_name):
    # driver.get(baseurl + "login")
    driver.find_element_by_xpath("//input[@type='text']").click()
    driver.find_element_by_xpath("//input[@type='text']").clear()
    driver.find_element_by_xpath("//input[@type='text']").send_keys("sunyy")
    driver.find_element_by_xpath("//input[@type='password']").click()
    driver.find_element_by_xpath("//input[@type='password']").clear()
    driver.find_element_by_xpath("//input[@type='password']").send_keys("WE@3dfsa")
    time.sleep(5)
    driver.find_element_by_xpath(
        "//div[@id='app']/div/div[3]/div/div/div/div/div[2]/form/div[5]/div/button/span").click()
    driver.implicitly_wait(30)
    cookies = driver.get_cookies()
    with open(cookie_name, 'w') as f:
        cookies = json.dump(cookies, f)


def insert_cookies(jsonname, driver):
    with open(jsonname, 'r') as f:
        cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)