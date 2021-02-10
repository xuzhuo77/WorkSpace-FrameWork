import redis

pool = redis.ConnectionPool(host='129.211.61.116',port=60379, decode_responses=True,password='xuzhuo77!')
r = redis.Redis(connection_pool=pool)
# r.set('food', 'mutton')    # key是"food" value是"mutton" 将键值对存入redis缓存
print(r.get('food'))  # mutton 取出键food对应的值

