import pygame
from src.bullet import bullet
from src.Globals import HTANKWIDTH, HTANKCOL, HTANKSPEED, HTANKDX, \
    HTANKDY, HTANKDDIR, HTANKDHEALTH, TBULGEN


class tank(pygame.sprite.Sprite):
    """
    A class to represent main object of the game - Hero tank.

    Attributes
    ----------
    type : str
	Object type
    image : pygame.Surface
        Hero picture
    rect : pygame.rect
        Hero rectangle
    speed : int
        Hero move speed
    oldx : int
        X coordinate of hero tank before tick
    oldy : int
        Y coordinate of hero tank before tick
    direction : string
        Tank move direction
    health : int
        Hero tank lives

    Methods
    -------
    init(self):
        Create class object.
    update(self):
        Implements tanks movement
    shoot(self, len=TBULGEN):
        Implements tank shooting, retuns bullet

    """

    def __init__(self, type='tank', width=HTANKWIDTH, \
                 height=HTANKWIDTH, color=HTANKCOL, \
                 speed=HTANKSPEED, x=HTANKDX, \
                 y=HTANKDY, direction=HTANKDDIR, \
                 health=HTANKDHEALTH):
        """
        Constructs all the necessary attributes for the tank object.

        Parameters
        ----------
            type : string
                Type object
	    width, height : int, int
		Size of tank surface
	    color : RGB
		Hero tank color
	    speed : int
		Hero move speed
	    x : int
		X coordinate of hero tank
	    y : int
		Y coordinate of hero tank
	    direction : string
		Move direction
	    health : int
		Hero tank lives
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
        self.direction = direction
        self.health = health

    def update(self):
        """
        Implements tank movement.

        Parameters
        ----------
        Self

        Returns
        -------
        None
        """
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
        """
        Implements tank shooting, retuns bullet.

        Parameters
        ----------
        Self
        len : int
            Lenght from tank to generate bullet

        Returns
        -------
        bullet
        """
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

