
import pygame
import numpy as np

from zhak_projects.agame.elements.Ghost import Ghost, Yaorao, Xiaohua, Tiaotiao, Qie, Kuaile, Phoenix
from zhak_projects.agame.elements.Resources import Resources
from zhak_projects.agame.elements.SpriteActor import SpriteActor
from zhak_projects.agame.map import ViewPort, VIEW_PORT_W, VIEW_PORT_H, Map
# from zhak_projects.agame.test_game.test_run_map_bilt import tilesize
from zhak_projects.agame.zhgame import UserController, LIFE_STATE_GHOST, is_in_rect
from zhak_projects.groups import IGroup

pygame.init()

print(len(""))

view_port=ViewPort()
screen = pygame.display.set_mode((VIEW_PORT_W,VIEW_PORT_H),0,32)
controller=UserController()
pygame.display.set_caption("精灵类测试")
framerate = pygame.time.Clock()

resource=Resources()

sprite_group = IGroup()

# sa=Ghost(screen)
# sa.pos=np.random.randint(-100,100, size=(1,2))
# group.add(sa)
#
sa=Phoenix(screen)
sa.pos=np.random.randint(-100,100, size=(1,2))
sprite_group.add(sa)

sa=Kuaile(screen)
sa.pos=np.random.randint(-100,100, size=(1,2))
sprite_group.add(sa)
sa.type=1
#
sa=Qie(screen)
sa.pos=np.random.randint(-100,100, size=(1,2))
sprite_group.add(sa)
sa.attack_range=20

# sa=Tiaotiao(screen)
# sa.pos=np.random.randint(-100,100, size=(1,2))
# group.add(sa)

# sa=Xiaohua(screen)
# sa.pos=np.random.randint(-100,100, size=(1,2))
# sprite_group.add(sa)

# sa=Yaorao(screen)
# sa.speed=20
# sa.pos=np.random.randint(-100,100, size=(1,2))
# group.add(sa)
map=Map()

# sa.init_frame(*resource.get_surface("ghost"))

controller.main_actor=sa
while True:
    framerate.tick(30)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            world_click_pos = view_port.to_world(np.array([x, y]))
            controller.control_actor(world_click_pos,sprite_group)
            # controller.main_actor.be_attacked=True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                view_port.pos+=np.array([-20,0])
            elif event.key == pygame.K_RIGHT:
                view_port.pos += np.array([20, 0])
            if event.key == pygame.K_UP:
                view_port.pos+=np.array([0,-20])
            elif event.key == pygame.K_DOWN:
                view_port.pos += np.array([0, 20])
    key = pygame.mouse.get_pos()
    # print(key)
    # if key[pygame.K_ESCAPE]:
    #     exit()

    screen.fill((0, 0, 100))
    sprite_group.update(ticks)
    view_port.update(ticks)
    low_map, hight_map = map.update(sprite_group)

    screen.blits(low_map)
    sprite_group.draw(screen)
    screen.blits(hight_map)
    pygame.display.update()