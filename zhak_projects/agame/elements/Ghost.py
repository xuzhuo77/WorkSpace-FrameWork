import pygame

from zhak_projects.agame.elements.Resources import Resources
from zhak_projects.agame.elements.SpriteActor import SpriteActor
from zhak_projects.agame.elements.weapon import Weapon, Bullet
import numpy as np

class Ghost(SpriteActor):
    def __init__(self, scene):
        SpriteActor.__init__(self, scene)
        self.sprite_type=2
        self.init_frame(*Resources().get_surface("qie"))


class Kuaile(SpriteActor):
    def __init__(self, scene):
        SpriteActor.__init__(self, scene)
        self.sprite_type=7
        self.init_frame(*Resources().get_surface("kuaile"))


class Qie(SpriteActor):
    def __init__(self, scene):
        super(Qie,self).__init__(scene=scene)
        self.init_frame(*Resources().get_surface("qie"))
        self.sprite_type=1
        self.weapon=Weapon(self)
        self.weapon.bullet=Bullet(self.weapon)
        self.weapon.bullet.image=pygame.Surface((16, 16))


class Tiaotiao(SpriteActor):
    def __init__(self, scene):
        SpriteActor.__init__(self, scene)
        self.sprite_type=4
        self.init_frame(*Resources().get_surface("tiaotiao"))


class Xiaohua(SpriteActor):
    def __init__(self, scene):
        SpriteActor.__init__(self, scene)
        self.type=5
        self.init_frame(*Resources().get_surface("xiaohua"))

class Yaorao(SpriteActor):
    def __init__(self, scene):
        SpriteActor.__init__(self, )
        self.sprite_type=6
        self.init_frame(*Resources().get_surface("yaorao"))


class Phoenix(SpriteActor):
    def __init__(self, scene):
        SpriteActor.__init__(self, scene)
        self.sprite_type=3
        self.init_frame(*Resources().get_surface("phoenix"))


class Insect(SpriteActor):
    def __init__(self, scene):
        super(Insect,self).__init__(scene)
        self.sprite_type=9
        self.init_frame(*Resources().get_surface("insect"))

