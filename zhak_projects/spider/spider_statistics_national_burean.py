from bs4 import BeautifulSoup
import requests
import queue
next_q=queue.Queue()

table_names=["citytable","countytable","towntable","villagetable"]
def get(url,region_code,pid=None):
    r = requests.get(url)
    demo = r.text  # 服务器返回响应
    soup = BeautifulSoup(demo, "html.parser")
    citytable = soup.findAll(class_="citytable")
    if citytable:
        for tr in citytable[0].findAll("tr"):
            key,value=tr.findAll("td")

            key1=key.find("a")
            value1=value.find("a")
            # if key.contains('a'):
            if key1:
                # print(key1.attrs['href'],key1.string,value1.string,key1.attrs['href'].split("/")[0])
                # print(key1.attrs['href'],key1.string,value1.string,key1.attrs['href'].split("/")[0])
                id,pid,content=key1.string,pid,value1.string
                print(id,pid,content)
                next_q.put((key1.attrs["href"],key1.string,""))
            else:
                print(key.string,value.string)
    countytable = soup.findAll(class_="countytable")
    if countytable:
        for tr in countytable[0].findAll("tr"):
            key, value = tr.findAll("td")

            key1 = key.find("a")
            value1 = value.find("a")
            # if key.contains('a'):
            if key1:
                # print(key1["href"], key1.string, value1.string)
                next_q.put((key1.attrs["href"],key1.string,"64/"))
                id,pid,content=key1.string,pid,value1.string
                print(id,pid,content,key1.attrs["href"])


            else:
                print(key.string, value.string)
    towntable = soup.findAll(class_="towntable")
    if towntable:
        for tr in towntable[0].findAll("tr"):
            key, value = tr.findAll("td")

            key1 = key.find("a")
            value1 = value.find("a")
            # if key.contains('a'):
            if key1:
                # print(key1["href"], key1.string, value1.string)
                next_q.put((key1.attrs["href"],key1.string,key1.string[:2]+"/"+key1.string[2:4]+"/"))
                id,pid,content=key1.string,pid,value1.string
                print(id,pid,content,key1.attrs["href"])

            else:
                print(key.string, value.string)
    villagetable = soup.findAll(class_="villagetable")
    if villagetable:
        for tr in villagetable[0].findAll("tr"):
            td=tr.findAll("td")
            # print(td[0].string,td[1].string,td[2].string)
            id,pid,code,content=td[0].string,pid,td[1].string,td[2].string
            print(id,pid,code,content)
#


# get("http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/64/05/02/640502102.html",'64/05/',"640502102000")
# get("http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/64/05/640522.html","64","640500000000")
# get("http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/64/6405.html","","640501000000")
# next_q.put(("64.html",640000000000,""))
t="640522103000"
# next_q.put(("22/640522105.html","640522103000",t[:2]+"/"+t[2:4]+"/"))
t="640522000000"
next_q.put(("05/640522.html","640522000000",t[:2]+"/"))
base_url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/"

while next_q.empty() is False:
    q_item=next_q.get()
    pageUrl,pid,region=q_item
    print(q_item)
    url=base_url+region+pageUrl
    print(url)
    get(url,region,pid)
