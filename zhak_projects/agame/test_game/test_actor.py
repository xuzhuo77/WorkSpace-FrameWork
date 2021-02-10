from zhak_projects.agame.map import ViewPort
from zhak_projects.agame.zhgame import m_attack, UserController, determine_target, Actor, move_to_pos, move_to_actor, \
    distance, is_in_rect, left_or_right

from zhak_projects.agame.test_game.test_value import     init_actor_list
import numpy as np
actor_list=init_actor_list()
m_attack(actor_list[0],actor_list[1])


def get_actor_list():
    return actor_list


userController=UserController(actor_list[0])
determine_target(userController,actor_list[3])

def test_serialize_deserialize(actor_list):
    actor = actor_list[0]
    actor.pos=np.ones((1,2))
    print(actor)
    newa = Actor()
    print(newa)
    newa.deserialize(actor.serialize())
    print(newa)

test_serialize_deserialize(actor_list)

actor_list[0].update()

print("位置移动")
print(actor_list[0].pos)
move_to_pos(actor_list[0],np.array([4,5]))
print(actor_list[0].pos)

print("向物体移动")
print(actor_list[0].pos)
move_to_actor(actor_list[0],actor_list[1])
print(actor_list[0].pos)

print("两点距离")
print(distance(actor_list[0].pos,actor_list[1].pos))
print("   ")

width_height=np.array([32,32])
pos=np.array([0,0])
random_pos=np.array([2,2])
print("在范围内",is_in_rect(random_pos,pos,width_height))
random_pos=np.array([-2,2])
print("不在范围内",is_in_rect(random_pos,pos,width_height))
random_pos=np.array([40,2])
print("不在范围内",is_in_rect(random_pos,pos,width_height))

for actor in actor_list:
    print(is_in_rect(random_pos,actor.pos,width_height))

pos=np.array([10,0])
direction_pos=np.array([0,5])
# left_or_right()
print("left",left_or_right(direction_pos,pos))
direction_pos=np.array([20,5])
print("right",left_or_right(direction_pos,pos))


width_height=np.array([32,32])
pos=np.array([0,0])
random_pos=np.array([2,2])

view_port=ViewPort()
world_pos=view_port.to_world(random_pos)
print("不在范围内",is_in_rect(world_pos,pos,width_height))




if direction_pos is None:
    print("T")

