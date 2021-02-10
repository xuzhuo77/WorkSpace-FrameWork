from pygame.sprite import Sprite
import numpy as np

from zhak_projects.agame.elements.Resources import Resources
import pygame
PANEL_HIDE_POS=[-20000,-20000]
class Panel(Sprite):
    def __init__(self, screen=None):
        Sprite.__init__(self)
        source=Resources().get_surface("panel_info")
        self.image =source[0]
        self.width_height = np.array([source[1] , source[2] ])
        self.screen = screen
        self.pos=np.array([0,0])
        self.name="panel"
        self.content="empty"
        self.show_pos=np.array([2,2])
        self.rect=(self.pos[0],self.pos[1],self.width_height[0],self.width_height[1])
        self.text=Resources().get_font("panel")
    def show(self):
        self.pos=self.show_pos
        self.rect=(self.pos[0],self.pos[1],self.width_height[0],self.width_height[1])
    def hide(self):
        self.pos=np.array(PANEL_HIDE_POS)
        self.rect = (self.pos[0], self.pos[1], self.width_height[0], self.width_height[1])

    def update_content(self, sprite):
        self.content=sprite.panel_info()
        source=Resources().get_surface("panel_info")
        self.image =source[0]
        if self.text:
            text_fmt=self.text.render(self.content,1,(255,255,255))
            self.image.blit(text_fmt,(120,40))




