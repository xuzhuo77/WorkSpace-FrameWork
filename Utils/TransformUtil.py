import datetime
import decimal
class TransformUtil:
    def assemble(self, _list, _cls):
        pass

    def to_dict(self, _cls):
        return {key.name: getattr(_cls, key.name, None) for key in _cls.__table__.columns}

    @classmethod
    def jsonable(self,data):
        if isinstance(data, datetime.datetime):
            data= data.isoformat()
        elif isinstance(data, datetime.date):
            data= data.isoformat()
        elif isinstance(data, datetime.timedelta):
            data = (datetime.datetime.min + data).time().isoformat()
        elif isinstance(data, decimal.Decimal):
            data= float(data)
        elif isinstance(data, dict):
            inst = Dict()
            for k, v in data.items():
                inst[k] = self.jsonable(v)
            data=inst
        elif isinstance(data, list) or isinstance(data,tuple):
            l = []
            for v in data:
                if isinstance(v, decimal.Decimal):
                    v = float(v)
                l.append(v)
            data=l
        elif isinstance(data, bytes):
            data=str(data, encoding='utf-8')
        else:
            data = None
        return  data


class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__

# print(TransformUtil.jsonable({"ba":[{"data":3}]}))