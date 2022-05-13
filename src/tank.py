import pygame
from src.bullet import bullet
from src.Globals import HTANKWIDTH, HTANKCOL, HTANKSPEED, HTANKDX, \
    HTANKDY, HTANKDDIR, HTANKDHEALTH, TBULGEN 


class tank(pygame.sprite.Sprite):
    def __init__(self, type='tank', width=HTANKWIDTH, \
                 height=HTANKWIDTH, color=HTANKCOL, \
                 speed=HTANKSPEED, x=HTANKDX, \
                 y=HTANKDY, direction=HTANKDDIR, \
                 health=HTANKDHEALTH):
        self.type = type
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.oldx = x
        self.oldy = y
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.health = health

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

    def shoot(self, len=TBULGEN):
        a = bullet()
        a.direction = self.direction
        if self.direction == 'right':
            a.rect.x = self.rect.x + self.image.get_width() + len
            a.rect.y = self.rect.y + self.image.get_height() // 2
        elif self.direction == 'left':
            a.rect.x = self.rect.x - len
            a.rect.y = self.rect.y + self.image.get_height() // 2
        if self.direction == 'up':
            a.rect.x = self.rect.x + self.image.get_width() // 2
            a.rect.y = self.rect.y - len
        if self.direction == 'down':
            a.rect.x = self.rect.x + self.image.get_width() // 2
            a.rect.y = self.rect.y + self.image.get_height() + len
        return a

