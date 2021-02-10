from zhak_projects.databases_connection.A_session import get_session,ConnectionDatabase
"""大洼,盘锦"""
host = "49.4.123.194"
port = "1521"
sid = "zhsafety"
F_ECHO=False
user_name="pjsyjj"
password="pjsyjj_01"

session=None
def db_session():
    database = ConnectionDatabase(host, port, sid, F_ECHO, user_name, password)
    session = get_session(database)
    return session
def execute_sql(sql,value):
    result = session.execute(sql,value)
    print('Successful')
    session.commit()
    session.close_all()


def delete(table):
    session.delete(table)
    session.commit()