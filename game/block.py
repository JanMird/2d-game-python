import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
blwidth = 30

bldefaultrectx = 0
bldefaultrecty = 0
bldefaulthealth = 3


class block(pygame.sprite.Sprite):
    def __init__(self):
        self.type = 'block'
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((blwidth, blwidth))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = bldefaultrectx
        self.rect.y = bldefaultrecty
        self.health = bldefaulthealth

    def update(self):
        pass

    def damage(self):
        pass

