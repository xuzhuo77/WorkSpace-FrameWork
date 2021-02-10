from FirstService.First import First
from FirstService.FirstService import FirstService
# from Application import app
from flask import Blueprint
from flask import request

from Pagenation import Pagenation
from RequestBase import RequestBody, json_dict_entity, json_to_query
from Utils.ReturnUtil import ReturnUtil

firstController = Blueprint("first", __name__)
first_service = FirstService()


@firstController.route('/find_by_id', methods=['GET'])
def find_by_id():
    id = request.args.get("id")  # 获取  get  参数
    entity = first_service.find_by_id(id)
    return ReturnUtil().ok(entity);


@firstController.route('/find_by_ids', methods=["POST"])
def find_by_ids():
    entity_list = first_service.find_by_ids([1218444021506121730, 1209285449480388610])
    print(entity_list[0].id, entity_list[1].id)
    return ""


@firstController.route('/list', methods=["POST"])
def find_list():
    dict_json = RequestBody()
    query = json_to_query(dict_json, First)
    entity_list = first_service.find_pagenation(query, Pagenation())
    return ReturnUtil().ok(entity_list);


@firstController.route('/create', methods=["POST"])
def create():
    dict_json = RequestBody()
    entity = json_dict_entity(dict_json, First)
    entity = first_service.create(entity)
    return ReturnUtil().ok(entity);


@firstController.route('/createBatch', methods=["POST"])
def createBatch():
    json_dict = RequestBody()
    entities = [json_dict_entity(entity, First) for entity in json_dict]
    FirstService().create_batch(entities)
    return ReturnUtil().ok();


@firstController.route('/save', methods=["POST"])
def save():
    json_dict = RequestBody()
    entity = json_dict_entity(json_dict, First)
    entity = FirstService().update(entity)
    if entity is not None:
        return ReturnUtil().ok(entity);
    else:
        return ReturnUtil().falid()


@firstController.route('/delete_by_id', methods=["POST"])
def delete_by_id():
    json_dict = RequestBody()
    entity = json_dict_entity(json_dict, First)
    entity = first_service.delete_by_id(id)
    if entity is not None:
        return ReturnUtil().ok(entity);
    else:
        return ReturnUtil().falid()


@firstController.route('/delete_by_guid', methods=["POST"])
def delete_by_guid():
    json_dict = RequestBody()
    entity = json_dict_entity(json_dict, First)
    entity = first_service.delete_by_guid(guid)
    if entity is not None:
        return ReturnUtil().ok(entity);
    else:
        return ReturnUtil().falid()


@firstController.route('/remove_by_id', methods=["POST"])
def remove_by_id():
    json_dict = RequestBody()
    entity = json_dict_entity(json_dict, First)
    entity = first_service.delete_by_guid(guid)
    if entity is not None:
        return ReturnUtil().ok(entity);
    else:
        return ReturnUtil().falid()


@firstController.route('/remove_by_guid', methods=["POST"])
def remover_by_id():
    json_dict = RequestBody()
    entity = json_dict_entity(json_dict, First)
    entity = first_service.delete_by_guid(guid)
    if entity is not None:
        return ReturnUtil().ok(entity);
    else:
        return ReturnUtil().falid()


@firstController.route('/prove', methods=["get"])
def prove():
    # 证明单例的有效性
    first_service = FirstService()
    f2=FirstService()
    f3=FirstService()

    print(first_service.find_list())
    from super_init_wrapper import instance
    return str(instance)
