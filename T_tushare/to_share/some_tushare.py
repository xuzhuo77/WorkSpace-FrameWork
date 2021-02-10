# from zhak_projects.agame.zhgame import actor_list, get_actor_list

# print(get_actor_list())
import tushare as ts
import matplotlib.pyplot as plt
import numpy as np
token="5f7b1dbf981b2d7dec38abd0b3aa37720b0cf96ddb36e4476680396f"
pro = ts.pro_api(token)#初始化接口

df1=pro.daily(ts_code='000001.SZ', start_date='20200101', end_date='20200713')
df2=pro.daily(ts_code='603160.SH', start_date='20200101', end_date='20200713')
_lambda=0.1
df3=(_lambda*df1["high"]+(1-_lambda)*df2["high"])
_lambda=0.3
df4=(_lambda*df1["high"]+(1-_lambda)*df2["high"])
_lambda=0.5
df5=(_lambda*df1["high"]+(1-_lambda)*df2["high"])
_lambda=0.7
df6=(_lambda*df1["high"]+(1-_lambda)*df2["high"])
_lambda=0.9
df7=(_lambda*df1["high"]+(1-_lambda)*df2["high"])
print(df1)
print(df1.columns)
plt.plot(np.linspace(0,1,df1.shape[0]),df1["high"])
plt.plot(np.linspace(0,1,df2.shape[0]),df2["high"])
plt.plot(np.linspace(0,1,df2.shape[0]),df3)
plt.plot(np.linspace(0,1,df2.shape[0]),df4)
plt.plot(np.linspace(0,1,df2.shape[0]),df5)
plt.plot(np.linspace(0,1,df2.shape[0]),df6)
plt.plot(np.linspace(0,1,df2.shape[0]),df7)



# df.plot(x = "trade_date", y = "high")
# df2.plot(x = "trade_date", y = "low")
plt.show()

print(len("sealingUpDistraintDocNumber"))