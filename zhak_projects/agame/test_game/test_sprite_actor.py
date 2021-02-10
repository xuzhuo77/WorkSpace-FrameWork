import pygame
import numpy as  np
from zhak_projects.agame.elements.SpriteActor import SpriteActor
from zhak_projects.agame.map import ViewPort, VIEW_PORT_W, VIEW_PORT_H
from zhak_projects.agame.zhgame import UserController

framerate = pygame.time.Clock()

actor=SpriteActor()
attacked_actor=SpriteActor()

group = pygame.sprite.Group()
group.add(actor)
group.add(attacked_actor)

attacked_actor.type=1
attacked_actor.pos=np.array([[3,4]])
actor.target=attacked_actor
actor.attack_range=6

controller=UserController()
controller.main_actor=actor
controller.set_actor_target(attacked_actor)


framerate.tick(30)
ticks = pygame.time.get_ticks()
group.update(ticks)

framerate.tick(30)
ticks = pygame.time.get_ticks()
group.update(ticks)

framerate.tick(30)
ticks = pygame.time.get_ticks()
group.update(ticks)

del attacked_actor

framerate.tick(30)
ticks = pygame.time.get_ticks()
group.update(ticks)



print(len(""))

view_port=ViewPort()
controller=UserController()
pygame.display.set_caption("精灵类测试")
framerate = pygame.time.Clock()

for sprite in  group.sprites():
    print(sprite.pos)

import json
print(actor.map_editor_serialize())





