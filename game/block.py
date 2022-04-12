import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
blwidth = 30


class block(pygame.sprite.Sprite):
    def __init__(self):
        self.type = 'block'
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((blwidth, blwidth))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.health = 1

    def update(self):
        pass

    def damage(self):
        pass
