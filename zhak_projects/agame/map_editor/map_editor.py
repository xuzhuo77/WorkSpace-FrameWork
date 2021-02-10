from zhak_projects.agame.elements.SpriteActor import SpriteActor
from zhak_projects.agame.elements.scene import Scene
from zhak_projects.agame.elements.sprite_data import sprite_dict
from zhak_projects.agame.map import VIEW_PORT_W, VIEW_PORT_H
from zhak_projects.agame.map_editor.YamlUtils import read_default, write_default
import os
import numpy as np
import copy
import pygame
import json

from zhak_projects.agame.map_editor.map_file_access import FileAccessMap


class MapEditor():
    map_name = None
    data = {}
    sprite_group = None
    scene = None
    pen = None
    sprite_dict = {}

    def __init__(self, map_name, screen=None):
        pygame.init()
        pygame.display.set_caption("场景测试")
        self.screen = pygame.display.set_mode((VIEW_PORT_W, VIEW_PORT_H), 0, 32)
        self.framerate = pygame.time.Clock()

        self.scene = Scene(self.screen, self)
        self.map_name = map_name

        self.pen = Pen(self)
        self.sprite_dict = sprite_dict

        self.file_access_map = FileAccessMap(self, self.map_name)
        self.file_access_map.read(self.sprite_dict, self.screen, self.scene)

    def event(self):
        # Scene.event(self)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                world_click_pos = self.scene.view_port.to_world(np.array([x, y]))
                # self.controller.control_actor(world_click_pos, self.sprite_group)
                # controller.main_actor.be_attacked=True
                # world_pos = self.view_port.to_world(np.array([VIEW_PORT_W / 2, VIEW_PORT_H / 2]))
                # self.pen.sprite_type = 1
                # self.pen.tile_type = 1
                self.pen.paint(world_click_pos, self.scene.map, self.scene.sprite_group)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.scene.view_port.pos += np.array([-20, 0])
                elif event.key == pygame.K_RIGHT:
                    self.scene.view_port.pos += np.array([20, 0])
                if event.key == pygame.K_UP:
                    self.scene.view_port.pos += np.array([0, -20])
                elif event.key == pygame.K_DOWN:
                    self.scene.view_port.pos += np.array([0, 20])

    def write(self):
        self.file_access_map.write(self.scene)

    def run(self):
        self.pen.tile_type = 1

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
            pygame.display.update()


class Pen():
    pos = None
    range = 1
    sprite_type = None
    tile_type = None

    def __init__(self, parent):
        self.parent = parent

    def paint(self, world_pos, current_map=None, sprite_group=None):
        if self.sprite_type is not None and not self.tile_type:
            sprite = self.parent.sprite_dict[self.sprite_type](self.parent.screen)
            sprite.pos = np.array([world_pos])
            if sprite_group is not None:
                sprite_group.add(sprite)
        if self.tile_type is not None and not self.sprite_type:
            current_map.set_type(world_pos, self.tile_type)
