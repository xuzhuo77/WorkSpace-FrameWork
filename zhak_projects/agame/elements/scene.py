from zhak_projects.agame.elements.Bomb import BombExplosion, MissalBullet
from zhak_projects.agame.elements.Ghost import Qie, Insect
from zhak_projects.agame.elements.Resources import Resources
from zhak_projects.agame.elements.weapon import Bullet
from zhak_projects.agame.map import ViewPort, Map, VIEW_PORT_W, VIEW_PORT_H
from zhak_projects.agame.zhgame import UserController, is_in_rect
from zhak_projects.groups import IGroup
import pygame
import numpy as np


class Scene():
    map_list = []
    current_map = None
    sprite_group = None
    screen = None
    controller = None
    view_port = None

    def __init__(self, screen=None, mapEditor=None):
        if not screen:
            pygame.init()
            pygame.display.set_caption("场景测试")
            screen = pygame.display.set_mode((VIEW_PORT_W, VIEW_PORT_H), 0, 32)

        self.screen = screen
        self.map_list = []
        self.sprite_group = None
        self.controller = None
        self.view_port = None
        self.map_file = None
        self.framerate = pygame.time.Clock()

        if mapEditor:
            self.init_elements_mapEditor()
        else:
            self.init_elements()

    def init_elements(self):
        self.view_port = ViewPort()
        self.controller = UserController()
        self.resource = Resources()
        self.sprite_group = IGroup()
        self.explosion_group = IGroup()
        self.map = Map()

        main_sprite = Qie(self)
        main_sprite.pos = np.random.randint(-100, 100, size=(1, 2))
        self.sprite_group.add(main_sprite)
        main_sprite.attack_range = 2000
        insect = Insect(self)
        insect.pos = np.random.randint(-100, 100, size=(1, 2))
        insect.speed=1
        insect.target=main_sprite
        self.sprite_group.add(insect)

        exp=BombExplosion(self)
        exp.pos = np.random.randint(-100, 100, size=(1, 2))
        self.explosion_group.add(exp)
        exp=MissalBullet(self)
        exp.pos = np.random.randint(-100, 100, size=(1, 2))
        exp.speed = 1
        exp.target = main_sprite
        self.sprite_group.add(exp)
        self.framerate.tick(30)
        ticks = pygame.time.get_ticks()
        exp.explode(ticks)


        self.controller.main_actor = main_sprite

    def init_elements_mapEditor(self):
        self.view_port = ViewPort()
        self.controller = UserController()
        self.resource = Resources()
        self.sprite_group = IGroup()
        self.map = Map()

    # def init_from_read(self):

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                world_click_pos = self.view_port.to_world(np.array([x, y]))
                self.controller.control_actor(world_click_pos, self.sprite_group)
                # controller.main_actor.be_attacked=True
                # self.controller.main_actor.weapon.bullet.destination = world_click_pos

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.view_port.pos += np.array([-20, 0])
                elif event.key == pygame.K_RIGHT:
                    self.view_port.pos += np.array([20, 0])
                if event.key == pygame.K_UP:
                    self.view_port.pos += np.array([0, -20])
                elif event.key == pygame.K_DOWN:
                    self.view_port.pos += np.array([0, 20])

    def update(self, ticks):
        self.sprite_group.update(ticks)
        self.explosion_group.update(ticks)
        # self.view_port.update(ticks)
        self.map.update(self.sprite_group)

    def draw(self, screen):
        screen.fill((0, 0, 100))
        self.map.draw(screen)
        self.sprite_group.draw(self.screen)
        self.explosion_group.draw(self.screen)

        self.controller.main_actor.weapon.bullet.draw(screen)

    def run(self):
        while True:
            self.framerate.tick(30)
            ticks = pygame.time.get_ticks()

            self.event()

            self.update(ticks)
            self.draw(self.screen)
            # screen.fill((0, 0, 100))
            # sprite_group.update(ticks)
            # view_port.update(ticks)
            # low_map, hight_map = map.update(sprite_group)
            #
            # screen.blits(low_map)
            # sprite_group.draw(screen)
            # screen.blits(hight_map)
            pygame.display.update()
