url = "http://180.97.151.94:9012/inspectionCheck/checkMethod"

cookies = [
    {
        "name": "Admin-Token",
        "value": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjciLCJ1c2VyR3VpZCI6IjIyNENDNDE3RjI0OTQ3OTBCNUQ1OTYxRDRDNDQ2RDc4IiwiZXhwIjoxNTg1MDU5NzU3fQ.4tf9geky-qQof6t1hQdZGbnFkH_aKeFbJPE_umC1Ddk"

    }
    , {
        "name": "safetyUIUrl",
        "value": "http://180.97.151.94:9012/safety"

    }
]
from selenium import webdriver

options = webdriver.FirefoxOptions()
argu = 'Host=180.97.151.94:9012 \
User-Agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0 \
Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8 \
Accept-Language=zh-CN \
Accept-Encoding=gzip, deflate \
Content-Type= application/json;charset=utf-8 \
access_token= eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjciLCJ1c2VyR3VpZCI6IjIyNENDNDE3RjI0OTQ3OTBCNUQ1OTYxRDRDNDQ2RDc4IiwiZXhwIjoxNTg1MDYyNDczfQ.3YgnSDeP0-l4OuA8YaFUR5Hv_Qxy5tWHmIwpVgrzPas\
Content-Length= 242 \
Origin= http://180.97.151.94:9012 \
Connection= keep-alive \
Referer= http://180.97.151.94:9012/inspectionCheck/checkMethod \
Cookie= safetyUIUrl=http://180.97.151.94:9012/safety; Admin-Token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjciLCJ1c2VyR3VpZCI6IjIyNENDNDE3RjI0OTQ3OTBCNUQ1OTYxRDRDNDQ2RDc4IiwiZXhwIjoxNTg1MDYyNDczfQ.3YgnSDeP0-l4OuA8YaFUR5Hv_Qxy5tWHmIwpVgrzPas'
argu2 = 'Host= 180.97.151.94:9012 \
User-Agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0 \
Accept= text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8 \
Accept-Language= zh-CN \
Accept-Encoding= gzip, deflate \
Connection= keep-alive \
Upgrade-Insecure-Requests= 1 \
Cookie= safetyUIUrl=http://180.97.151.94:9012/safety; Admin-Token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjciLCJ1c2VyR3VpZCI6IjIyNENDNDE3RjI0OTQ3OTBCNUQ1OTYxRDRDNDQ2RDc4IiwiZXhwIjoxNTg1MDYyNDczfQ.3YgnSDeP0-l4OuA8YaFUR5Hv_Qxy5tWHmIwpVgrzPas'
# Origin: http://180.97.151.94:9012 \
# Content-Type: application/json;charset=utf-8 \
# access_token: eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjciLCJ1c2VyR3VpZCI6IjIyNENDNDE3RjI0OTQ3OTBCNUQ1OTYxRDRDNDQ2RDc4IiwiZXhwIjoxNTg1MDYyNDczfQ.3YgnSDeP0-l4OuA8YaFUR5Hv_Qxy5tWHmIwpVgrzPas \

# Content-Length: 242 \
# Referer: http://180.97.151.94:9012/inspectionCheck/checkMethod \

# options.add_argument(argu2)
# options.add_argument("Host= 180.97.151.94:9012")
# options.add_argument("User-Agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0 ")
# options.add_argument("Accept-Language= zh-CN  ")
# options.add_argument("Accept-Encoding= gzip, deflate ")
# options.add_argument("Cookie= safetyUIUrl=http://180.97.151.94:9012/safety; Admin-Token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjciLCJ1c2VyR3VpZCI6IjIyNENDNDE3RjI0OTQ3OTBCNUQ1OTYxRDRDNDQ2RDc4IiwiZXhwIjoxNTg1MDYyNDczfQ.3YgnSDeP0-l4OuA8YaFUR5Hv_Qxy5tWHmIwpVgrzPas")
#


# driver = webdriver.Firefox(firefox_options=options)
# driver.add_cookie(cookie_dict=cookies)

cookies = [{"name": "safetyUIUrl", "value": "http://180.97.151.94:9012/safety;"},
           {"name": "Admin-Token",
            "value": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjciLCJ1c2VyR3VpZCI6IjIyNENDNDE3RjI0OTQ3OTBCNUQ1OTYxRDRDNDQ2RDc4IiwiZXhwIjoxNTg1MDk5NjQ1fQ.ivmQhzJjPlNMJOFnMDpRMItb0GfWELbHiarNGSWPhtw	"}]
# driver.add_cookie(cookie_dict=cookies)

# for d in cookies:
#     driver.add_cookie({
#         # 'domain': '.baidu.com',
#         'name': d['name'],
#         'value': d['value'],
#         # 'path': '/',
#         # 'expires': None
#     })
# driver.get(url)
# print(driver.get_cookies())

from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

headers = {
    "Host": "180.97.151.94:9012",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": 1,
    # "Cookie": "safetyUIUrl=http://180.97.151.94:9012/safety; Admin-Token="
    #           "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjciLCJ1c2VyR3VpZCI6IjIyNENDNDE3RjI0OTQ3OTBCNUQ1OTYxRDRDNDQ2RDc4IiwiZXhwIjoxNTg1MDY0OTQ1fQ.rXKCM_3vLmCkRcMRX84erybfy1u0IymHYvUy2WLhMFk"

}
headers={
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
# "Cookie": "Admin-Token=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6IjciLCJ1c2VyR3VpZCI6IjIyNENDNDE3RjI0OTQ3OTBCNUQ1OTYxRDRDNDQ2RDc4IiwiZXhwIjoxNTg1MDk5NjQ1fQ.ivmQhzJjPlNMJOFnMDpRMItb0GfWELbHiarNGSWPhtw; safetyUIUrl=http://180.97.151.94:9012/safety",
"Host": "180.97.151.94:9012",
"Upgrade-Insecure-Requests": 1,
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}
# cap = DesiredCapabilities.PHANTOMJS.copy()  # 使用copy()防止修改原代码定义dict
# for key, value in headers.items():
#     cap['phantomjs.page.customHeaders.{}'.format(
#         key)] = value
# browser = webdriver.PhantomJS(desired_capabilities=cap, executable_path=r"phantomjs-2.1.1-windows\bin\phantomjs")
# # browser.add_cookie(cookie_dict=cookies)
# for d in cookies:
#     browser.add_cookie({
#         'domain': '.180.97.151.94',
#         'name': d['name'],
#         'value': d['value'],
#         'path': '/',
#         'expires': "Session"
#     })
# browser.get(url)
# print(browser.get_cookies())
# # browser.delete_all_cookies()
# # browser.add_cookie(cookies)
#
# print(browser.page_source)
# # browser.get_screenshot_as_file('01.png')
#
# browser.close()

import  requests
response=requests.get(url,headers)
print(response.text.encode("utf8"))

import json

login_url = 'http://www.xxxxxx.com/wp-login.php'


def get_cookie(account, password):
    s = requests.Session()
    payload = {
        'log': account,
        'pwd': password,
        'rememberme': 'forever',
        'wp-submit': "Log In",
        'redirect_to': 'http://www.xxxxxx.com/wp-admin/',
        'testcookie': '1'
    }
    response = s.post(url, data=payload)
    cookies = response.cookies.get_dict()
    return json.dumps(cookies)


print(get_cookie('xxx', 'xxxxx'))
