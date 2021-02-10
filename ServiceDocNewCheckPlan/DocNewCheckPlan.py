
from sqlalchemy import String, Column
from sqlalchemy import create_engine

from Entity import Entity


class DocNewCheckPlan(Entity):
    __tablename__ = 'z_docnewcheckplan'

    address = Column(String(128))


