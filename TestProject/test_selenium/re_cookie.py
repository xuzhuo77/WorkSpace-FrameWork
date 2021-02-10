from requestium import Session, Keys
import time
import json

from TestProject.test_selenium.re_auth import get_Cookies
import sys
sys.path.append("..")

def get_session():
    session = Session(webdriver_path='E:/pythonWebWorkSpace/WorkSpace-FrameWork/TestProject/test_selenium/chromedriver.exe',
                          browser='chrome',
                          default_timeout=15,
                          # webdriver_options={'arguments': ['headless']}
                          )
    try:
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)
        if len(cookies) == 0:
            raise Exception("empty cookie")

        return session
    except:
        session = get_Cookies(username="csgq1",session=session)
        return session


def insert_cookies(session):
    with open('cookies.json', 'r') as f:
        cookies = json.load(f)
    for cookie in cookies:
            session.driver.add_cookie(cookie)


def test_checkMethod(session):
    type2 = 'http://180.97.151.94:9012/dljpSpecal?type=2'
    url_rcjc = 'http://180.97.151.94:9012/inspectionCheck/checkMethod'
    session.driver.get(type2)
    time.sleep(1)
    insert_cookies(session)
    session.driver.get(url_rcjc)
    time.sleep(2)

    x_name = '//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[3]/table'
    l = session.driver.find_element_by_xpath(x_name)
    # chakan='//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[3]/table/tbody/tr[1]/td[8]/div/div/div'
    #         '//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[3]/table/tbody/tr[2]/td[8]/div/div/div'
    for i in range(8):
        chakan = '//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[3]/table/tbody/tr['+str(i+1)+']/td[8]/div/div/div'
                 # '//*[@id="app"]/div/div[2]/section/div/div[2]/div/div[3]/table/tbody/tr[4]/td[8]/div/div/div'
        linkchak=session.driver.find_element_by_xpath(chakan)
        linkchak.click()

        time.sleep(2)
        session.driver.switch_to.window(session.driver.window_handles[-1])
        time.sleep(2)
        session.driver.back()
        session.driver.implicitly_wait(2)
        # session.driver.switch_to.window(session.driver.window_handles[-1])
    session.driver.close()
    session.driver.quit()

def test_get_type2(session):
    type2 = 'http://180.97.151.94:9012/dljpSpecal?type=2'
    session.driver.get(type2)
    session.driver.implicitly_wait(2)
    insert_cookies(session)
    return session



if __name__ == '__main__':

    session=get_session()
    test_checkMethod(session)
# # 定位到要悬停的元素
# move = driver.find_element_by_id("xx")
# # 对定位到的元素执行悬停操作
# ActionChains(driver).move_to_element(move).perform()
