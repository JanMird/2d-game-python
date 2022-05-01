import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
buwidth = 5

buldefaultrectx = 0
buldefaultrecty = 0
buldefaultspeed = 9
buldefaultdamage = 1
buldefaultdir = 'right'


class bullet(pygame.sprite.Sprite):
    def __init__(self, type='bullet', width=buwidth, height=buwidth, \
                 color=RED, x=buldefaultrectx, y=buldefaultrecty, \
                 speed=buldefaultspeed, damege=buldefaultdamage, \
                 dir=buldefaultdir):
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

