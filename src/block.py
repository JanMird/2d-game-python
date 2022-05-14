import pygame
from src.Globals import BLWIDTH, BLOCKCOL, BLDEFAULTRECTX, \
    BLDEFAULTRECTY, BLDEFAULTHEALTH


class block(pygame.sprite.Sprite):
    """
    A class to represent map object of the game - block.

    Attributes
    ----------
    type : str
	Object type
    image : Surface
        Block pygame.picture
    rect : rect
        Block pygame.rectangle
    health : int
        Block health

    Methods
    -------
    init(self):
        Create class object.

    """

    def __init__(self, type='block', width=BLWIDTH, \
                 height=BLWIDTH, color=BLOCKCOL, \
                 x=BLDEFAULTRECTX, y=BLDEFAULTRECTY, \
                 health=BLDEFAULTHEALTH):
        """
        Constructs all the necessary attributes for the bullet object.

        Parameters
        ----------
            type : string
                Type object
	    width, height : int, int
		Size of block surface
	    color : RGB
		Block color
	    x : int
		X coordinate of block
	    y : int
		Y coordinate of block
	    health : int
		Block health
         """
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health

