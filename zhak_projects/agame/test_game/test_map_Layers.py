
from zhak_projects.agame.elements.Resources import Resources
from zhak_projects.agame.map import find_tiles, ViewPort, n_tiles_width, n_tiles_height, TILE_WIDTH, Map, VIEW_PORT_W, \
    VIEW_PORT_H
import numpy as np
import pygame
map_tiles_type=np.random.randint(4,size=(n_tiles_width,n_tiles_height))
print(map_tiles_type)
pygame.init()
screen = pygame.display.set_mode((VIEW_PORT_W,VIEW_PORT_H),0,32)
resource=Resources()
view_port=ViewPort()
map=Map()


map.update()
map.draw(screen)