from zhak_projects.databases_connection import DB_wjcase
from sqlalchemy import Column, String, create_engine, Integer, TIMESTAMP, FLOAT, BOOLEAN, CHAR, VARCHAR,distinct
from sqlalchemy.ext.declarative import declarative_base


BaseModel = declarative_base()
class APP_ACCESSORY_FILE(BaseModel):  # 必须继承declaraive_base得到的那个基类
    __tablename__ = "APP_ACCESSORY_FILE"  # 必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
    id = Column(primary_key=True)  # Column类创建一个字段
    version = Column()
    filename = Column()
    modulename = Column()  # nullable就是决定是否not null，unique就是决定是否unique。。这里假定没人重名，设置index可以让系统自动根据这个字段为基础建立索引
    contenttype = Column()
    # leaf = Column()
    # code = Column()
    # name = Column()
    # remark = Column()
session=DB_wjcase.session

def get_filename_modulename_distinct(wsmc):
        result=session.query(APP_ACCESSORY_FILE.filename,APP_ACCESSORY_FILE.modulename).filter(APP_ACCESSORY_FILE.filename.like("%{}%".format(wsmc))).distinct()
        for i in result:
            print(i)
