import tushare as ts
import matplotlib.pyplot as plt
import numpy as np
token="5f7b1dbf981b2d7dec38abd0b3aa37720b0cf96ddb36e4476680396f"
pro = ts.pro_api(token)#初始化接口
data=pro.index_basic(ts_code='162411')

print(data)