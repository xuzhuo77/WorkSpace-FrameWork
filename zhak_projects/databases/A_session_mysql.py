from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
session=None
class ConnectionDatabase():
    host = "60.22.23.216"
    port = "31521"
    sid = "ykSDB"
    F_ECHO = True
    user_name = "startover"
    password = "startover"

    def __init__(self, host="",
                 port="",
                 sid="",
                 F_ECHO=True,
                 user_name="",
                 password=""):
        self.host = host
        self.port = port
        self.sid = sid
        self.F_ECHO = F_ECHO
        self.user_name = user_name
        self.password = password

def get_session(database):
    url="mysql+pymysql://" + database.user_name + ":" + database.password + "@" + database.host + ":" + database.port + "/" + database.sid
    engine = create_engine(url, encoding='utf-8', echo=database.F_ECHO)
    engine.connect()
    session = sessionmaker(bind=engine)
    return session()

def get_engine(database):
    url="mysql+pymysql://" + database.user_name + ":" + database.password + "@" + database.host + ":" + database.port + "/" + database.sid
    engine = create_engine(url, encoding='utf-8', echo=database.F_ECHO)
    return engine

def execute_sql(sql, value):
    result = session.execute(sql, value)
    print('Successful')
    session.commit()
    session.close_all()


def delete(table):
    session.delete(table)
    session.commit()


