
from zhak_projects.databases.A_session_mysql import ConnectionDatabase, get_session



host = "49.4.6.132"
port = "33061"
sid = "sas_huaian_dev"
F_ECHO=False
user_name="root"
password="Zhonghang_01"


session=None
def db_session():
    database = ConnectionDatabase(host, port, sid, F_ECHO, user_name, password)
    session = get_session(database)
    return session
def execute_sql(sql,value):
    result = session.execute(sql,value)
    print('Successful')
    print(list(result))
    session.commit()
    session.close_all()


def delete(table):
    session.delete(table)
    session.commit()


# session=db_session()
# execute_sql("select * from s_dictionary",{})

