from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine, Integer, TIMESTAMP, FLOAT, BOOLEAN, CHAR, VARCHAR
from sqlalchemy.orm import sessionmaker
import pandas as pd

Base = declarative_base()
host = "60.22.23.216"
port = "31521"
sid = "ykSDB"
F_ECHO=False
def getColumnsFromSql(sql):
    engine = create_engine("oracle://startover:startover@60.22.23.216:31521/yksdb", encoding='utf-8', echo=F_ECHO)
    engine.connect()
    StartOverSession = sessionmaker(bind=engine)
    session = StartOverSession()
    # sql="select column_name from user_tab_columns   where Table_Name='Z_DOC'"
    result=session.execute(sql)
    yield from result

    # wlist = session.query(TableColumns).all()
    # print(wlist)
    # session.rollback()
    # session.commit()
    session.close_all()

if __name__ == '__main__':
    main()
