# https://faker.readthedocs.io/en/master/
# https://www.jb51.net/article/175348.htm
from faker import Faker
from sqlalchemy import Integer, String, DateTime,Table

from Entity import Entity
from FirstService.First import First
from Utils.UniqueIdUtil import gen_guid


def generateFakeEntity(table_name):
    class FakeEntityCls(Entity):
        __tablename__ = table_name
    return FakeEntityCls



#
# fake = Faker()
# fake = Faker("zh_CN")
# print(fake.text(max_nb_chars=200))


class FakerUtil:

    def __init__(self, country="zh_CN", seed=None):
        self.fake = Faker(country)
        Faker.seed(seed)
        self._default = {}

    def entity_fake_data(self, _cls):
        if isinstance(_cls,Table):
            colums=_cls.columns
            _cls=generateFakeEntity(_cls)()

        else:
            colums=_cls.__table__.columns

        for k in colums:
            if isinstance(k.type, Integer):
                int_value = self._integer_value(k.name)
                setattr(_cls, k.name, int_value)
            if isinstance(k.type, String):
                str_value = self._string_value(k.name)

                setattr(_cls, k.name, str_value)
            if isinstance(k.type, DateTime):
                datetime_value = self._dateime_value(k.name)
                setattr(_cls, k.name, datetime_value)

        return _cls

    def _integer_value(self, key_name):
        int_value = None
        self._default["version"] = 1
        try:
            value = self._default[key_name]
            return value
        except:
            v = int(self.fake.random_int())
            return v

    def _string_value(self, key_name):
        str = None
        self._default["guid"] = gen_guid()
        self._default["deleteflag"] = None
        self._default["creator"] = self.fake.name()
        # self._default["address"] = self.fake.address()

        try:
            value = self._default[key_name]
            return value
        except:
            return self.fake.job()

    def _dateime_value(self, key_name):
        datetime_value = None
        self._default["createdate"] = self.fake.date(pattern='%Y-%m-%d', end_datetime=None)

        # datetime_value=fake.date_between(start_date='-30d', end_date='today')
        try:
            value = self._default[key_name]
            return value
        except:
            return None

    def profile(self):

        return self.fake.profile(fields=None, sex=None)


# first = FakerUtil().entity_fake_data(First)
# print()
# print(TransformUtil().to_dict(first))

# print(FakerUtil().profile())
