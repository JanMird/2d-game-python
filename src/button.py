import pygame
from src.Globals import TSIZE, BUTTCOL, BACKGCOL, BUTTON_WIDTH, \
    BUTTON_HEIGHT, UPDBUTTCOL, UPDBUTBGCOL


class button():
    def __init__(self, text, x, y, textsize=TSIZE, \
                 tcol=BUTTCOL, bg=BACKGCOL, \
                 type='button'):
        self.type = type
        self.font = pygame.font.SysFont("impact", textsize)
        self.text = self.font.render(text, True, tcol)
        self.text_rect = self.text.get_rect()
        self.but_rect = self.text.get_rect()
        self.but_rect.width = BUTTON_WIDTH
        self.but_rect.height = BUTTON_HEIGHT
        self.text_rect.center = (x, y)
        self.but_rect.center = (x, y)
        self.state = 0
        self.clicked = 0
        self.rect_col = bg

    def change_but(self, text='txt not stated', \
                   tcol=UPDBUTTCOL, bg=UPDBUTBGCOL):
        self.text = self.font.render(text, True, tcol)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.but_rect.center
        self.rect_col = bg

    def show(self, screen=None):
        pygame.draw.rect(screen, self.rect_col, self.but_rect)
        screen.blit(self.text, self.text_rect)

    def ismouseon(self, pos):
        if pos[0] <= self.but_rect.x + self.but_rect.width and \
                pos[0] >= self.but_rect.x \
                and pos[1] <= self.but_rect.y + self.but_rect.height \
                and pos[1] >= self.but_rect.y:
            return 1
        else:
            return 0

    def update(self, text1='movedon', text2='default', \
               tcol=BUTTCOL, bg=BACKGCOL, \
               cltcol=UPDBUTTCOL, clbg=UPDBUTBGCOL, \
               ):
        pos = pygame.mouse.get_pos()
        if self.clicked == 0:
            if self.ismouseon(pos):
                self.change_but(text1, cltcol, clbg)
            else:
                self.change_but(text2, tcol=tcol, bg=bg)
                self.state = 0

