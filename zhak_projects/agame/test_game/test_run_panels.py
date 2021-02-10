
import pygame
import numpy as np

from zhak_projects.agame.elements.Ghost import Ghost, Yaorao, Xiaohua, Tiaotiao, Qie, Kuaile, Phoenix
from zhak_projects.agame.elements.Panels import Panel
from zhak_projects.agame.elements.Resources import Resources
from zhak_projects.agame.elements.SpriteActor import SpriteActor
from zhak_projects.agame.map import ViewPort, VIEW_PORT_W, VIEW_PORT_H, Map
# from zhak_projects.agame.test_game.test_run_map_bilt import tilesize
from zhak_projects.agame.zhgame import UserController, LIFE_STATE_GHOST, is_in_rect

pygame.init()

print(len(""))

view_port=ViewPort()
screen = pygame.display.set_mode((VIEW_PORT_W,VIEW_PORT_H),0,32)
controller=UserController()
pygame.display.set_caption("界面类测试")
framerate = pygame.time.Clock()

resource=Resources()

sprite_group = pygame.sprite.Group()


sa=Phoenix(screen)
sa.pos=np.random.randint(-100,100, size=(1,2))
sa.name="Phoenix"
sprite_group.add(sa)


sa=Kuaile(screen)
sa.pos=np.random.randint(-100,100, size=(1,2))
sprite_group.add(sa)

map=Map()

panel_group=pygame.sprite.Group()

panel=Panel(screen)
panel_group.add(panel)

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
            for panel in panel_group.sprites():
                if is_in_rect(np.array([x,y]), panel.pos, panel.width_height):
                    print(panel.name)
                    # panel.show()
                    panel.hide()
            world_click_pos=view_port.to_world(np.array([x, y]))

            for sprite in sprite_group.sprites():
                if is_in_rect(world_click_pos, sprite.pos, np.array([sprite.frame.frame_width,sprite.frame.frame_height])):
                    panel.update_content(sprite)
                    panel.show()
                    print(panel.content)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                view_port.pos+=np.array([-20,0])
            elif event.key == pygame.K_RIGHT:
                view_port.pos += np.array([20, 0])
            if event.key == pygame.K_UP:
                view_port.pos+=np.array([0,-20])
            elif event.key == pygame.K_DOWN:
                view_port.pos += np.array([0, 20])
    key = pygame.key.get_pressed()
    # print(key)
    if key[pygame.K_ESCAPE]:
        exit()

    screen.fill((0, 0, 100))
    sprite_group.update(ticks)
    panel_group.update(ticks)
    low_map,hight_map=map.update(sprite_group)


    screen.blits(low_map)
    sprite_group.draw(screen)
    screen.blits(hight_map)
    panel_group.draw(screen)

    pygame.display.update()