import numpy as np

from SingleInstance import SingleInstance
from zhak_projects.agame.elements.Resources import Resources
from zhak_projects.agame.map_component.connected_domain import MapGenerate
from zhak_projects.agame.zhgame import UserController
from pygame.math import Vector2
import pygame

# TILE_WIDTH = 64
# TILE_HEIGHT = 48
N_TILE_WIDTH =10
N_TILE_HEIGHT =10

TILE_WIDTH = 64
TILE_HEIGHT = 64
MAP_WIDTH = TILE_WIDTH * N_TILE_WIDTH
MAP_HEIGHT = TILE_HEIGHT * N_TILE_HEIGHT
n_tiles_width = (int)(MAP_WIDTH / TILE_WIDTH)
n_tiles_height = (int)(MAP_HEIGHT / TILE_HEIGHT)


N_TILE_WIDTH_BIG = N_TILE_WIDTH/2
N_TILE_HEIGHT_BIG = N_TILE_HEIGHT/2
TILE_WIDTH_BIG = TILE_WIDTH * 2
TILE_HEIGHT_BIG = TILE_HEIGHT * 2
MAP_WIDTH_BIG = TILE_WIDTH_BIG * N_TILE_WIDTH_BIG
MAP_HEIGHT_BIG = TILE_HEIGHT_BIG * N_TILE_HEIGHT_BIG
n_tiles_width_big = (int)(MAP_WIDTH_BIG / TILE_WIDTH_BIG)
n_tiles_height_big = (int)(MAP_HEIGHT_BIG / TILE_HEIGHT_BIG)

VIEW_PORT_W = 1024
VIEW_PORT_H = 500

map_tiles_type = np.array([[-1, 2, 4]])


# # x,y,type
# map_tiles_type=np.append(map_tiles_type,[[5,3,4],[3,-1,3],[1,-1,4]],axis=0)
# print(map_tiles_type)


@SingleInstance
class ViewPort():
    def __init__(self, pos=np.array([0, 0])):
        self.pos = pos
        self.user_controller = UserController()

    def to_world(self, pos):
        return self.pos + pos - np.array([VIEW_PORT_W / 2, VIEW_PORT_H / 2])

    def to_screen(self, pos):
        return pos - self.pos + np.array([VIEW_PORT_W / 2, VIEW_PORT_H / 2])

    @property
    def get_pos(self):
        if self.pos.shape[0] == 2:
            return self.pos[0]
        return self.pos

    def update(self, current_time):
        main_actor = self.user_controller.main_actor
        if main_actor:
            follow_pos = main_actor.pos
            self.pos = follow_pos[0]

    def get_post_vector(self):
        viewport_pos = self.pos
        # if viewport_pos.shape[0] != 2:
        #     viewport_pos = viewport_pos[0]

        viewport_offset = pygame.math.Vector2(viewport_pos[0], viewport_pos[1])
        return viewport_offset


@SingleInstance
class MapEditorViewPort(ViewPort):
    def __init__(self, pos=np.array([0, 0])):
        ViewPort.__init__(pos)


# qi yong
def find_tiles(view_port_pos, map_tiles_type):
    x, y = view_port_pos
    upper_x = x + VIEW_PORT_W / 2
    lowwer_x = x - VIEW_PORT_W / 2
    upper_y = y + VIEW_PORT_H / 2
    lowwer_y = y - VIEW_PORT_H / 2

    lowwer_tile_i = (int)(lowwer_x // TILE_HEIGHT + n_tiles_width // 2)
    upper_tile_i = (int)(upper_x // TILE_WIDTH + n_tiles_width // 2)

    lowwer_tile_j = (int)(lowwer_y // TILE_HEIGHT + n_tiles_height // 2)
    upper_tile_j = (int)(upper_y // TILE_WIDTH + n_tiles_height // 2)

    lowwer_tile_i = lowwer_tile_i if upper_tile_i > 0 else 0
    upper_tile_i = upper_tile_i if upper_tile_i < map_tiles_type.shape[1] else map_tiles_type.shape[1]

    lowwer_tile_j = lowwer_tile_j if lowwer_tile_j > 0 else 0
    upper_tile_j = upper_tile_j if upper_tile_j < map_tiles_type.shape[0] else map_tiles_type.shape[0]

    return map_tiles_type[lowwer_tile_j:upper_tile_j, lowwer_tile_i:upper_tile_i]


# print(map_tiles_type [(map_tiles_type[:,0]<2) &(map_tiles_type[:,0]>-2)&(map_tiles_type[:,1]<2) &(map_tiles_type[:,1]>-2)])


# map_tiles_type=np.ones((n_tiles_width,n_tiles_height))
# print(map_tiles_type[4:7,8:11])
#
# show_tiles=find_tiles((0,0),map_tiles_type)
#
# print(show_tiles[0])
class MapBase():
    def __init__(self, tilempap_dict=None, viewport=None, ):
        # self.map_type=None
        self.map_data=None
        self.tilemap_dict=tilempap_dict
        self.viewport=viewport
        self.rescts=None
        self.init()

    def init(self):
        view_port_size = pygame.math.Vector2(VIEW_PORT_W / 2, VIEW_PORT_H / 2)
        map_size = pygame.math.Vector2(MAP_WIDTH_BIG / 2, MAP_HEIGHT_BIG / 2)
        self.map_offset = view_port_size - map_size
        self.tile_size = pygame.math.Vector2(TILE_WIDTH_BIG, TILE_HEIGHT_BIG)

    def set_type(self, world_pos, tile_type):
        x = world_pos[0] + MAP_WIDTH / 2
        y = world_pos[1] + MAP_HEIGHT / 2
        j = (int)(x // TILE_WIDTH)
        i = (int)(y // TILE_HEIGHT)
        self.map_data[j, i] = tile_type

    def update(self, group=None):
        # tilemap_dict = self.tilemap_dict
        # map_data = self.map_data

        viewport_offset = self.viewport.get_post_vector()

        low_layer = []
        high_layer = []
        self.map_blits = [(self.tilemap_dict[self._get_tile_type(j,i)], self._make_rect(viewport_offset, j, i))
                     for j in range(self.map_data.shape[0])
                     for i in range(self.map_data.shape[1])  if  self._get_tile_type(j,i) is not None ]


    def draw(self,screen):
        screen.blits(self.map_blits)
    def _get_tile_type(self,j,i):
        return self.map_data[j, i]
    def _make_rect(self, viewport_offset, j, i):
        tile_pos = Vector2(j * self.tile_size.x, i * self.tile_size.y)
        rect_map_pos = tile_pos - viewport_offset + self.map_offset
        rect = (rect_map_pos.x, rect_map_pos.y, self.tile_size.x, self.tile_size.y)
        return rect


class MapLayerTerritory(MapBase):
    def __init__(self, tilempap_dict=None, viewport=None):

        super(MapLayerTerritory, self).__init__(tilempap_dict, viewport, )
        # self.map_data = np.random.randint(4, size=(n_tiles_width_big, n_tiles_height_big))
        self.map_data=MapGenerate(n_tiles_width_big,8)

    def init(self):
        view_port_size = pygame.math.Vector2(VIEW_PORT_W / 2, VIEW_PORT_H / 2)
        map_size = pygame.math.Vector2(MAP_WIDTH_BIG / 2, MAP_HEIGHT_BIG / 2)
        self.map_offset = view_port_size - map_size
        self.tile_size = pygame.math.Vector2(TILE_WIDTH_BIG, TILE_HEIGHT_BIG)

class MapLayerGroundObject(MapBase):
    def __init__(self, tilempap_dict=None, viewport=None):

        super(MapLayerGroundObject, self).__init__(tilempap_dict, viewport, )

        sub = np.random.randint(0, 4, (n_tiles_width, n_tiles_height))
        y=np.argwhere(sub != 0)
        np.random.shuffle(y)
        sub[y[:40][:,0],y[:40][:,1]] = 0
        self.map_data = np.zeros((n_tiles_width, n_tiles_height))+sub
    def init(self):
        view_port_size = pygame.math.Vector2(VIEW_PORT_W / 2, VIEW_PORT_H / 2)
        map_size = pygame.math.Vector2(MAP_WIDTH/ 2, MAP_HEIGHT/ 2)
        self.map_offset = view_port_size - map_size
        self.tile_size = pygame.math.Vector2(TILE_WIDTH, TILE_HEIGHT)

    def _get_tile_type(self,j,i):
        type=self.map_data[j, i]
        if type!=0:
            return type
class Map():
    def __init__(self):
        self.tilemap_dict = Resources().tilemap_dict
        self.tilemapT_dict = Resources().tilemapT_dict
        self.viewport = ViewPort()
        self.layer1 = MapLayerTerritory(self.tilemapT_dict, self.viewport)
        self.layer2 = MapLayerGroundObject(self.tilemap_dict, self.viewport)

    def update(self, group=None):
        self.layer1.update(group)
        self.layer2.update(group)

    def draw(self, screen):
        self.layer1.draw(screen)
        self.layer2.draw(screen)


if __name__ == '__main__':
    pass
