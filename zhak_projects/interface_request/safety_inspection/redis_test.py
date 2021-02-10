import redis

import struct

r = redis.Redis(host='192.168.51.223', password="guofeng+0" ,port=6379)
print(r)
import  numpy as np
a=np.ones((2,3))
h,w=a.shape
shape = struct.pack('>II',h,w)
print(shape)
encode=shape+a.tobytes()
print(encode)

r.set("numpy",encode)
encoded=r.get("numpy")
print(encoded)
h,w=struct.unpack('>II',encoded[:8])
print(h,w)
a=np.frombuffer(encoded,offset=8).reshape(h,w)
print(a)


# print(r.get("22"))
r.hset("hash1", "k1", "v1")
r.hset("hash1", "k2", "v224")
print(r.hkeys("hash1"))
print(r.hget("hash1", "k2"))    # 单个取hash的key对应的值
print(r.hmget("hash1", "k1", "k2")) # 多个取hash的key对应的值
