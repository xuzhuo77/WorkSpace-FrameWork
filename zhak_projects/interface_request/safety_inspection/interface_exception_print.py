import json


# print("\033[1;36m error {} \033[0m".format("Item Empty"))

def myprint(content):
    if not content["success"] or content["code"] == 401:
        print("\033[1;33m error {} \033[0m".format(
            json.dumps(content, ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': '))))
    elif not content["success"] or content["code"] == 500:
        print("\033[1;31m error {} \033[0m".format(
            json.dumps(content, ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': '))))

    else:
        print(json.dumps(content, ensure_ascii=False, sort_keys=True, indent=4, separators=(', ', ': ')))


# myprint({"code":222,"success":3})


class DataWarp():
    def __init__(self, data):
        self.data = data

    def json_loads(self):
        return json.loads(self.data)

    def print(self):
        myprint(self.json_loads())

    def __call__(self):
        return self.data

    def pure(self):
        return self.json_loads()["data"]

    def pure_items(self):
        return self.json_loads()["data"]["items"]

    def payload(self):
        return json.dumps(self.pure())
