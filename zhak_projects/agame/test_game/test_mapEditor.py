from zhak_projects.agame.elements.Ghost import Qie
from zhak_projects.agame.map import VIEW_PORT_W, VIEW_PORT_H
from zhak_projects.agame.map_editor.map_editor import MapEditor, Pen
import numpy as np

from zhak_projects.agame.map_editor.map_editor_tkinter import MapEditorTkinter

map_editor=MapEditorTkinter("map1",None)
print(map_editor.scene.current_map.map_type)


# ----------------save tile-----------------
world_pos = map_editor.scene.view_port.to_world(np.array([VIEW_PORT_W/2,VIEW_PORT_H/2]))
map_editor.pen.tile_type=2
map_editor.pen.sprite_type=None
map_editor.pen.paint(world_pos,map_editor.scene.current_map)
map_editor.pen.paint(world_pos, map_editor.scene.map, map_editor.scene.sprite_group)

print(map_editor.scene.current_map.map_type)
map_editor.write()


# ----------------save sprite-----------------
# map_editor.pen.sprite_type=1
# map_editor.pen.tile_type=None
# map_editor.pen.paint(world_pos, map_editor.scene.map, map_editor.scene.sprite_group)
# print(len(map_editor.scene.sprite_group.sprites()))
# map_editor.write()
#
# map_editor.read()





