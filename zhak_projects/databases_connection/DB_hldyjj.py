from zhak_projects.databases_connection.A_session import get_session,ConnectionDatabase
"""葫芦岛"""
host = "42.56.70.231"
port = "1521"
sid = "orcl"
F_ECHO=False
user_name="hldyjj"
password="Hldyjj_01"


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