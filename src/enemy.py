import pygame
from src.bullet import bullet
from src.Globals import ENTWIDTH, ENTWIDTH, ENEMYCOL, ENDEFAULTSPEED, \
    ENDEFAULTRECTX, ENDEFAULTRECTY, ENDEFAULTDIR, ENDEFAULTHEALTH, \
    TURNFREQ, SHOOTFREQ, ENBULGEN


class enemy(pygame.sprite.Sprite):
    """
    A class to represent enemy object of the game - enemy tank.

    Attributes
    ----------
    type : str
	Object type
    image : pygame.Surface
        Enemy picture
    rect : pygame.rect
        Enemy rectangle
    speed : int
        Enemy move speed
    oldx : int
        X coordinate of enemy before tick
    oldy : int
        Y coordinate of enemy before tick
    direction : string
        Enemy move direction
    health : int
        Enemy lives
    turnfr : int
        Frequancy of enemy turns
    movecooldown : int
        Tick for turnfr
    shootfr : int
        Frequancy of enemy shooting
    shootcooldown : int
        Tick for shootfr

    Methods
    -------
    init(self):
        Create class object.
    update(self):
        Implements enemy movement
    shoot(self, len=ENBULGEN):
        Implements enemy shooting, retuns bullet

    """

    def __init__(self, type='enemy', width=ENTWIDTH, height=ENTWIDTH, \
                 color=ENEMYCOL, speed=ENDEFAULTSPEED, x=ENDEFAULTRECTX, \
                 y=ENDEFAULTRECTY, dir=ENDEFAULTDIR, \
                 health=ENDEFAULTHEALTH, turnfr=TURNFREQ, shootfr=SHOOTFREQ):
        """
        Constructs all the necessary attributes for the enemy object.

        Parameters
        ----------
            type : string
                Type object
	    width, height : int, int
		Size of enemy surface
	    color : RGB
		Enemy color
	    speed : int
		Enemy move speed
	    x : int
		X coordinate of enemy tank
	    y : int
		Y coordinate of enemy tank
	    dir : string
		Enemy move direction
	    health : int
		Enemy tank lives
            turnfr : int 
                Frequancy of enemy turns
            shootfr : int
                Frequancy of enemy shooting
         """
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
        """
        Implements enemy movement.

        Parameters
        ----------
        Self

        Returns
        -------
        None
        """
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
        """
        Implements enemy shooting, retuns bullet.

        Parameters
        ----------
        Self
        len : int
            Lenght from tank to generate bullet

        Returns
        -------
        bullet
        """
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

