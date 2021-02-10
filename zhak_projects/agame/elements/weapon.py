import pygame

from pygame.sprite import Sprite

from zhak_projects.agame.elements.Resources import Resources
import numpy as np

from zhak_projects.agame.elements.SpriteActor import AbstractSprite
from zhak_projects.agame.center_rotate import rotate
from zhak_projects.agame.map import ViewPort, VIEW_PORT_H, VIEW_PORT_W


class Weapon(AbstractSprite):
    def __init__(self, parent):
        super(Weapon, self).__init__(parent)
        self.master_image = Resources().get_surface("gun2")[0]
        self.pos = np.array([20, 20])
        self.weapon = None
        self.frame = None
        self.image = None
        self.offset_value = -12
        self.offset_waist_value = 20
        self.bullet = None
        self.head_offset=None
    def update(self, current_time):
        _, _, sprite_width, sprite_height = self.parent.rect
        sprite_screen_pos_x, sprite_screen_pos_y =self.parent.view_port.to_screen(self.parent.pos)[0]

        mouse_pos = np.array(pygame.mouse.get_pos())
        sprite_screen_pos = np.array([sprite_screen_pos_x, sprite_screen_pos_y])
        direction_vector = mouse_pos - sprite_screen_pos
        angle = np.rad2deg(np.arctan(direction_vector[1] / (1e-5 if direction_vector[0] == 0 else direction_vector[0])))
        pivot = [sprite_screen_pos_x + sprite_width / 2, sprite_screen_pos_y + sprite_height / 2 + self.offset_waist_value]
        if direction_vector[0] < 0:
            self.image = pygame.transform.flip(self.master_image, True, False)
            offset = pygame.math.Vector2(self.offset_value, 0.0)
            offset_100 = pygame.math.Vector2(-50, 0)

        else:
            self.image = self.master_image
            offset = pygame.math.Vector2(-1 * self.offset_value, 0.0)
            offset_100 = pygame.math.Vector2(50, 0)

        rotated_101 = offset_100.rotate(angle)
        sprite_x,sprite_y=self.parent.pos[0]
        weapon_pivot = [ sprite_x+sprite_width//2, sprite_y + self.offset_waist_value]

        self.head_offset = weapon_pivot + rotated_101
        self.image, self.rect = rotate(surface=self.image, angle=angle, pivot=pivot, offset=offset)
        if self.bullet:
            self.bullet.update(current_time)

    def parent_pos(self):
        return self.parent.pos


        # self.bullet.draw(self.screen)


class ParticalSystem():
    def __init__(self, parent=None):
        self._list = []
        self.partical_type = None
        self.parent = parent
        self.n_rows = 10
        self.destination = np.array([[1, 2]])
        self.width = 16
        self.height = 16
        self.image = None
        self._switcher = False
        self.last_time = 0
        self.view_port = ViewPort()
        self.init()

    def init(self):
        self.start_point = self.particals = np.random.randint(4, 9, (self.n_rows, 3))
        self.particals[:, 2] = 0

    def set_pos(self, destination):
        self.destination = destination

    def _start_point(self):
        return np.array([self.parent.head_offset.x,self.parent.head_offset.y])

    def trigger(self):
        self._switcher = True
    def intrigger(self):
        self._switcher = False
    def _deactivated(self, particals):
        return particals[:, 2] == 0

    def _activated(self, particals):
        return particals[:, 2] != 0

    def update(self, current_time=None, rate=60):
        if self._switcher == True:

            particals = self.particals
            if current_time > self.last_time + rate:
                deactivated = np.argwhere(self._deactivated(particals)).reshape(1, -1)[0]
                if deactivated.size != 0:
                    choice_id = np.random.choice(deactivated)
                    # choice_id=np.random.choice(self.n_rows)
                    particals[choice_id][2] = 1
                    particals[choice_id][:2] = self._start_point()
                self.last_time = current_time

            activated = np.argwhere(self._activated(particals)).reshape(1, -1)[0]
            if activated.size != 0:
                vector = self.destination - particals[:, :2]
                # direction=self.destination - self.start_point[:, :2]
                particals_speed = vector / np.linalg.norm(vector) * 15
                self.particals = particals + np.column_stack((particals_speed, np.zeros(self.n_rows)))

            self.destination=self.parent.parent.target.pos
            destination_distance = np.linalg.norm((self.destination.reshape(-1, 2) - particals[:, :2]), axis=1,
                                                  keepdims=True)
            condition = (destination_distance < 4).reshape(self.n_rows)
            if condition.any():
                self.particals[np.where(condition), 2] = 0

            # moving_distance=np.linalg.norm(( particals[:, :2])-self._start_point(), axis=1,
            #                                       keepdims=True)
            # condition = (moving_distance >300 ).reshape(self.n_rows)
            # if condition.any():
            #     self.particals[np.where(condition), 2] = 0
        else:
            activated = np.argwhere(self._activated(self.particals)).reshape(1, -1)[0]
            if activated.size != 0:
                vector = self.destination - self.particals[:, :2]
                # direction=self.destination - self.start_point[:, :2]
                particals_speed = vector / np.linalg.norm(vector) * 15
                self.particals = self.particals + np.column_stack((particals_speed, np.zeros(self.n_rows)))

                # self.destination = self.parent.parent.target.pos
                destination_distance = np.linalg.norm((self.destination.reshape(-1, 2) - self.particals[:, :2]), axis=1,
                                                      keepdims=True)
                condition = (destination_distance < 4).reshape(self.n_rows)
                if condition.any():
                    self.particals[np.where(condition), 2] = 0

    def draw(self, screen=None):
        particals = self.particals

        particals_show = particals[
            np.argwhere((self._activated(particals)))[:, 0]
        ]
        particals_show = self.view_port.to_screen(particals_show[:, :2])
        rect = np.column_stack(
            (particals_show, np.repeat(np.array([[self.width, self.height]]), particals_show.shape[0], axis=0)))

        surface = self.image
        all_par = [(surface, tuple(t)) for t in rect.tolist()]
        # print(all_par)
        screen.blits(all_par)


class Bullet(ParticalSystem):
    def __init__(self, parent):
        super(Bullet, self).__init__(parent)


