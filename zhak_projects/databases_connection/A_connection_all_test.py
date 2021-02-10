from zhak_projects.databases_connection import DB_ddqajj, DB_hldyjj, DB_jzyjj_new, DB_lnformal, DB_pjsyjj, DB_startover, \
    DB_SY13010_AJ, DB_sygrid, DB_wjcase
from zhak_projects.databases_connection import DB_startover
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text
a=text("aabb")
print(a)

BaseModel = declarative_base()
class docnewinquiryrecord(BaseModel):
    __tablename__ = "z_docnewinquiryrecord"
    guid = Column()
    id = Column(primary_key=True)


# se=DB_startover.db_session()
# print(se.query(z_doc).all())
databases = [
    # DB_startover,

    # DB_ddqajj,
    # DB_hldyjj,
    # DB_jzyjj_new,
    # DB_lnformal,
    # DB_pjsyjj,
    # DB_SY13010_AJ,
    # DB_sygrid,
    # DB_wjcase,
]


add_column=text("alter table z_docnewinquiryrecord add PARTY_MEMBER VARCHAR2(32)")
for db in databases:
    print(db.user_name)
    session = db.db_session()
    session.execute(add_column)