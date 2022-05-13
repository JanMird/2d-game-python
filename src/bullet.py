import pygame
from src.Globals import BUWIDTH, BULCOL, BULDEFAULTRECTX, \
    BULDEFAULTRECTY, BULDEFAULTSPEED, BULDEFAULTDAMAGE, BULDEFAULTDIR


class bullet(pygame.sprite.Sprite):
    def __init__(self, type='bullet', width=BUWIDTH, \
                 height=BUWIDTH, color=BULCOL, \
                 x=BULDEFAULTRECTX, \
                 y=BULDEFAULTRECTY, \
                 speed=BULDEFAULTSPEED, \
                 damege=BULDEFAULTDAMAGE, \
                 dir=BULDEFAULTDIR):
        self.type = type
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.damage = damege
        self.direction = dir

    def update(self):
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed

