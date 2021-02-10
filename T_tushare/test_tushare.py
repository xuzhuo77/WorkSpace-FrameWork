import tushare as ts
df = ts.get_k_data(code='600000', start='2020-01-01', end='2020-04-02')
print(df)


print(df["volume"])