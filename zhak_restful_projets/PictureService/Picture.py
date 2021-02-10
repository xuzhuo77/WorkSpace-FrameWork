from Entity import Entity
from sqlalchemy import String, Column, Integer
from zhak_projects.databases_connection import DB_xujingtong


class Picture(Entity):
    __tablename__ = 'xu_picture'

    parent_id = Column(Integer, autoincrement=True)
    module_name = Column(String(128))
    type_name = Column(String(128))
    name = Column(String(128))
    local_name = Column(String(128))


# engine = DB_xujingtong.db_engine()
# Picture.metadata.create_all(engine)
