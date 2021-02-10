from zhak_projects.databases_connection.A_session import get_session,ConnectionDatabase

host = "60.22.23.216"
port = "31521"
sid = "yksdb"
F_ECHO = False
user_name = "startover"
password = "startover"
session=None
def db_session():
    database = ConnectionDatabase(host, port, sid, F_ECHO, user_name, password)
    session = get_session(database)
    return session
