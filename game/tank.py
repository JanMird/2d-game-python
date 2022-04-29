import pygame
from bullet import bullet

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
twidth = 30

tdefaultspeed = 5
tdefaultrectx = 100
tdefaultrecty = 100
tdefaulthealth = 3
tdefaultdir = 'right'

bulgenl = 5

class tank(pygame.sprite.Sprite):
    def __init__(self):
        self.type = 'tank'
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((twidth, twidth))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.speed = tdefaultspeed
        self.oldx = tdefaultrectx
        self.oldy = tdefaultrecty
        self.rect.x = tdefaultrectx
        self.rect.y = tdefaultrecty
        self.direction = tdefaultdir
        self.health = tdefaulthealth

    def update(self):
        self.oldx = self.rect.x
        self.oldy = self.rect.y
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed

    def drawinterface(self):
        pass

    def ishot(self, bullet):
        pass

    def die(self):
        pass

    def isalive(self):
        pass

    def shoot(self):
        a = bullet()
        a.direction = self.direction
        if self.direction == 'right':
            a.rect.x = self.rect.x + self.image.get_width() + bulgenl
            a.rect.y = self.rect.y + self.image.get_height() // 2
        elif self.direction == 'left':
            a.rect.x = self.rect.x - bulgenl
            a.rect.y = self.rect.y + self.image.get_height() // 2
        if self.direction == 'up':
            a.rect.x = self.rect.x + self.image.get_width() // 2
            a.rect.y = self.rect.y - bulgenl
        if self.direction == 'down':
            a.rect.x = self.rect.x + self.image.get_width() // 2
            a.rect.y = self.rect.y + self.image.get_height() + bulgenl
        return a

