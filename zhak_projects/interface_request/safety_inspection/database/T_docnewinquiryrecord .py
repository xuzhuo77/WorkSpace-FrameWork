from zhak_projects.databases_connection import DB_SY13010_AJ, DB_sygrid
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base

mapper = {
    "guid": "guid",
    "inquiryInformation": "jlxx",

    "id": "id",
}
BaseModel = declarative_base()


class Z_docnewinquiryrecord(BaseModel):
    __tablename__ = "z_docnewinquiryrecord"
    guid = Column()
    inquiryinformation=Column()
    id = Column(primary_key=True)


class z_docnewxwbl(BaseModel):
    __tablename__ = "z_docnewxwbl"
    guid = Column()
    jlxx=Column()
    id = Column(primary_key=True)


session_sygrid=DB_sygrid.db_session()
session_SY13010_AJ = DB_SY13010_AJ.db_session()
[]
old_data=[(old.guid,old.jlxx) for old in session_SY13010_AJ.query(z_docnewxwbl).all()]
print(old_data)
for guid,jlxx in old_data:
    session_sygrid.query(Z_docnewinquiryrecord).filter(Z_docnewinquiryrecord.guid==guid).update({"inquiryinformation":jlxx})

session_sygrid.commit()

# session_startover = DB_startover.db_session()
#
# for t in session_startover.query(z_docregistcaseaudit).all():
#     print(t)
# print(session_sygrid.query(z_docregistcaseaudit))
# for t in session_SY13010_AJ.query(z_doc_registcaseaudit).all():
#     print(t)
# all_data = []
# for t in session_SY13010_AJ.query(z_doc_registcaseaudit).all():
#     k = t.__dict__
#     k.pop("_sa_instance_state")
#     values = {mapper[k]: v for k, v in t.__dict__.items()}
#     values["systemversion"] = 1006
#     docregist = z_docregistcaseaudit(**values)
#     all_data.append(docregist)
#     print(docregist)
#
# session_sygrid.add_all(all_data)
# session_sygrid.commit()
# ins=z_docregistcaseaudit.__table__.insert()
#
# print(ins)
# ins.values()
