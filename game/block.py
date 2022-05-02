import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
blwidth = 30

bldefaultrectx = 0
bldefaultrecty = 0
bldefaulthealth = 1


class block(pygame.sprite.Sprite):
    def __init__(self, type='block', width=blwidth, height=blwidth, \
                 color=BLUE, x=bldefaultrectx, y=bldefaultrecty, \
                 health=bldefaulthealth):
        self.type = type
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health

    def update(self):
        pass

