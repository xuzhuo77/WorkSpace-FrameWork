from Entity import Entity
from sqlalchemy import String, Column
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://startover:startover@111.229.148.2:3306/gameserver?charset=utf8', echo=False)

class First(Entity):
    __tablename__ = 'z_docnewcheckplan'

    # Entity.__table__.name= 'z_docnewcheckplan'
    address = Column(String(128))

# First.metadata.drop_all(engine)
#
# First.metadata.create_all(engine)

