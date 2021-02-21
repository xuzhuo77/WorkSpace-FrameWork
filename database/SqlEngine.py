from sqlalchemy import create_engine


def mysql_engine(url_path, echo=False):
    url = "mysql+pymysql://" + url_path + "?charset=utf8"
    return create_engine(url, echo=echo)


def oracle_Engine(url_path, echo=False):
    url = "oracle://" + url_path 
    return create_engine(url, echo=echo)


# MySqlEngine = create_engine('mysql+pymysql://startover:startover@111.229.148.2:3306/gameserver?charset=utf8', echo=True)
#
# OracleEngind = create_engine('oracle://startover:startover@60.22.23.216:31521/yksdb', echo=True)

url_path={
    "myself":"startover:startover@111.229.148.2:3306/gameserver",
    "zhak_startover":"startover:startover@60.22.23.216:31521/yksdb",
    "zhak_wujiang":"wjcase:wjcase_01@180.97.151.94:9020/zhsafety"
}
