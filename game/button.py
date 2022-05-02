import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

button_width = 350
button_height = 65


class button():
    def __init__(self, text, x, y, tsize=50, tcol=BLUE, bg=GREEN, type=None):
        self.type = type
        self.font = pygame.font.SysFont("impact", tsize)
        self.text = self.font.render(text, True, tcol)
        self.text_rect = self.text.get_rect()
        self.but_rect = self.text.get_rect()
        self.but_rect.width = button_width
        self.but_rect.height = button_height
        self.text_rect.center = (x, y)
        self.but_rect.center = (x, y)
        self.state = 0
        self.clicked = 0
        self.rect_col = bg

    def change_but(self, text='txt not stated', tcol=GREEN, bg=BLUE):
        self.text = self.font.render(text, True, tcol)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.but_rect.center
        self.rect_col = bg

    def show(self, screen=None):
        pygame.draw.rect(screen, self.rect_col, self.but_rect)
        screen.blit(self.text, self.text_rect)

    def ismouseon(self, pos):
        if pos[0] <= self.but_rect.x + self.but_rect.width and pos[0] >= self.but_rect.x \
                and pos[1] <= self.but_rect.y + self.but_rect.height \
                and pos[1] >= self.but_rect.y:
            return 1
        else:
            return 0

    def update(self, text1='movedon', text2='default', tcol=GREEN, bg=RED):
        pos = pygame.mouse.get_pos()
        if self.state == 0:
            if self.ismouseon(pos):
                self.change_but(text1, tcol, bg)
                self.state = 1
        if self.state == 1:
            if not self.ismouseon(pos):
                self.change_but(text2, tcol=BLUE, bg=GREEN)
                self.state = 0

