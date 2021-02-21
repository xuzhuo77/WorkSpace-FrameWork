from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from contextlib import contextmanager
import pandas as pd
from sqlalchemy import and_, or_, not_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String  # 区分大小写
from FirstService.First import First

db_connect_string = 'oracle://startover:startover@60.22.23.216:31521/yksdb'
# db_connect_string = 'oracle://wjcase:wjcase_01@180.97.151.94:9020/zhsafety'

ssl_args = {
    'ssl': {
        'cert': '/home/ssl/client-cert.pem',
        'key': '/home/shouse/ssl/client-key.pem',
        'ca': '/home/shouse/ssl/ca-cert.pem'
    }
}
# engine=create_engine(db_connect_string,connect_args=ssl_args)
engine = create_engine(db_connect_string)
# conn = engine.connect()
# result=conn.execute("SELECT * FROM z_docnewcheckplan")
# print(list(result))
# conn.close()
SessionType=scoped_session(sessionmaker(bind=engine,expire_on_commit=False))
# base = declarative_base()

# class DocNewCheckPlan(base):
#     __tablename__ = 'z_docnewcheckplan'  # 表名
#     id = Column(Integer,primary_key=True)
#     version = Column(Integer)
#     guid = Column(String)
#
# def all(entity):
#     Session = sessionmaker(bind=engine)
#     my_user = SessionType.query(DocNewCheckPlan).all()
#     print(my_user[1].id)
# # print(First.__tablename__)
# # all(First)
#
#
l=SessionType.query(First).all()
print(l)
#
# import json
# from  AlchemyEncoder import AlchemyEncoder
# # print(json.dumps(l[0], cls=AlchemyEncoder))
#
#
# print(l)

