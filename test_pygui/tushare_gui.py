from dearpygui.core import *
from dearpygui.simple import *
from database.db_mongo_collection import MongoCollection
from database.db_mongo_utils import dict2dataframe
import time


def mktime(datetime_parm):
    return int(time.mktime(time.strptime(str(datetime_parm),"%Y%m%d")   ))


def lines(result):
    result=dict2dataframe(result)
    dates=list(map(mktime,result["trade_date"].tolist()))
    opens=result["open"].tolist()
    highs=result["high"].tolist()
    lows=result["low"].tolist()
    closes=result["close"].tolist()
    add_plot(result["ts_code"][0], x_axis_name="Day", y_axis_name="USD", height=400, xaxis_time=True)
    add_candle_series(result["ts_code"][0], "GOOGL", dates, opens, highs, lows, closes)




with window("tushare"):
    # daily=pro.daily(ts_code='000001.SZ', start_date='20200101', end_date='20200713')
    #
    #
    # dates=list(map(mktime,daily["trade_date"].tolist()))
    # opens=daily["open"].tolist()
    # highs=daily["high"].tolist()
    # lows=daily["low"].tolist()
    # closes=daily["close"].tolist()
    with MongoCollection("index_basic") as mc:
        result0=mc.select_all('000811.CSI',sort_col="trade_date",sort='asc')
        result1=mc.select_all('h30031.CSI',sort_col="trade_date",sort='asc')
        lines(result0)
        lines(result1)

start_dearpygui()