# 口香糖联盟
import numpy as np
import pickle
from SingleInstance import SingleInstance

LIFE_STATE_ALIVE = 1
LIFE_STATE_GHOST = 2


class Action():
    def __init__(self, pos=(0, 0)):
        self.pos = pos


class Actor():
    id = id
    name = "default"
    hp = 0
    maxhp = 0
    attack = 5
    defance = 5
    speed = 4
    rate = 1
    lucky = 5
    attack_range = 5
    pos = np.zeros((1, 2))
    life_state = LIFE_STATE_ALIVE

    def __init__(self, id=9999, name="default_Name", attack=2, maxhp=2, defance=2, speed=1, rate=1, lucky=1,
                 attack_range=1, pos=(0, 0)):
        self.id = id
        self.name = name
        self.hp = maxhp
        self.maxhp = maxhp
        self.attack = attack
        self.defance = defance
        self.speed = speed
        self.rate = rate
        self.lucky = lucky
        self.attack_range = attack_range
        self.pos = np.array([0, 0])
        self.life_state = LIFE_STATE_ALIVE

    def update(self, current_time=60, rate=60):
        pass

    def serialize(self):
        return pickle.dumps(self.__dict__)

    def deserialize(self, actor_dict):
        self.__dict__.update(pickle.loads(actor_dict))

    def __repr__(self):
        return str(self.__dict__)


def m_attack(actor1, actor2):
    if np.random.rand() < actor1.rate:
        loss_hp = actor1.attack - actor2.defance
        actor2.hp -= loss_hp
        print(" @{} 攻击 @{} ,@{} 失血{}。".format(actor1.name, actor2.name, actor2.name, loss_hp))
    else:
        print(" @{} 未命中".format(actor1.name))


def move_to_pos(actor, pos):
    diff = (pos - actor.pos)
    actor.pos = diff / (diff ** 2).sum() ** 0.5 * actor.speed + actor.pos
    # =des_pos if des_pos.shape[0]==2 else des_pos[0]


def move_to_actor(actor, target_actor):
    move_to_pos(actor, target_actor.pos)


def distance(pos1, pos2):
    diff = pos1 - pos2
    return np.sqrt(np.sum(np.square(diff)))


def left_or_right(direction_pos, pos):
    if np.array([pos]).shape[0] == 1:
        pos = pos[0]
    if direction_pos.shape[0] == 1:
        direction_pos = direction_pos[0]
    return (direction_pos - pos)[0] < 0


delete_list = []


def delete_actor(actor):
    delete_list.append(actor)


def delete_actor_actor_list(actor_list, _actor_list):
    for act in delete_list:
        _actor_list.remove(act)


def is_in_rect(target_pos, pos, width_height):
    lower_pos = pos
    if width_height is not None:
        upper_pos = pos + width_height
        return (target_pos > lower_pos).all() and (target_pos < upper_pos).all()
    return False


# print(actor_list[1].hp)
# print(actor_list[1].hp)
def determine_dead(actor):
    if actor.hp < 0:
        gost_list.append(actor)


def determine_target(controller, target):
    controller.target = target


def sprite_shake(actor):
    actor.pos = actor.pos + np.random.randint(-1, 1, size=(1, 2))


@SingleInstance
class UserController():
    def __init__(self, main_actor=None):
        self.target = None
        self.main_actor = main_actor

    def set_actor_target(self, actor):
        self.target = actor
        self.main_actor.target = actor

    def control_actor(self, world_click_pos, sprite_group):
        # clicked_sprite = [sprite for sprite in sprite_group.sprites()
        #                   if is_in_rect(world_click_pos, sprite.pos,
        #                                 np.array([sprite.frame.frame_width,
        #                                           sprite.frame.frame_height])) and sprite is not self.main_actor]
        clicked_sprite = [sprite for sprite in sprite_group.sprites()
                          if is_in_rect(world_click_pos, sprite.pos,sprite.get_frame_rect())
                          and sprite is not self.main_actor
                          and sprite.can_selected ==True
                          ]

        if clicked_sprite:
            self.main_actor.target = clicked_sprite[0]

            self.main_actor.weapon.bullet.trigger()
        else:
            self.main_actor.target_pos = world_click_pos
            self.main_actor.target = None
            self.main_actor.weapon.bullet.intrigger()



# print(userController.target.name,userController.main_actor.name)

# print(actor_list[0].__dict__)

if __name__ == '__main__':
    actor = Actor()
