from zhak_projects.databases_connection import  DB_SY13010_AJ
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base

mapper = {
    "guid": "guid",
    "deleteflag": "deleteflag",
    "lastchanger": "lastchanger",
    "systemversion": "systemversion",
    "lastchangeddate": "lastchangeddate",
    "creator": "creator",
    "createdate": "createdate",
    "version": "version",
    "tbrid": "fillingperson",
    "jcajid": "checkingcaseid",
    "dsrjbqk": "litigantsituation",
    "lasj": "casedate",
    "ajbh": "casenumber",
    "zfkdz": "ensectionstation",
    "wsdate": "documentdate",
    "wsbh": "documentnum",
    "cbryj": "undertakeropinion",
    "cbrq": "undertakedate",
    "ajqk": "casesituation",
    "yzbm": "postalcode",
    "dz": "address",
    "ajmc": "casename",
    "jcsj": "inspectiondate",
    "ajly": "caseorigin",
    "ay": "casereason",
    "dsr": "litigant",
    "dh": "litigantphone",
    "fddbr": "legalperson",
    "zfry": "marshalstried",
    "zfzh": "enforcementnum",
    "zfryid": "marshalstriedguid",
    "no": "documentserialnum",
    "wszl": "documenttype",
    "ajbmid": "safetysupdepid",
    "id": "id",
}
BaseModel = declarative_base()


class z_docregistcaseaudit(BaseModel):
    __tablename__ = "z_docregistcaseaudit"
    guid = Column()
    deleteflag = Column()
    lastchanger = Column()
    systemversion = Column()
    lastchangeddate = Column()
    creator = Column()
    createdate = Column()
    version = Column()
    fillingperson = Column()
    checkingcaseid = Column()
    litigantsituation = Column()
    casedate = Column()
    casenumber = Column()
    ensectionstation = Column()
    documentdate = Column()
    documentnum = Column()
    undertakeropinion = Column()
    undertakedate = Column()
    casesituation = Column()
    postalcode = Column()
    address = Column()
    casename = Column()
    inspectiondate = Column()
    caseorigin = Column()
    casereason = Column()
    litigant = Column()
    litigantphone = Column()
    legalperson = Column()
    marshalstried = Column()
    enforcementnum = Column()
    marshalstriedguid = Column()
    documentserialnum = Column()
    documenttype = Column()
    safetysupdepid = Column()
    id = Column(primary_key=True)


class z_doc_registcaseaudit(BaseModel):
    __tablename__ = "z_doc_registcaseaudit"
    guid = Column()
    deleteflag = Column()
    lastchanger = Column()
    systemversion = Column()
    lastchangeddate = Column()
    creator = Column()
    createdate = Column()
    version = Column()
    tbrid = Column()
    jcajid = Column()
    dsrjbqk = Column()
    lasj = Column()
    ajbh = Column()
    zfkdz = Column()
    wsdate = Column()
    wsbh = Column()
    cbryj = Column()
    cbrq = Column()
    ajqk = Column()
    yzbm = Column()
    dz = Column()
    ajmc = Column()
    jcsj = Column()
    ajly = Column()
    ay = Column()
    dsr = Column()
    dh = Column()
    fddbr = Column()
    zfry = Column()
    zfzh = Column()
    zfryid = Column()
    no = Column()
    wszl = Column()
    ajbmid = Column()
    id = Column(primary_key=True)


# session_sygrid=DB_sygrid.db_session()
session_SY13010_AJ=DB_SY13010_AJ.db_session()

# session_startover = DB_startover.db_session()
#
# for t in session_startover.query(z_docregistcaseaudit).all():
#     print(t)
# print(session_sygrid.query(z_docregistcaseaudit))
# for t in session_SY13010_AJ.query(z_doc_registcaseaudit).all():
#     print(t)
all_data=[]
for t in session_SY13010_AJ.query(z_doc_registcaseaudit).all():
    k=t.__dict__
    k.pop("_sa_instance_state")
    values={mapper[k]:v for k,v in t.__dict__.items()}
    values["systemversion"]=1006
    docregist=z_docregistcaseaudit(**values)
    all_data.append(docregist)
    print(docregist)
#
# session_sygrid.add_all(all_data)
# session_sygrid.commit()
# ins=z_docregistcaseaudit.__table__.insert()
#
# print(ins)
# ins.values()
