import numpy as np

from SingleInstance import SingleInstance


@SingleInstance
class MoveAll():
    _action_dict = {0: 0}
    _positions = np.array([[0, 0, 0]])
    _velocity = np.array([[0, 0, 0]])
    _remove_ids = []

    def __init__(self):
        pass

    def update(self):
        self._positions = np.add(self._positions, self._velocity)

    def regist(self, action):
        if len(self._remove_ids) > 0:
            id = self._remove_ids.pop()
            self._action_dict[action] = id
            self._positions[id] = np.array(action.pos)
            self._velocity[id] = np.array(action.v)

        else:
            self._action_dict[action] = len(self._action_dict)
            self._positions = np.vstack((self._positions, np.array(action.pos)))
            self._velocity = np.vstack((self._velocity, np.array(action.v)))

    def de_regist(self, action):
        id = self._action_dict[action]
        self._remove_ids.append(id)
        self._action_dict.pop(action)

    def get_pos(self, action):
        id = self._action_dict[action]
        return self._positions[id]


#
# pos = [[1, 2, 3],
#        [2, 3, 4]]
# v = [[2, 3, 4], [1, 1, 1]]
# npos = np.array(pos)
# nv = np.array(v)
# print(np.add(pos , v))

class Action():

    def __init__(self):
        self.pos = [1, 2, 3]
        self.v = [0, 0, 0]

    def get_pos(self):
        self.pos= MoveAll().get_pos(self)
        return self.pos


class A():
    def __init__(self):
        self.action = Action()
        self.d = 2


m = MoveAll()
a = A()
b = A()
b.action.v = [2, 2, 1]

m.regist(a.action)
m.regist(b.action)

print(m._positions)
m.update()
print(a.action.get_pos(), b.action.get_pos())

c = A()
c.action.v = [9,9,9]

m.de_regist(a.action)
print(m._remove_ids)

m.regist(c.action)
print(m._remove_ids)


print(m._positions)
m.update()
print(c.action.get_pos(), b.action.get_pos())
