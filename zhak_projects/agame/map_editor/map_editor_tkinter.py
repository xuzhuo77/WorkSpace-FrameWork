from zhak_projects.agame.elements.scene import Scene
from zhak_projects.agame.elements.sprite_data import sprite_dict
from zhak_projects.agame.map import VIEW_PORT_W, VIEW_PORT_H
from zhak_projects.agame.map_editor.YamlUtils import read_default, write_default
import os
import numpy as np
import copy
import pygame

from zhak_projects.agame.map_editor.game_tkinter import PygameTkinter
from zhak_projects.agame.map_editor.map_editor import MapEditor


class MapEditorTkinter(MapEditor,PygameTkinter):
    map_name = None
    data = {}
    sprite_group = None
    scene = None
    pen = None
    sprite_dict = {}

    def __init__(self, map_name, screen=None):
        PygameTkinter.__init__(self, (VIEW_PORT_W, VIEW_PORT_H),self)
        self.init_pygame()

        MapEditor.__init__(self,map_name,None)

        # self.init_pygame()
        # pygame.display.init()
        # pygame.display.set_caption("场景测试")
        # self.screen = pygame.display.set_mode((VIEW_PORT_W, VIEW_PORT_H), 0, 32)
        # pygame.display.flip()
        # self.framerate = pygame.time.Clock()
        #
        # self.scene = Scene(self.screen,self)
        # self.map_name = map_name
        # self.data = {"map_name": self.map_name}
        #
        # self.pen = Pen(self)
        # self.sprite_dict = sprite_dict
        # self.read()
        # self.scene.current_map.map_type=np.array(self.data["map_type"])
        # # self.map_type=self.data["map_type"]

    # def event(self):
    #     # Scene.event(self)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             exit()
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             x, y = event.pos
    #
    #             world_click_pos = self.scene.view_port.to_world(np.array([x, y]))
    #             # self.controller.control_actor(world_click_pos, self.sprite_group)
    #             # controller.main_actor.be_attacked=True
    #             # world_pos = self.view_port.to_world(np.array([VIEW_PORT_W / 2, VIEW_PORT_H / 2]))
    #             # self.pen.sprite_type = 1
    #             # self.pen.tile_type = 1
    #             self.pen.paint(world_click_pos, self.scene.current_map, self.scene.sprite_group)
    #
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_LEFT:
    #                 self.scene.view_port.pos += np.array([-20, 0])
    #             elif event.key == pygame.K_RIGHT:
    #                 self.scene.view_port.pos += np.array([20, 0])
    #             if event.key == pygame.K_UP:
    #                 self.scene.view_port.pos += np.array([0, -20])
    #             elif event.key == pygame.K_DOWN:
    #                 self.scene.view_port.pos += np.array([0, 20])

    # def update_map(self):
    #     self.data.update({"map_type": self.scene.current_map.map_type.tolist()})



#     def read(self):
#         self.data = read_default(self.map_name + ".yaml")
#
#
#     def write(self):
#         self.update_map()
#         self.update_sprite()
#         try:
#             write_default(self.map_name + ".yaml", self.data)
#         except:
#             open(self.map_name + ".yaml", 'w')
#             write_default(self.map_name + ".yaml", self.data)
#
    def run(self):
        # self.pen.tile_type = 1

        while True:
            self.framerate.tick(30)
            ticks = pygame.time.get_ticks()

            self.event()

            self.scene.update(ticks)
            self.scene.draw(self.screen)
            # screen.fill((0, 0, 100))
            # sprite_group.update(ticks)
            # view_port.update(ticks)
            # low_map, hight_map = map.update(sprite_group)
            #
            # screen.blits(low_map)
            # sprite_group.draw(screen)
            # screen.blits(hight_map)
            # pygame.display.update()
            pygame.display.flip()
            self.tk_root.update()
#
#
# class Pen():
#     pos = None
#     range = 1
#     sprite_type = None
#     tile_type = None
#
#     def __init__(self, parent):
#         self.parent = parent
#
#     def paint(self, world_pos, current_map=None, sprite_group=None):
#         if self.sprite_type is not None and not self.tile_type:
#             sprite = self.parent.sprite_dict[self.sprite_type](self.parent.screen)
#             sprite.pos = np.array([world_pos])
#             sprite_group.add(sprite)
#         if self.tile_type is not None and not self.sprite_type:
#             current_map.set_type(world_pos, self.tile_type)
