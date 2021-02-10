import datetime
from Entity import Entity
from sqlalchemy import String, Column,DateTime


class Registration(Entity):
    __tablename__ = 'b_registration'

    parentguid = Column(String(64))
    ip=Column(String(64))
    port=Column(String(16))
    module_name = Column(String(128))
    end_date=Column(DateTime, default=datetime.datetime.now, comment='创建时间')




