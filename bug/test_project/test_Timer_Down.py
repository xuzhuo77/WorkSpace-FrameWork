from bug.Timer import Timer2, TimerInterval


import numpy as np
it1=TimerInterval(5)
it2=TimerInterval(2)
timer=Timer2(10)
timer.vec-=3
print(timer.vec)
print()

timer.vec.put(1,20)
timer.vec.put(2,20)

# print(timer.vec)
print(np.minimum(timer.vec,0))
end_index = np.argwhere(timer.vec <=0)[:,0]
rest_ids=[1,2,3,4]
print(end_index)
l_end_index=list(end_index)
# idx=[ l_end_index.index(_id) for _id in rest_ids if _id in l_end_index]
idx=filter(lambda x: if x in rest_ids else l_end_index.index(x),l_end_index  )
print(np.delete(end_index, np.array(idx)))


# timer.start(it1)
# timer.start(it2)
# timer.update()
# timer.update()
# print(it1.is_ready())
# print(it2.is_ready())
# timer.update()
# timer.update()
# print(it1.is_ready())
# print(it2.is_ready())
