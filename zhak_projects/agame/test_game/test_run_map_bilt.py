import sys
import random
import numpy as np
import pygame

from zhak_projects.agame.elements.Resources import Resources
from zhak_projects.agame.map import  ViewPort, VIEW_PORT_W, VIEW_PORT_H, \
    TILE_WIDTH, Map

pygame.init()


tilesize = TILE_WIDTH
screen = pygame.display.set_mode((VIEW_PORT_W, VIEW_PORT_H))
resource=Resources()
map=Map()
view_port=ViewPort()

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pass

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x, y)
        if event.type == pygame.MOUSEBUTTONUP:
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                view_port.pos+=np.array([-20,0])
            elif event.key == pygame.K_RIGHT:
                view_port.pos += np.array([20, 0])
            if event.key == pygame.K_UP:
                view_port.pos+=np.array([0,-20])
            elif event.key == pygame.K_DOWN:
                view_port.pos += np.array([0, 20])
    blit_list = []
    blit_list=map.show()


    # instead of using multiple blit calls above, calling screen.blits here fails
    # remove the area argument (3rd arg) from each blit_arg tuple works
    screen.blits(blit_list)

    pygame.display.flip()

    # wait a second
    pygame.time.wait(30)