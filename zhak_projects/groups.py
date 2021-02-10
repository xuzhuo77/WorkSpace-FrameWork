

import pygame
class IGroup(pygame.sprite.Group):
    def draw(self, surface):
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            self.spritedict[spr] = surface_blit(spr.image, spr.rect)
            if spr.weapon:
                self.spritedict[spr.weapon] = surface_blit(spr.weapon.image, spr.weapon.rect)
        self.lostsprites = []