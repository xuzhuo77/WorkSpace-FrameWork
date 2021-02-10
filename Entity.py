from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime
from Utils.UniqueIdUtil import gen_guid

base = declarative_base()


class Entity(base):
    __abstract__ = True

    # __tablename__ = "Entity"
    id = Column(Integer, primary_key=True,autoincrement=True)
    version = Column(Integer, nullable=False)
    update_time=Column(DateTime, default=datetime.datetime.now, comment='更新时间')
    # guid =Column(String(64), default=gen_guid(), primary_key=True)
    # delete_flag=Column(Integer)
    # creator=Column(String(64))
    create_date=Column(DateTime, default=datetime.datetime.now, comment='创建时间')

    # def __new__(cls, *args, **kwargs):
    #     print(kwargs)
    # def __init__(self,*args,**kwargs):
    #     for i,k in kwargs:
    # def __dict__(self):
    #     return str({c.name: getattr(self, c.name, None) for c in self.__table__.columns})
