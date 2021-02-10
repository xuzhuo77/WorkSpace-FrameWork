import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from Utils.TransformUtil import TransformUtil


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:  # 添加了对datetime的处理
                    fields[field] = TransformUtil.jsonable(data)

            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


def to_dict(entity):
    return json.dumps(entity, cls=AlchemyEncoder)

