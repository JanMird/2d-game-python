import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
buwidth = 5


class bullet(pygame.sprite.Sprite):
    def __init__(self):
        self.type = 'bullet'
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((buwidth, buwidth))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 9
        self.damage = 1
        self.direction = 'right'

    def update(self):
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed

    def hit(self):
        pass
