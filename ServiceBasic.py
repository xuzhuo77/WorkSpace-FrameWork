# from nameko.rpc import rpc
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from database.SqlEngine import oracle_Engine,url_path,mysql_engine

from SingleInstance import SingleInstance
from sqlalchemy.sql import func
from Utils.MapperUtil import mapper_util

from sqlalchemy import and_, or_, not_
# engine=oracle_Engine(url_path["myself"])
from Utils.TransformUtil import TransformUtil
# engine=oracle_Engine(url_path["zhak_startover"])
# session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))

from zhak_projects.databases_connection import  DB_xujingtong

# session=DB_huaian.db_session()
session=DB_xujingtong.db_session()
@SingleInstance
class ServiceBasic:
    __eneity__ = None
    name = "baseic_service"
    def __init__(self, service_name="ServiceBasic"):
        self.service_name = service_name

    def _delete_flag(self):
        return or_(None == self.__eneity__.delete_flag, self.__eneity__.delete_flag == 0)

    def find_by_id(self, id):
        try:
            return session.query(self.__eneity__).filter(self.__eneity__.id == id).one()
        except:
            return None

    def find_by_guid(self, guid=""):
        entity = session.query(self.__eneity__).filter(self.__eneity__.guid == guid).one()
        return entity

    def find_by_ids(self, ids=[]):
        return session.query(self.__eneity__).filter(self.__eneity__.id.in_(ids)).all()
    # @rpc
    def find_list(self, entity_query={}):
        a=session.query(self.__eneity__).filter(*entity_query).all()
        return a

    def find_pagenation(self, entity_query, pagenation):
        return session.query(self.__eneity__).filter(*entity_query, self._delete_flag()).limit(
            pagenation.page_size).offset(
            (pagenation.page_index - 1) * pagenation.page_size).all()

    def create(self, entity):
        entity.version = 1
        session.add(entity)
        session.commit()
        return entity

    def create_batch(self, entities):
        for entity in entities:
            entity.version = 1
        session.add_all(entities)
        session.commit()

    def find_id_max(self):
        qry = session.query(func.max(self.__eneity__.id)).one();
        return qry[0]

    def find_one(self, entity_query={}):
        try:
            return session.query(self.__eneity__).filter(*entity_query).one()
        except:
            return None

    def update(self, entity):
        if entity.version is None:
            entity.version = 0
        query = {
            self.__eneity__.id == entity.id,
            self.__eneity__.version == entity.version,
            # self.__eneity__.deleteflag!=1
        }
        result = self.find_one(query)
        if result is not None:
            mapper_util(entity, result)
            result.version += 1
            session.commit()
            return result
        else:
            return None

    def save(self, entity):
        pass

    def delete_by_id(self, id):
        session.query(self.__eneity__).filter(self.__eneity__.id == id).delete(synchronize_session=False)
        session.commit()
        return None

    def delete_by_ids(self, ids):
        session.query(self.__eneity__).filter(self.__eneity__.id.in_(ids)).delete(synchronize_session=False)
        session.commit()
        return 1

    def delete_by_guid(self, guid):
        session.query(self.__eneity__).filter(self.__eneity__.guid == guid).delete(synchronize_session=False)
        session.commit()
        return 1

    def delete_by_entity(self, entity):
        session.query(self.__eneity__).filter(*entity).delete(synchronize_session=False)
        session.commit()
        return 1

    def remove_by_id(self, id):
        res = session.query(self.__eneity__).filter(self.__eneity__.id == id).update({"deleteflag": 1},
                                                                                     synchronize_session=False)
        session.commit()
        return 1

    def remove_by_ids(self, ids):
        session.query(self.__eneity__).filter(self.__eneity__.id.in_(ids)).update({"deleteflag": 1},
                                                                                  synchronize_session=False)
        session.commit()
        return 1

    def remove_by_entity(self, entity_query):
        session.query(self.__eneity__).filter(*entity_query).update({"deleteflag": 1}, synchronize_session=False)
        session.commit()
        return 1

    def remove_by_guid(self, guid):
        session.query(self.__eneity__).filter(self.__eneity__.guid == guid).delete(synchronize_session=False)
        session.commit()
        return 1

    @classmethod
    def joinQuery_by_dict(self, query, query_condition):
        return session.query(*query).join(*query_condition).all()

    def joinQuery_by_entity(self, other_entity, query_condition={}):
        return session.query(self.__eneity__, other_entity).filter(*query_condition).all()

    # @classmethod
    def outerjoin(self, result={}, outerjoin={}, filter={}):
        return session.query(*result).outerjoin(*outerjoin).filter(*filter).all()

