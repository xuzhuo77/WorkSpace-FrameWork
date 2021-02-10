from Entity import Entity
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class FakeData(Entity):
    __tablename__ = 'f_fakedata'

    parentguid = Column(String(64))
    modulename = Column(String(128))
    # columnkeys = Column(String(4000))
    content_value = Column(String(4000))
    classname = Column(String(64))
    database_url=Column(String(256))
    table_name=Column(String(64))

