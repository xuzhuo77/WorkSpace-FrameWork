from FakeDataService.FakeData import FakeData
from FakeDataService.FakeDataService import FakeDataService
from FirstService.First import First
from FirstService.FirstService import FirstService
tid=2000123223
# param=[tid]
# entity=First()
# setattr(entity,"id",tid)

# FirstService().create(entity)
# test=FirstService().find_by_id(tid)
# print(test.id,test.id==tid)

# d=FirstService().delete_by_id(tid)
# print(d.id,d.id==tid)

# d=FirstService().delete_by_ids([tid])
# print(d.id,d.id==tid)

# d=FirstService().find_list({First.id==tid})
# d=FirstService().find_by_ids([tid])
# FirstService().remover_by_id(tid)
# d=FirstService().find_id_max()

# print(d)


# FakeDataService().create(FakeData(classname="First",entityguid='4c1272dcc8724ce6a941e297106dd010'))
# query_dict={
#     FakeData.id,
#     First.id
# }
# query_condition={
#     First,
#     FakeData.entityguid==First.guid
#
# }
# d=FakeDataService().joinQuery_by_dict(query_dict,query_condition)
# print(d)
query_condition={
    # First.id,
    First.guid==FakeData.entityguid,
    First.guid=="4c1272dcc8724ce6a941e297106dd010"
}

d=FakeDataService().joinQuery_by_entity(First,query_condition)

for t in d:
    print(t)

# result={
#     FakeData.entityguid,
#     FakeData.id,
#     First.id
#
# }
# outerjoin={First,FakeData.entityguid==First.guid}
# filter={FakeData.id==9}
# print(FakeDataService().outerjoin(result,outerjoin,filter))