import tushare as ts
import json
import pandas as pd

from database.db_mongodb import collection_tushare, db_tushare

token = "5f7b1dbf981b2d7dec38abd0b3aa37720b0cf96ddb36e4476680396f"
pro = ts.pro_api(token)
"""
['ts_code', 'trade_date', 'open', 'high', 'low', 'close', 'pre_close',
 'change', 'pct_chg', 'vol', 'amount']
"""

"""
    reference:
    https://blog.csdn.net/yutian1320789/article/details/101536830
"""


df1 = pro.daily(ts_code='000001.SZ', start_date='20200101', end_date='20200713')

ZhangTing_df = df1[(df1["change"]>9.5) & (df1["change"]<10.5) ]
print(ZhangTing_df.head())

# print(df1["ts_code"][0])
def insert(df):
    collection = db_tushare[df["ts_code"][0]]
    collection.insert_many(json.loads(df.T.to_json()).values())



# for x in db_tushare["000001.SZ"].find():
#     print(x["low"])
# closes = [x["close"] for x in db_tushare["000001.SZ"].find()]


def MA(tsPrice, k):  # MovingAverage计算
    Sma = pd.Series(0.0, index=tsPrice.index)
    for i in range(k - 1, len(tsPrice)):
        Sma[i] = sum(tsPrice[(i - k + 1):(i + 1)]) / k
    return (Sma)


def MA_5_10_30(df):
    d5 = MA(df.close, 5)
    d10 = MA(df.close, 10)
    d30 = MA(df.close, 30)
    df['d5'] = pd.DataFrame({'d5': d5})
    df['d10'] = pd.DataFrame({'d10': d10})
    df['d30'] = pd.DataFrame({'d30': d30})
    return df

# collection = db_tushare[df1["ts_code"][0]]
# collection.drop()
# update_df=MA_5_10_30(df1)
# collection.insert_many(json.loads(update_df.T.to_json()).values())
collection = db_tushare[df1["ts_code"][0]]
for x in collection.find().limit(3).skip(2):
    print(x)
