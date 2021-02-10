from requestium import Session, Keys
import time
import json


def get_Cookies(username="admin", passwo="WE@3dfsa", session=None):
    if not None:
        session = Session(
                          webdriver_path='E:/pythonWebWorkSpace/WorkSpace-FrameWork/TestProject/test_selenium/chromedriver.exe',
                          # webdriver_path='geckodriver.exe',
                          browser='chrome',
                          default_timeout=15,
                          # webdriver_options={'arguments': ['headless']}
                          )
    session.driver.get('http://180.97.151.94:9012/login')
    us = '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/form/div[1]/div/div/input'
    pa = '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/form/div[2]/div/div/input'
    sub = '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/form/div[4]/div/button'

    session.driver.find_element_by_xpath(us).send_keys(username)
    session.driver.find_element_by_xpath(pa).send_keys(passwo)
    time.sleep(5)

    session.driver.find_element_by_xpath(sub).click()
    # s.driver.switch_to.window(s.driver.window_handles[-1])
    time.sleep(1)
    # safety='//*[@id="app"]/div/div[1]/div[4]/div/div/div[1]/div'
    # s.driver.find_element_by_xpath(safety).click()
    #
    # s.driver.switch_to.window(s.driver.window_handles[-1])
    #
    # richang='//*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[6]/a/li'
    # s.driver.find_element_by_xpath(richang).click()
    #
    cookies = session.driver.get_cookies()
    with open('cookies.json', 'w') as f:
        cookies = json.dump(cookies, f)
    return session
    # s.driver.close()
    # s.driver.quit()

    # s.driver.switch_to.window(s.driver.window_handles[-1])
    # # sreach_window=s.driver.current_window_handle
    # time.sleep(2)
    # chakan='//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[3]/table/tbody/tr[2]/td[8]/div/div/div'
    # s.driver.find_element_by_xpath(chakan).click()





if __name__ == '__main__':
    get_Cookies()
