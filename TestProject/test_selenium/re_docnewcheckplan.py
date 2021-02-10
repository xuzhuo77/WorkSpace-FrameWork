from selenium.webdriver import ActionChains

from TestProject.test_selenium.re_cookie import get_session, test_get_type2
from requestium import Session, Keys
import time


def test_locate_Document(session):
    if not session:
        session = Session()
    url = 'http://180.97.151.94:9012/inspectionCheck/checkMethod'
    session.driver.get(url)
    session.driver.switch_to.window(session.driver.window_handles[-1])
    session = add_zhifajianca(session)
    return session


def add_zhifajianca(session):
    # 新增执法检查
    jianchajilu_button_xpath = '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/div[1]/div/button[1]'
    session.driver.find_element_by_xpath(jianchajilu_button_xpath).click()
    time.sleep(2)

    session = selectGrid(session)
    fill_docnewcheckplan(session)
    return session


def selectGrid(session):
    wangge_xpath = '/html/body/div[3]/div/div[2]/div/div/div[1]/div[1]/span[2]'
    button_confime = '/html/body/div[3]/div/div[3]/div/button[2]'
    d = session.driver.find_element_by_xpath(wangge_xpath)
    d.click()
    print(d)
    d = session.driver.find_element_by_xpath(button_confime)
    d.click()
    time.sleep(1)
    return session


def fill_docnewcheckplan(session):
    xpathes = {
        "bjcdw": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[1]/div[1]/div[1]/div/div/div[1]/input',
        "dz": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[1]/div[1]/div[2]/div/div/div/input',
        "fddbr": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[1]/div[2]/div[1]/div/div/div/input',
        "zw": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[1]/div[2]/div[2]/div/div/div/input',
        "lxdh": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[1]/div[3]/div[1]/div/div/div/input',
        "jccs": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[1]/div[3]/div[2]/div/div/div/input',
        "jcsj": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[1]/div[4]/div[1]/div/div/div/input',
        "jcjssj": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[1]/div[4]/div[2]/div/div/div/input',
        "xzzfry": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[1]/div[5]/div[1]/div/div/div/input',
        "zjhm": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[1]/div[5]/div[2]/div/div/div/input',
        "lhzfry": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[1]/div[6]/div[1]/div/div/div/input',
        "lhzfryzh": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[1]/div[6]/div[2]/div/div/div/input',
        "xcdyjcx": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[3]/button[1]',
        "jcqq1": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[4]/div/div[3]/table/tbody/tr[1]/td[1]/div/div/input',
        "jcqq2": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[4]/div/div[3]/table/tbody/tr[2]/td[1]/div/div/input',
        "confirm": '/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[3]/div/button[2]',
    }
    driver=session.driver
    doc=DocNewCheckPlan()
    time.sleep(1)
    bjcdwsearch='//*[@id="app"]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[1]/div[1]/div[1]/div/div/div/div/button'
    qy="/html/body/div[5]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div/label"
    tj="/html/body/div[5]/div/div[2]/div/div[1]/form/div[3]/div/button[3]"
    session.driver.find_element_by_xpath(bjcdwsearch).click()
    session.driver.find_element_by_xpath(qy).click()
    session.driver.find_element_by_xpath(tj).click()


    # fill(driver, xpathes["bjcdw"], doc.bjcdw)
    fill(driver, xpathes["dz"], doc.dz)
    fill(driver, xpathes["fddbr"], doc.fddbr)
    fill(driver, xpathes["zw"], doc.zw)
    fill(driver, xpathes["lxdh"], doc.lxdh)
    fill(driver, xpathes["jccs"], doc.jccs)
    fill(driver, xpathes["jcsj"], doc.jcsj)
    fill(driver, xpathes["jcjssj"], doc.jcjssj)



    zfrysearch="/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[2]/div/form/div[1]/div[5]/div[1]/div/div/div/div/button"
    select_person='/html/body/div[4]/div'
    glj="/html/body/div[4]/div/div[2]/div/div[1]/div/div[1]/div"
    p1="/html/body/div[4]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div/label"
    p2='/html/body/div[4]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr[2]/td[1]/div/label'
    add='/html/body/div[4]/div/div[2]/div/div[2]/form/div[2]/div/button[2]'
    zfry_add='/html/body/div[4]/div/div[2]/div/div[3]/div[1]/button[1]'

    session.driver.find_element_by_xpath(zfrysearch).click()
    time.sleep(3)
    sp=session.driver.find_element_by_xpath(select_person)
    print(sp)
    sp.find_element_by_xpath(glj).click()
    sp.find_element_by_xpath(p1).click()
    sp.find_element_by_xpath(p2).click()
    sp.find_element_by_xpath(add).click()
    sp.find_element_by_xpath(zfry_add).click()

    # ActionChains(driver)..click(hidden_submenu).perform()


    # fill(driver, xpathes["xzzfry"], doc.xzzfry)
    fill(driver, xpathes["zjhm"], doc.zjhm)
    fill(driver, xpathes["lhzfry"], doc.lhzfry)
    fill(driver, xpathes["lhzfryzh"], doc.lhzfryzh)


    session.driver.find_element_by_xpath(xpathes["xcdyjcx"]).click()
    session.driver.find_element_by_xpath(xpathes["xcdyjcx"]).click()

    fill(driver, xpathes["jcqq1"], "23123")
    fill(driver, xpathes["jcqq2"], "kkkk")
    session.driver.find_element_by_xpath(xpathes["confirm"]).click()

def fill(driver,xpath,value):
    target=driver.find_element_by_xpath(xpath)
    js_value = 'arguments[0].value="'+value+'"'
    driver.execute_script(js_value,target)
class DocNewCheckPlan():
    bjcdw = '123'
    dz = '123'
    fddbr = '这个法定代表人'
    zw = '好职务'
    lxdh = '18332667423'
    jccs = '某个好场所'
    jcsj = '2020-04-06 00:00:00'
    jcjssj = '2020-04-08 00:00:00'
    xzzfry = '孙永林,戚文杰'
    zjhm = '123'
    lhzfry = '123'
    lhzfryzh = 'aaaaa'


def add_jianchafangan(session):
    # 新增检查方案
    jianchafangan_button_xpath = '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/div[1]/div/button[2]'
    session.driver.find_element_by_xpath(jianchafangan_button_xpath).click()
    time.sleep(2)



if __name__ == '__main__':
    s = get_session()
    s = test_get_type2(s)
    s = test_locate_Document(s)
