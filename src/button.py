import pygame
from src.Globals import TSIZE, BUTTCOL, BACKGCOL, BUTTON_WIDTH, \
    BUTTON_HEIGHT, UPDBUTTCOL, UPDBUTBGCOL


class button():
    """
    Simple class for button object, for main manu.

    Attributes
    ----------
    type : str
	Object type
    font : pygame.font
        Font of text on button
    text : pygame.font
        Text on button
    text_rect : pygame.rect
        Rect for text
    but_rect : pygame.rect
        Rect for button
    image : Surface
        Block picture
    rect : rect
        Block rectangle
    clicked : int
        Click flag
    rect_col : RGB
        Button color

    Methods
    -------
    init(self):
        Create class object.
    change_but(self, text='txt not stated', \
                   tcol=UPDBUTTCOL, bg=UPDBUTBGCOL):
        Changes button view               
    show(self, screen=None):
        Draws button
    ismouseon(self, pos):
        Checks if mouse moved on button
    update(self, text1='movedon', text2='default', \
               tcol=BUTTCOL, bg=BACKGCOL, \
               cltcol=UPDBUTTCOL, clbg=UPDBUTBGCOL, \
               ):
        Checks if changes are neccecery, and change view if true
    """

    def __init__(self, text, x, y, textsize=TSIZE, \
                 tcol=BUTTCOL, bg=BACKGCOL, \
                 type='button'):
        """
         Constructs all the necessary attributes for button object.
         Parameters
         ----------
             type : string
                 Object type
             text : string
                 Text for button
             x : int
                 X coordinate for button
             y : int
                 Y coordinate for button
             textsize : int
                 Text size
             tcol : RGB
                 Text color
             bg : RGB
                 Background color
        """
        self.type = type
        self.font = pygame.font.SysFont("impact", textsize)
        self.text = self.font.render(text, True, tcol)
        self.text_rect = self.text.get_rect()
        self.but_rect = self.text.get_rect()
        self.but_rect.width = BUTTON_WIDTH
        self.but_rect.height = BUTTON_HEIGHT
        self.text_rect.center = (x, y)
        self.but_rect.center = (x, y)
        self.clicked = 0
        self.rect_col = bg

    def change_but(self, text='txt not stated', \
                   tcol=UPDBUTTCOL, bg=UPDBUTBGCOL):
        """
        Changes button view.
        Parameters
        ----------
        Self
        text : string
            New text
        tcol : RGB
            New text color
        bg : RGB
            New background color
        
        Returns
        -------
        None
        """
        self.text = self.font.render(text, True, tcol)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.but_rect.center
        self.rect_col = bg

    def show(self, screen=None):
        """
        Draws button.
        
        Parameters
        ----------
        Self
        screen : pygame.screen
            Screen where to draw
        
        Returns
        -------
        None
        """
        pygame.draw.rect(screen, self.rect_col, self.but_rect)
        screen.blit(self.text, self.text_rect)

    def ismouseon(self, pos):
        """
        Checks if mouse moved on button.
        
        Parameters
        ----------
        Self
        pos : tuple
            Mouse position
        
        Returns
        -------
        True if it is, false otherwise
        """
        if pos[0] <= self.but_rect.x + self.but_rect.width and \
                pos[0] >= self.but_rect.x \
                and pos[1] <= self.but_rect.y + self.but_rect.height \
                and pos[1] >= self.but_rect.y:
            return 1
        else:
            return 0

    def update(self, text1='movedon', text2='default', \
               tcol=BUTTCOL, bg=BACKGCOL, \
               cltcol=UPDBUTTCOL, clbg=UPDBUTBGCOL):
        """
        Checks if changes are neccecery, and change view if true.
        
        Parameters
        ----------
        Self
        text1 : string
            Text for not changing conditions
        text2 : string
            Text for changing conditions
        tcol : RGB
            Text color for not changing conditions
        bg : RGB
            Background color for not changing conditions
        cltcol : RGB
            Text for changing conditions
        clbg : RGB
            Background color for changing conditions
        
        Returns
        -------
        None
        """
        pos = pygame.mouse.get_pos()
        if self.clicked == 0:
            if self.ismouseon(pos):
                self.change_but(text1, cltcol, clbg)
            else:
                self.change_but(text2, tcol=tcol, bg=bg)

