
from requestium import Session, Keys
import time
from selenium.webdriver import ActionChains

session = Session(webdriver_path='phantomjs-2.1.1-windows/bin/phantomjs.exe',
                  browser='phantomjs',
                  default_timeout=15,
                  # webdriver_options={'arguments': ['headless']}
                  )


# session.driver.get('http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/15/1504.html')

# time.sleep(2)


def _find(driver):
    table=driver.find_element_by_css_selector('table[class$="table"]')
    # time.sleep(2)
    # print(table)
    head=table.find_element_by_css_selector('tr[class$="head"]')
    # print(head.text)
    trs=table.find_elements_by_css_selector('tr[class$="tr"]')
    # time.sleep(2)

    a_s=table.find_elements_by_tag_name("a")

    for tr in trs:
        print(tr.text)
    if a_s:
        for i in range(1,len(a_s),2):
            href=a_s[i].get_attribute("href")
            print(a_s[i].text)
            # a_s[i].click()
            # driver.switch_to.window(driver.window_handles[-1])
            # actions.key_down(Keys.CONTROL).click(a_s[i]).key_up(Keys.CONTROL).perform()

            # time.sleep(1)
            _find(driver)

    else:
        driver.back()

        driver.switch_to.window(driver.window_handles[-1])



# _find(session.driver)
import queue
qu = queue.Queue()
def except_queue(queue,current_url):
    with open("f_que.txt", "w",encoding="utf8") as file:
        urls = [current_url[0]+" "+current_url[1]+" "+current_url[2]]
        while not queue.empty():
            url = queue.get()
            urls.append(url[0]+" "+url[1]+" "+url[2])
        file.writelines("\n".join(urls))
def _get(session,fcode):
    # time.sleep(2)
    session.driver.switch_to.window(session.driver.window_handles[-1])

    table=session.driver.find_element_by_css_selector('table[class$="table"]')
        # time.sleep(2)
        # print(table)
    head=table.find_element_by_css_selector('tr[class$="head"]')
    trs=table.find_elements_by_css_selector('tr[class$="tr"]')
    a_s=table.find_elements_by_tag_name("a")


    t=[]
    d={}
    for tr in trs:
        # print(tr.text)
        sp=tr.text.split(" ")
        if len(sp)==3:
            code,c,address=sp
            d[address] = code
            t.append(code+" "+ address+ " " + fcode+" "+c)
        else:
            code, address=sp
            d[address] = code
            t.append(tr.text + " " + fcode)


    if a_s:
        for i in range(1,len(a_s),2):
            href=a_s[i].get_attribute("href")
            code=d[a_s[i].text]
            qu.put((code,a_s[i].text,href))
    return "\n".join(t)


qu.put(("co","s",'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/15/1504.html'))
# with open("f_que.txt","r") as f_que:
#     a=f_que.readline()
#     a = a.split(" ")
#     t = (a[0], a[1], a[2])
#     qu.put(a)
#     while a:
#         a=f_que.readline()
#         if "http:" in a:
#             a=a.split(" ")
#             t=(a[0],a[1],a[2])
#             qu.put(t)
# while not qu.empty():
#     print(qu.get())
with open("f2.txt","a",encoding="utf8") as f:
    while not qu.empty():
        print(qu.qsize())

        k= qu.get()
        hcode, address, url=k
        print(address,url.split("/")[-1])
        try:
            session.driver.get(url)
        except Exception as e:
            except_queue(qu, (hcode,address,url))

        try:
            l=_get(session,hcode)
        except Exception as e:
            except_queue(qu,(hcode,address,url))
            session.driver.get(url)
            l=_get(session,hcode)
        # print(l)
        f.writelines("\n")
        f.writelines(l)
print("end")

