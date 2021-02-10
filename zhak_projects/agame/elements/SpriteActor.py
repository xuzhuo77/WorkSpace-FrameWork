import pygame
from pygame.sprite import Sprite
import numpy as np
import json

from zhak_projects.agame.center_rotate import rotate
from zhak_projects.agame.elements import Resources
from zhak_projects.agame.map import VIEW_PORT_W, VIEW_PORT_H, ViewPort
from zhak_projects.agame.zhgame import Actor, distance, move_to_actor, move_to_pos, left_or_right, LIFE_STATE_GHOST, \
    LIFE_STATE_ALIVE


class AbstractSprite(Sprite):
    def __init__(self, parent=None):
        super(AbstractSprite, self).__init__()
        self.frame = None
        self.weapon = None
        self.sprite_type = None
        self.parent = parent
        self.can_selected=False

    def get_frame_rect(self):
        if self.frame:
            return np.array([self.frame.frame_width, self.frame.frame_height])
        return None


class SpriteActor(AbstractSprite, Actor):
    def __init__(self, scene):


        self.image = None
        self.rect = None
        super(SpriteActor, self).__init__()
        self.scene =scene
        self.screen = scene.screen if scene.screen else None
        self.can_selected=True
        self.last_attack_time = 0
        self.attack_rate = 1000
        self.type = 0
        self.target = None
        self.target_pos = None
        self.width_height = np.array([32, 32])
        self.be_lelf_right = True
        self.be_attacked = False
        self.be_attacked_last_time = 0
        self.be_attacked_rate = 20000
        self.view_port = ViewPort()

    def init_frame(self, suface, width, height, column):
        self.frame = Frame(self, self.screen)
        self.frame.load(suface, width, height, column)

    def update(self, current_time, rate=60):
        if self.life_state == LIFE_STATE_ALIVE:
            if self.hp < 0:
                self.hp = 0
                self.life_state = LIFE_STATE_GHOST
                self.init_frame(*Resources().get_surface("ghost"))

        if self.target and self.target.type == 1:
            if self.attack_range >= distance(self.target.pos, self.pos):
                if current_time > self.last_attack_time + self.attack_rate:
                    print("attack")
                    self.target.be_attacked = True
                    self.last_attack_time = current_time

        if self.target and distance(self.pos, self.target.pos) > self.attack_range:
            move_to_actor(self, self.target)
            self.be_lelf_right = left_or_right(self.target.pos, self.pos)
        elif not self.target and (self.target_pos is not None and distance(self.pos, self.target_pos) > 30):
            move_to_pos(self, self.target_pos)
            self.be_lelf_right = left_or_right(self.target_pos, self.pos)

        viewport_x, viewport_y = self.view_port.pos
        frame_width, frame_height = 0, 0

        if self.frame:
            self.frame.update(current_time)
            frame_width, frame_height = self.frame.frame_width, self.frame.frame_height
        shake_range = np.zeros((1, 2))
        if current_time > self.be_attacked_last_time + self.be_attacked_rate:
            self.be_attacked = False
            self.be_attacked_last_time = current_time
        if self.be_attacked:
            shake_range += np.random.randint(-1, 2, size=(1, 2)) * 4

        self.rect = (shake_range[0][0] + self.pos[0][0] + VIEW_PORT_W / 2 - viewport_x,
                     shake_range[0][0] + self.pos[0][1] + VIEW_PORT_H / 2 - viewport_y, frame_width, frame_height)

        if self.weapon:
            self.weapon.update(current_time)

    def panel_info(self):
        return self.name

    def set_life_state(self, state):
        self.life_state = state

    def map_editor_serialize(self):
        return json.dumps({"pos": self.pos.tolist(), "sprite_type": self.sprite_type})


class Frame():
    def __init__(self, parent, target):
        self.target_surface = target
        self.image = None
        self.master_image = None
        self.rect = None
        self.topleft = 0, 0
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.parent = parent

    def load(self, surface, width, height, columns):
        self.master_image = surface
        self.frame_width = width
        self.frame_height = height
        self.parent.rect = 0, 0, width, height
        self.columns = columns
        if self.master_image:
            rect = self.master_image.get_rect()
            self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=60):
        # 更新动画帧
        if self.columns==1:
            _, _, sprite_width, sprite_height = self.parent.rect

            sprite_screen_pos_x, sprite_screen_pos_y = self.parent.view_port.to_screen(self.parent.pos)[0]
            sprite_screen_pos = np.array([sprite_screen_pos_x, sprite_screen_pos_y])

            target_pos = self.parent.target.pos
            target_screen_pos =self.parent.view_port.to_screen(target_pos)[0]
            # target_pos = np.array(pygame.mouse.get_pos())

            direction_vector = target_screen_pos - sprite_screen_pos
            angle = np.rad2deg(
                np.arctan(direction_vector[1] / (1e-5 if direction_vector[0] == 0 else direction_vector[0])))
            pivot = [sprite_screen_pos_x + sprite_width / 2,
                     sprite_screen_pos_y + sprite_height / 2 ]

            if direction_vector[0] < 0:
                self.image =pygame.transform.flip(self.master_image, True, False)
                offset = pygame.math.Vector2(0, 0.0)
                rotated_image, self.rect = rotate(surface=self.image, angle=angle-90, pivot=pivot, offset=offset)

            else:
                self.image =self.master_image
                offset = pygame.math.Vector2(0, 0.0)
                rotated_image, self.rect = rotate(surface=self.image, angle=angle+90, pivot=pivot, offset=offset)

            self.parent.image =rotated_image


        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
        if self.columns != 1:
            if self.frame != self.old_frame:
                frame_x = (self.frame % self.columns) * self.frame_width
                frame_y = (self.frame // self.columns) * self.frame_height
                rect = (frame_x, frame_y, self.frame_width, self.frame_height)
                if self.parent.be_lelf_right is not None:
                    if not self.parent.be_lelf_right:
                        self.parent.image = self.master_image.subsurface(rect)
                        if self.parent.life_state == LIFE_STATE_GHOST:
                            self.parent.image = pygame.transform.rotate(self.parent.image, -20)

                    else:
                        self.parent.image = self.master_image.subsurface(rect)
                        if self.parent.life_state == LIFE_STATE_GHOST:
                            self.parent.image = pygame.transform.rotate(self.parent.image, -20)
                        self.parent.image = pygame.transform.flip(self.parent.image, True, False)
                else:
                    self.parent.image = self.master_image.subsurface(rect)
                self.old_frame = self.frame
