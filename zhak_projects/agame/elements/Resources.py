import pygame
import os

from SingleInstance import SingleInstance


@SingleInstance
class Resources():
    frame_surfaces = {}
    image_data = {"ghost": ("ghost.png", 72, 72, 12),
                  "kuaile": ("kuaile.png", 64, 64, 47),
                  "qie": ("qie.png", 72, 72, 26),
                  "tiaotiao": ("tiaotiao.png", 64, 64, 47),
                  "xiaohua": ("xiaohua.png", 64, 64, 10),
                  "yaorao": ("yaorao.png", 128, 100, 8),
                  "phoenix":("phoenix1.png", 80, 128, 1),
                  "panel_info":("panel_info.png", 256, 144, 1),
                  "fangtang":("fangtang.png",128,128,1),
                  "xiezi_run":("xiezi_run.png",128,100,10),
                  "gun":("gun.png",64,30,1),
                  "gun2": ("gun2.png", 64, 30, 1),
                  "light":("light.png",300,150,10),
                  "insect":("insect2.png",16,16,1),

                  "explosion": ("explosion.png", 64, 64, 10),
                  "bullet": ("bullet.png", 32, 32, 1),
                  }

    system_path='D:\\WorkSpace-FrameWork\\'
    # system_path='E:\\pythonWebWorkSpace\\'
    base_path = system_path+'zhak_projects\\agame\\statics'

    font_data={
        "panel":("宋体",40)
    }
    font_surface={}
    tilemap_dict={}
    def __init__(self):
        print("intt---------------")
        self.init()

    def init(self):
        try:
            for key, value in self.image_data.items():
                filename = self.base_path + os.sep + value[0]
                surface = pygame.image.load(filename).convert_alpha()
                self.frame_surfaces[key] = surface
        except:
            print("Exception Resource Test","actor")
        try:
            tilemapT1 = pygame.image.load(self.base_path+'\\tiles\\tile1.png')
            tilemapT2 = pygame.image.load(self.base_path+'\\tiles\\tile2.png')
            tilemapT3 = pygame.image.load(self.base_path+'\\tiles\\tile3.png')
            tilemapT4 = pygame.image.load(self.base_path+'\\tiles\\tile4.png')#hai
            self.tilemapT_dict = {0: tilemapT4, 1: tilemapT2, 2: tilemapT3, 3: tilemapT1}

            tilemap1 = pygame.image.load(self.base_path+'\\tiles\\sakula.png')
            tilemap2 = pygame.image.load(self.base_path+'\\tiles\\sakula1.png')
            tilemap3 = pygame.image.load(self.base_path+'\\tiles\\songshu1.png')
            tilemap4 = pygame.image.load(self.base_path+'\\tiles\\songshu2.png')
            self.tilemap_dict = {1: tilemap1, 2: tilemap2, 3: tilemap3, 4: tilemap4}
        except:
            print("Exception Resource Test","maptiles")
        try:
            for key, value in self.font_data.items():
                surface=pygame.font.SysFont(*value)
                self.font_surface[key] = surface
        except:
            print("Exception Resource Test","font")
    def get_surface(self, name):
        data = self.image_data[name]
        image=None
        try:
            image=self.frame_surfaces[name]
        except :
            print("Exception Resource Test frame Empty ,{}".format(name))
        return image, data[1], data[2], data[3]
    def get_font(self, name):
        image=None
        try:
            image=self.font_surface[name]
        except :
            print("Exception Resource Test font_surface Empty,{}".format(name))
        return image
# resource=Resources()
