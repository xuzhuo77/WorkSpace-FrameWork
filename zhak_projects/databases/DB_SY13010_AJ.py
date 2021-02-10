from zhak_projects.databases.A_session import get_session,ConnectionDatabase

host = "124.95.131.16"
port = "12001"
sid = "orcl"
F_ECHO=False
user_name="syajj"
password="Syyjj_01"

database = ConnectionDatabase(host,port,sid,F_ECHO,user_name,password)
session=get_session(database)
def execute_sql(sql,value):
    result = session.execute(sql,value)
    print('Successful')
    session.commit()
    session.close_all()
def db_session():
    return session

def delete(table):
    session.delete(table)
    session.commit()