from zhak_projects.agame.elements.Resources import Resources
from zhak_projects.agame.elements.SpriteActor import AbstractSprite, Frame
from zhak_projects.agame.map import VIEW_PORT_W, VIEW_PORT_H, ViewPort
import numpy as np


class AbstractBullet(AbstractSprite):
    def __init__(self, parent):
        super(AbstractBullet, self).__init__(parent)


class Bullet(AbstractBullet):
    def __init__(self, scene):
        self.image = None
        self.rect = None
        super(Bullet, self).__init__(self)
        self.scene = scene
        self.screen = scene.screen if scene.screen else None
        self.pos = np.array([0, 0])
        self.explosion = None
        self.view_port = ViewPort()

    def init_frame(self, suface, width, height, column):
        self.frame = Frame(self, self.screen)
        self.frame.load(suface, width, height, column)

    def update(self, current_time):
        viewport_x, viewport_y = self.view_port.pos
        frame_width, frame_height = 0, 0
        if self.frame:
            self.frame.update(current_time)
            frame_width, frame_height = self.frame.frame_width, self.frame.frame_height
        self.rect = (self.pos[0][0] + VIEW_PORT_W / 2 - viewport_x,
                     self.pos[0][1] + VIEW_PORT_H / 2 - viewport_y, frame_width, frame_height)


class MissalBullet(Bullet):
    def __init__(self, scene):
        super(MissalBullet, self).__init__(scene=scene)
        self.init_frame(*Resources().get_surface("bullet"))
        self.explosion = BombExplosion

    def explode(self, current_time):
        explosion = self.explosion(self.scene)
        explosion.pos = np.atleast_2d(self.pos)
        explosion.last_time = current_time
        self.scene.explosion_group.add(explosion)


class AbstractExplosion(AbstractSprite):
    def __init__(self, parent):
        super(AbstractExplosion, self).__init__(parent)


class Explosion(AbstractExplosion):
    def __init__(self, scene):
        self.image = None
        self.rect = None
        super(Explosion, self).__init__(self)
        self.scene = scene
        self.screen = scene.screen if scene.screen else None
        self.be_lelf_right = None
        self.pos = np.array([0, 0])
        self.view_port = ViewPort()
        self.last_time = 0

    def init_frame(self, suface, width, height, column):
        self.frame = Frame(self, self.screen)
        self.frame.load(suface, width, height, column)

    def update(self, current_time, rate=600):
        if current_time > self.last_time + rate:
            self.scene.explosion_group.remove(self)
        viewport_x, viewport_y = self.view_port.pos
        frame_width, frame_height = 0, 0
        if self.frame:
            self.frame.update(current_time)
            frame_width, frame_height = self.frame.frame_width, self.frame.frame_height
        self.rect = (self.pos[0][0] + VIEW_PORT_W / 2 - viewport_x,
                     self.pos[0][1] + VIEW_PORT_H / 2 - viewport_y, frame_width, frame_height)


class BombExplosion(Explosion):
    def __init__(self, scene):
        super(BombExplosion, self).__init__(scene=scene)
        self.init_frame(*Resources().get_surface("explosion"))
