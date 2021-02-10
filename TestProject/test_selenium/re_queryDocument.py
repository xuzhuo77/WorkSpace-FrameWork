from TestProject.test_selenium.re_cookie import get_session, insert_cookies,test_get_type2
import time
from selenium.webdriver.common.action_chains import ActionChains
from requestium import Session, Keys





def test_query_Document(session):

    main_url = 'http://180.97.151.94:9012/inspectionCheck/queryDocuments?guid=ADD6ACBC-C946-2D15-5AE5-2964092E2512&action=true'
    session.driver.get(main_url)
    session.driver.implicitly_wait(3)
    session.driver.switch_to.window(session.driver.window_handles[-1])
    session.driver.implicitly_wait(3)
    time.sleep(2)
    tag_a_list = session.driver.find_element_by_class_name('leftDiv')
    tag_a_list = tag_a_list.find_elements_by_tag_name("a")
    print(tag_a_list)
    for k, tag_a in enumerate(tag_a_list):
        print(tag_a.get_attribute('class'))
        # print(tag_a.screenshot(str(k)+".jpg"))
        if "el-link" in tag_a.get_attribute('class'):
            if "返回上一级" in tag_a.text:
                continue
            print(tag_a.text)
            tag_a.click()
            time.sleep(2)

        # link=en.find_element_by_class_name('el-link--inner')
        # time.sleep(2)
        # if not link:
        #     link.click()

    time.sleep(20)
    session.driver.quit()

class DocNewDsrcbbl():
    ssj = "	2020/3/4 0:00	"
    esj = "	2020/3/21 0:00	"
    dd = "	中央人民	"
    cssbr = "	张四	"
    xb = "	女	"
    zw = "	司机	"
    gzdw = "	新闻部	"
    dh = "	13842656767	"
    lxdz = "	北京	"
    yb = "	110025	"
    cbr1 = "	鲁迅	"
    cbr2 = "	周树人	"
    jlr = "	记录哥	"
    glj = "	北极管理局	"
    zfry1 = "	执法1	"
    zfry2 = "	执法2	"
    zfzh1 = "	12345	"
    zfzh2 = "	123456	"
    aj = "	好案件	"
    cssbjl = "	这是一个笔录,内容不详	"
    wsxdrq = "	2020/3/4 0:00	"


def test_locate_Document(session):
    if not session:
        session=Session()
    url='http://180.97.151.94:9012/inspectionCheck/queryDocuments?guid=da622969-6c38-4d4f-88c3-7e32e5aaec09&action=true'
    session.driver.get(url)
    session.driver.implicitly_wait(3)
    session.driver.switch_to.window(session.driver.window_handles[-1])
    session.driver.implicitly_wait(3)
    time.sleep(2)
    button='//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/div[1]/div/div/div'
    session.driver.find_element_by_xpath(button).click()
    time.sleep(2)
    '#dropdown-menu-890'
    uls=session.driver.find_elements_by_css_selector('ul[style^="position"]')
    print("--",uls)
    for ul in uls :
        print("S1",ul.get_attribute("class"))
        print("S ",ul.get_attribute("style"))

    main_ul=uls[-1]
    print(main_ul.get_attribute("class"))
    time.sleep(1)
    lis = main_ul.find_elements_by_tag_name('li')
    lis[4].click()

    fill_dsrcbbl(session)

    return session

def fill_dsrcbbl(session):
    dnd=DocNewDsrcbbl()
    ssj='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[1]/div[1]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(ssj)
    js_value = 'arguments[0].value="'+dnd.ssj+'"'
    session.driver.execute_script(js_value,sjb)
    time.sleep(1)

    esj='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[1]/div[2]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(esj)
    js_value = 'arguments[0].value="'+dnd.esj+'"'
    session.driver.execute_script(js_value,sjb)

    dd='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[2]/div/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(dd)
    js_value = 'arguments[0].value="'+dnd.dd+'"'
    session.driver.execute_script(js_value,sjb)

    cssbr='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[3]/div[1]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(cssbr)
    js_value = 'arguments[0].value="'+dnd.cssbr+'"'
    session.driver.execute_script(js_value,sjb)

    xb='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[3]/div[2]/div/div/div/div[1]/input'
    sjb=session.driver.find_element_by_xpath(xb)
    js_value = 'arguments[0].value="'+dnd.xb+'"'
    session.driver.execute_script(js_value,sjb)

    zw='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[3]/div[3]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(zw)
    js_value = 'arguments[0].value="'+dnd.zw+'"'
    session.driver.execute_script(js_value,sjb)

    gzdw='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[4]/div[1]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(gzdw)
    js_value = 'arguments[0].value="'+dnd.gzdw+'"'
    session.driver.execute_script(js_value,sjb)

    dh='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[4]/div[2]/div/div/div[1]/input'
    sjb=session.driver.find_element_by_xpath(dh)
    js_value = 'arguments[0].value="'+dnd.dh+'"'
    session.driver.execute_script(js_value,sjb)

    lxdz='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[5]/div[1]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(lxdz)
    js_value = 'arguments[0].value="'+dnd.lxdz+'"'
    session.driver.execute_script(js_value,sjb)

    yb='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[5]/div[2]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(yb)
    js_value = 'arguments[0].value="'+dnd.yb+'"'
    session.driver.execute_script(js_value,sjb)

    cbr1='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[6]/div[1]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(cbr1)
    js_value = 'arguments[0].value="'+dnd.cbr1+'"'
    session.driver.execute_script(js_value,sjb)

    cbr2='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[6]/div[2]/div/input'
    sjb=session.driver.find_element_by_xpath(cbr2)
    js_value = 'arguments[0].value="'+dnd.cbr2+'"'
    session.driver.execute_script(js_value,sjb)


    jlr='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[6]/div[3]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(jlr)
    js_value = 'arguments[0].value="'+dnd.jlr+'"'
    session.driver.execute_script(js_value,sjb)

    glj='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[7]/div[1]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(glj)
    js_value = 'arguments[0].value="'+dnd.glj+'"'
    session.driver.execute_script(js_value,sjb)


    zfry1='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[7]/div[2]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(zfry1)
    js_value = 'arguments[0].value="'+dnd.zfry1+'"'
    session.driver.execute_script(js_value,sjb)

    zfry2='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[7]/div[3]/div/div/div/input' 
    sjb=session.driver.find_element_by_xpath(zfry2)
    js_value = 'arguments[0].value="'+dnd.zfry2+'"'
    session.driver.execute_script(js_value,sjb)

    zfzh1='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[8]/div[1]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(zfzh1)
    js_value = 'arguments[0].value="'+dnd.zfry1+'"'
    session.driver.execute_script(js_value,sjb)

    zfzh2='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[8]/div[2]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(zfzh2)
    js_value = 'arguments[0].value="'+dnd.zfry2+'"'
    session.driver.execute_script(js_value,sjb)

    aj='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[8]/div[3]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(aj)
    js_value = 'arguments[0].value="'+dnd.aj+'"'
    session.driver.execute_script(js_value,sjb)

    sbjl='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[11]/div/div/div/textarea'
    sjb=session.driver.find_element_by_xpath(sbjl)
    js_value = 'arguments[0].value="'+dnd.cssbjl+'"'
    session.driver.execute_script(js_value,sjb)

    wsrq='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[2]/div/div/form/div/div[12]/div/div/div/input'
    sjb=session.driver.find_element_by_xpath(wsrq)
    js_value = 'arguments[0].value="'+dnd.wsxdrq+'"'
    session.driver.execute_script(js_value,sjb)

    time.sleep(3)
    confirm='//*[@id="app"]/div/div[2]/section/div/div[17]/div/div[3]/div/button[2]'
    button=session.driver.find_element_by_xpath(confirm)
    button.click()

if __name__ == '__main__':
    session = get_session()
    session = test_get_type2(session)
    session=test_locate_Document(session)
    session=fill_dsrcbbl(session)



