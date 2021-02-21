from Utils.date_utils import mktime


def trans_trade_date(df):
    df["trade_date"]=list(map(mktime, df["trade_date"].tolist()))
