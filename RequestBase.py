import json
from flask import request
import functools


def RequestKeyError(func):
    @functools.wraps(func)
    def wrapper(_dict, _cls):
        columns_keys = _cls.__table__.columns
        for key in _dict.keys():
            if key not in columns_keys:
                raise Exception("key [{}] not in {}".format(key, _cls))
        return func(_dict, _cls)

    return wrapper


@RequestKeyError
def json_dict_entity(json_dict, _cls):
    entity = _cls()
    # key_error(json_dict, _cls)
    for key in json_dict.keys():
        setattr(entity, key, json_dict[key])
    return entity


@RequestKeyError
def json_to_query(_dict, _cls):
    query = {getattr(_cls, key, None) == _dict[key] for key in _dict.keys()}
    return query


def RequestBody():
    dict_json = json.loads(request.environ['body_copy'].decode())
    return dict_json


