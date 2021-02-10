from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Table, MetaData
from ServiceBasic import ServiceBasic
from super_init_wrapper import super_init_wrapper


def mysql():
    # engine, suppose it has two tables 'user' and 'address' set up
    engine = create_engine('mysql+pymysql://startover:startover@111.229.148.2:3306/gameserver?charset=utf8')
    # engine = create_engine('oracle://startover:startover@60.22.23.216:31521/yksdb',echo=True)

    # reflect the tables
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Base.classes.keys()  # 获取所有的对象名

    # mapped classes are now created with names by default
    # matching that of the table name.
    DocNewCheckPlan = Base.classes.z_docnewcheckplan
    # Address = Base.classes.address

    Session = sessionmaker(bind=engine)
    session = Session()

    # print(DocNewCheckPlan.__table__.columns.keys())
    print(session.query(DocNewCheckPlan).all())
    # session.close()


def oracle():
    metadata = MetaData()
    engine = create_engine(
        'oracle://startover:startover@60.22.23.216:31521/yksdb',
        echo=True)
    # 反射数据库单表
    DocNewCheckPlan = Table('z_docnewjaspb', metadata, autoload=True, autoload_with=engine)

    '''反射数据库所有的表
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Admin = Base.classes.admin
    '''
    keys = DocNewCheckPlan.columns.keys()
    # print(1,DocNewCheckPlan.c.keys())

    # Base = automap_base()
    # Base.prepare(engine, reflect=True)
    # DocNewCheckPlan = Base.classes.z_docnewcheckplan
    Session = sessionmaker(bind=engine)

    session = Session()
    res = session.query(DocNewCheckPlan).all()
    print(res)
    # for k in keys:
    #     print(k)
    #
    #     # print(res)

    # print(res.id, res.account_text)


# oracle()
def oracel_d_blockpdf():
    from sqlalchemy import create_engine, Table, MetaData
    from sqlalchemy.orm import Session
    metadata = MetaData()
    engine = create_engine(
        'oracle://wjcase:wjcase_01@180.97.151.94:9020/zhsafety',
        # echo=True
    )
    # 反射数据库单表
    Blockpdf = Table('d_blockpdf', metadata, autoload=True, autoload_with=engine)
    print(dir(Blockpdf))
    '''反射数据库所有的表
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Admin = Base.classes.admin
    '''
    keys = Blockpdf.columns.keys()
    print(1, Blockpdf.c.keys())

    # Base = automap_base()
    # Base.prepare(engine, reflect=True)
    # DocNewCheckPlan = Base.classes.z_docnewcheckplan
    Session = sessionmaker(bind=engine)

    session = Session()
    res = session.query(Blockpdf).filter_by(doctype='DocRegistCaseAudit').all()
    print(res)


# oracel_d_blockpdf()

def oracle_map(metadata, engine, table_name):
    from sqlalchemy.orm import Session
    # 反射数据库单表
    return Table(table_name, metadata, autoload=True, autoload_with=engine)


def generateMappedEneity(engine, table_name):
    metadata = MetaData()
    mapped_entity = oracle_map(metadata, engine, table_name)
    return mapped_entity


def generateService(entity):
    @super_init_wrapper
    class ShellService(ServiceBasic):
        if not hasattr(entity, "deleteflage"):
            setattr(entity, "deleteflag", None)
        __eneity__ = entity

    return ShellService


if __name__ == '__main__':
    engine = create_engine(
        'oracle://wjcase:wjcase_01@180.97.151.94:9020/zhsafety',
        # echo=True
    )
    table_name = "z_docregistcaseaudit"
    mapped_eneity = generateMappedEneity(engine, table_name)
    keys = mapped_eneity.columns.keys()
    print(1, mapped_eneity.c.keys())
    list = generateService(mapped_eneity)().find_list()
    print(list)
