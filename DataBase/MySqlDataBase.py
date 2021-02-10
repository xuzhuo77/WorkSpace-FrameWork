import uuid
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from FirstService.FirstService import FirstService
from Pagenation import Pagenation
from Utils.ReturnUtil import ReturnUtil

engine = create_engine('mysql+pymysql://startover:startover@111.229.148.2:3306/gameserver?charset=utf8', echo=True)

Base = declarative_base()


def gen_id():
    return uuid.uuid4().hex


class Student(Base):  # 必须继承declaraive_base得到的那个基类
    __tablename__ = "Students"  # 必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
    id = Column(Integer, primary_key=True, autoincrement=True)  # Column类创建一个字段
    guid = Column(String(32), default=gen_id(), primary_key=True)
    Sname = Column(String(20), nullable=False,
                   index=True)  # nullable就是决定是否not null，unique就是决定是否unique。。这里假定没人重名，设置index可以让系统自动根据这个字段为基础建立索引
    Ssex = Column(String(20), nullable=False)
    Sage = Column(Integer, nullable=False)
    Sdept = Column(String(20))

    def __repr__(self):
        return "<Student>{}:{}".format(self.Sname, self.id)


if __name__ == '__main__':
    # Student.metadata.drop_all(engine)
    #
    # Student.metadata.create_all(engine)

    # session=Session()
    # st=Student(Sname="中文名字",Ssex="女",Sage=4,Sdept="3")
    # print(st)
    # session.add(st)
    # session.commit()
    # session.close()
    #
    # session=Session()
    # st=Student(Sname="中文名字",Ssex="女",Sage=2,Sdept="3")
    # session.add(st)
    # session.commit()
    # session.close()
    #
    # session=Session()
    # list=session.query(Student).all()
    # print(list)
    # session.commit()

    # page_size = 2
    # page_index = 1
    # Session = sessionmaker(bind=engine)
    # session = Session()
    # entity_query={
    #     First.id==988014
    # }
    # x=session.query(First).filter(*entity_query).limit(page_size).offset((page_index-1)*page_size).all()
    # print(x)
    # entity_query={}
    # print(session.query(First).filter(*entity_query).all())
    # session.close()
    # entity_query={}

    # print(FirstService().find_by_id(988014))

    query = {}
    entity_list = FirstService().find_pagenation(query, Pagenation())
    print(ReturnUtil().ok(entity_list))
