# coding:utf-8
import yaml
# 直接打开读出来
f = open(r'D:\WorkSpace-FrameWork\Configuration\DatabaseConfig.yaml','r',encoding='utf-8')
result = f.read()
# 转换成字典读出来
raw=yaml.load(result, Loader=yaml.FullLoader)
print(raw)
db_connect_string_raw=raw["database_type"]+"://"+raw["auth"]["username"]+raw["auth"]["password"]+"@"+\
                      raw["address"]["ip"]+":"+str(raw["address"]["port"])+"/"+raw["database"]+"?charset="+raw["charset"]


db_connect_string = 'mysql+pymysql://startover:startover@111.229.148.2:3306/gameserver?charset=utf8'
assert  db_connect_string==db_connect_string
