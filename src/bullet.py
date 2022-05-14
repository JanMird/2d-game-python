import pygame
from src.Globals import BUWIDTH, BULCOL, BULDEFAULTRECTX, \
    BULDEFAULTRECTY, BULDEFAULTSPEED, BULDEFAULTDAMAGE, BULDEFAULTDIR


class bullet(pygame.sprite.Sprite):
    """
    A class to represent damage object of the game - bullet.

    Attributes
    ----------
    type : str
	Object type
    image : Surface
        Bullet pygame.picture
    rect : rect
        Bullet pygame.rectangle
    speed : int
        Bullet move speed
    direction : string
        Bullet move direction
    damage : int
        Bullet damage

    Methods
    -------
    init(self):
        Create class object.
    update(self):
        Implements bullet movement

    """

    def __init__(self, type='bullet', width=BUWIDTH, \
                 height=BUWIDTH, color=BULCOL, \
                 x=BULDEFAULTRECTX, \
                 y=BULDEFAULTRECTY, \
                 speed=BULDEFAULTSPEED, \
                 damage=BULDEFAULTDAMAGE, \
                 dir=BULDEFAULTDIR):
        """
        Constructs all the necessary attributes for the bullet object.

        Parameters
        ----------
            type : string
                Type object
	    width, height : int, int
		Size of bullet surface
	    color : RGB
		Bullet color
	    speed : int
		Bullet move speed
	    x : int
		X coordinate of bullet
	    y : int
		Y coordinate of bullet
	    dir : string
		Bullet move direction
	    damage : int
		Bullet damage
         """
        self.type = type
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.damage = damage
        self.direction = dir

    def update(self):
        """
        Implements bullet movement.

        Parameters
        ----------
        Self

        Returns
        -------
        None
        """
        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed

