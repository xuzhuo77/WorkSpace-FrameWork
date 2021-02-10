import requests
from bs4 import BeautifulSoup
import re
import datetime
import time
# import yagmail
# from sendmail import Mail


def qingqiu():
    link = "http://jwxt.cupl.edu.cn/eams/teach/grade/course/person!search.action?semesterId=173&projectType=&projectId=1&_=1610462261440"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400',
        'Host': 'jwxt.cupl.edu.cn',
        'Cookie': 'semester.id=173; JSESSIONID=97C12DB1EA7C89F6C11BE90C27593F60.web1; SecTs-20480=EHABBAAKJABP; uname=190201341; lv=1; fid=16619; 16619userinfo=6cb2606b4382afd1f5fd187b8f34e093c49d67c0c30ca5047c5a963e85f11099e655533809e7904fd6a55a6327757746b3937b0ff5adfbc8096bf2d55b33b698; 16619UID=105352689; 16619enc=BCF74063FF9A7B99F4EA0BAB1F48F25B; _uid=105352689; uf=b2d2c93beefa90dcf08790ea8aa3af1eb877bf51d8cb35bd71cf49933c8920d3f682d3efb4224772cc0202bff96961fdd110c105546a283d88b83130e7eb4704f266005c1959c8c46e8c487b43036c04a696d78956426448561c5a5ee860473fa67ad453ac8db317e7fafd565af53bf2; _d=1609841178599; UID=105352689; vc=BCF74063FF9A7B99F4EA0BAB1F48F25B; vc2=4A943DE0755C339774D712C21500776F; vc3=aYSmQ0X%2F%2FXyKnmnkaPVu2kW6xw1SSeLpfcrzCSzS8YGWioqihj4CFUXnFtkrr1uBbeUciTJssafAhZqtG9LVY2GGkEzgeA6GC13IUNwUeHjbT5ExNlrmi2auSQY4%2FK6%2BYNOrQsm431dtDnJae2dXkY41LuB5SUboUyjGpVTQzvg%3D9dea60ed14c2eb353bca1f21d6b95acd; xxtenc=4c82a2c5db8baca92e602c1f64e09fca; DSSTASH_LOG=C_38-UN_17314-US_105352689-T_1609841178600; GSESSIONID=97C12DB1EA7C89F6C11BE90C27593F60.web1'}
    session = requests.Session()
    r = session.get(link, headers=headers)
    content = r.text
    return content


def update():
    print('通知系统启动中')
    old_pattern = qingqiu()
    while True:
        new_pattern = qingqiu()
        if new_pattern != old_pattern:
            old_pattern = new_pattern
            Mail().sendmail(msg=new_pattern[0], title='信息内容', receivers='1328133544@qq.com')
        else:
            now = datetime.datetime.now()
