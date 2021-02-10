# 27016
from pymongo import MongoClient

myclient = MongoClient("mongodb://root:root@192.168.51.223:27016/")



mydb = myclient["cycdb2"]
mycol = mydb["c1"]

# 准备要插入的数据
# myname1 = [{"_id": "3", "name": "cyc", "age": "19", "sex": "nan", "ds": ''}, {"_id": "4", "name": "zhq", "age": "20"}]
# 通过insert_mant()插入多条信息
# x = mycol.insert_many(myname1)
x = mycol.find_one()
# print(x.inserted_ids)
print(x)
