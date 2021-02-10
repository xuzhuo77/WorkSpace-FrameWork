import requests
import yaml
import sys
ACCESS_FILE_NAME='access_file.yaml'
path="E:\\pythonWebWorkSpace\\zhak_projects\\interface_request\\"
localhost='http://localhost:9030/'
liaoningsheng='http://218.60.145.28:8080/'
wujiang='http://180.97.151.94:9020/'

IP_PORT=localhost
IP_PORT=wujiang
# IP_PORT=liaoningsheng

def read_default():
    with open(path+ACCESS_FILE_NAME, "r") as rf:
        content = yaml.load(rf.read(), Loader=yaml.FullLoader)
        return content


def write_default(data={}):
    with open(ACCESS_FILE_NAME, "r") as rf:
        content = yaml.load(rf.read(), Loader=yaml.FullLoader)
        # [for d in data]
        content.update(data)
        with  open("access_file.yaml", "w") as wf:
            yaml_obj = yaml.dump(content, wf)

loginSafetyValidate="safety/auth/loginSafetyValidate"
# loginSafetyValidate="safety/auth/verify"
url=IP_PORT+loginSafetyValidate


payload = "{\n    \"username\": \"zhadmin\",\n    \"password\": \"WE@3dfsa\"\n}"
# payload = "{\n    \"username\": \"admin\",\n    \"password\": \"WE@3dfsa\"\n}"
# payload = "{\n    \"username\": \"yhqadmin\",\n    \"password\": \"WE@3dfsa\"\n}"
# payload = "{\n    \"username\": \"zhadmin\",\n    \"password\": \"WE@3dfsa\"\n}"
headers = {
    'Content-Type': 'application/json'
}

def get_IP_PORT():
    return IP_PORT


import json
def set_token():
  response = requests.request("POST", url, headers=headers, data=payload)
  print(json.loads(response.text.encode('utf8')))
  data = json.loads(response.text.encode('utf8'))["data"]
  write_default(data)


def get_headers():
    return {
        'Content-Type': 'application/json',
        'access_token': read_default()["token"]
    }


if __name__ == '__main__':
    set_token()