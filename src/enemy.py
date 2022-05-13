import pygame
from src.bullet import bullet
from src.Globals import ENTWIDTH, ENTWIDTH, ENEMYCOL, ENDEFAULTSPEED, \
    ENDEFAULTRECTX, ENDEFAULTRECTY, ENDEFAULTDIR, ENDEFAULTHEALTH, \
    TURNFREQ, SHOOTFREQ, ENBULGEN


class enemy(pygame.sprite.Sprite):
    def __init__(self, type='enemy', width=ENTWIDTH, height=ENTWIDTH, \
                 color=ENEMYCOL, speed=ENDEFAULTSPEED, x=ENDEFAULTRECTX, \
                 y=ENDEFAULTRECTY, dir=ENDEFAULTDIR, \
                 health=ENDEFAULTHEALTH, turnfr=TURNFREQ, shootfr=SHOOTFREQ):
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
        self.direction = dir
        self.health = health
        self.turnfr = turnfr
        self.movecooldown = 0
        self.shootfr = shootfr
        self.shootcooldown = 0

    def update(self):
        self.movecooldown += 1
        if self.movecooldown > self.turnfr:
            if self.direction == 'right':
                self.direction = 'up'
            elif self.direction == 'up':
                self.direction = 'left'
            elif self.direction == 'left':
                self.direction = 'down'
            elif self.direction == 'down':
                self.direction = 'right'
            self.movecooldown = 0
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

    def shoot(self, len=ENBULGEN):
            self.shootcooldown = 0
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

