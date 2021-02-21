import json

from T_tushare.tushare_config import pro
from database.db_mongodb import mongodb

df = pro.index_basic(market='MSCI')
# print(df.columns.values)
"""
['ts_code' 'name' 'market' 'publisher' 'category' 'base_date' 'base_point'
 'list_date']
"""
table=mongodb["index_basic"]
collection=table["index_basic"]
# collection.insert_many(json.loads(df.T.to_json()).values())

result=collection.find()
for x in result:
    print(x)