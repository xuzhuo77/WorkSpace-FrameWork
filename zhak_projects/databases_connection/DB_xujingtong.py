from zhak_projects.databases.A_session_mysql import ConnectionDatabase, get_session, get_engine

host = "129.211.61.116"
port = "3306"
sid = "xujingtong"
F_ECHO = False
user_name = "xujingtong"
password = "xujingtong"

session = None


def db_session():
    database = ConnectionDatabase(host, port, sid, F_ECHO, user_name, password)
    session = get_session(database)
    return session


def db_engine():
    database = ConnectionDatabase(host, port, sid, F_ECHO, user_name, password)
    return get_engine(database)


def execute_sql(sql, value):
    result = session.execute(sql, value)
    print('Successful')
    print(list(result))
    session.commit()
    session.close_all()


def delete(table):
    session.delete(table)
    session.commit()

# session=db_session()
# execute_sql("select * from x_tushare",{})
