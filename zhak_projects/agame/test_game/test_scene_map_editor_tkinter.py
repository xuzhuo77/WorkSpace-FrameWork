
import pygame
import numpy as np

from zhak_projects.agame.elements.Ghost import Ghost, Yaorao, Xiaohua, Tiaotiao, Qie, Kuaile, Phoenix
from zhak_projects.agame.elements.Resources import Resources
from zhak_projects.agame.elements.SpriteActor import SpriteActor
from zhak_projects.agame.elements.scene import Scene
from zhak_projects.agame.map import ViewPort, VIEW_PORT_W, VIEW_PORT_H, Map
# from zhak_projects.agame.test_game.test_run_map_bilt import tilesize
from zhak_projects.agame.map_editor.map_editor import MapEditor
from zhak_projects.agame.map_editor.map_editor_tkinter import MapEditorTkinter
from zhak_projects.agame.zhgame import UserController, LIFE_STATE_GHOST, is_in_rect
from zhak_projects.groups import IGroup


map_editor=MapEditorTkinter("map1")

map_editor.run()

# sa=Ghost(screen)
# sa.pos=np.random.randint(-100,100, size=(1,2))
# group.add(sa)
#
#
#


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

# sa.init_frame(*resource.get_surface("ghost"))
