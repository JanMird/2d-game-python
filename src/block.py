import pygame
from src.Globals import BLWIDTH, BLOCKCOL, BLDEFAULTRECTX, \
    BLDEFAULTRECTY, BLDEFAULTHEALTH


class block(pygame.sprite.Sprite):
    def __init__(self, type='block', width=BLWIDTH, \
                 height=BLWIDTH, color=BLOCKCOL, \
                 x=BLDEFAULTRECTX, y=BLDEFAULTRECTY, \
                 health=BLDEFAULTHEALTH):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health

