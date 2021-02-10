
import pygame
import numpy as np

from zhak_projects.agame.elements.Ghost import Ghost, Yaorao, Xiaohua, Tiaotiao, Qie, Kuaile, Phoenix
from zhak_projects.agame.elements.Resources import Resources
from zhak_projects.agame.elements.SpriteActor import SpriteActor
from zhak_projects.agame.elements.scene import Scene
from zhak_projects.agame.map import ViewPort, VIEW_PORT_W, VIEW_PORT_H, Map
# from zhak_projects.agame.test_game.test_run_map_bilt import tilesize
from zhak_projects.agame.zhgame import UserController, LIFE_STATE_GHOST, is_in_rect
from zhak_projects.groups import IGroup


scene=Scene()
scene.run()


